// Read-only compact finalized-receipt verifier for live evidence capture.
(async () => {
  const { createClient, chains } = await import('genlayer-js');
  const hash = process.argv[2];
  if (!/^0x[0-9a-fA-F]{64}$/.test(hash || '')) {
    throw new Error('Usage: node scripts/receipt-summary.cjs <transaction-hash>');
  }

  const client = createClient({ chain: chains.studionet });
  const tx = await client.waitForTransactionReceipt({
    hash,
    status: 'FINALIZED',
    retries: 100,
    interval: 3000,
  });
  const leader = tx.consensus_data?.leader_receipt?.[0];
  const summary = {
    hash: tx.tx_id || hash,
    status: tx.statusName || (Number(tx.status) === 7 ? 'FINALIZED' : String(tx.status)),
    status_code: Number(tx.status),
    result: tx.result_name,
    recipient: tx.to_address,
    contract: tx.data?.contract_address,
    leader_execution: leader?.execution_result,
    leader_error: leader?.genvm_result?.error_code || null,
    votes: tx.consensus_data?.votes || {},
  };
  console.log(JSON.stringify(summary, null, 2));
  if (summary.status !== 'FINALIZED' || summary.result !== 'MAJORITY_AGREE'
      || summary.leader_execution !== 'SUCCESS') {
    process.exitCode = 1;
  }
})().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
