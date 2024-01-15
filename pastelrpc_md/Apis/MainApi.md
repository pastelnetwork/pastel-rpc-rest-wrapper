# MainApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addMultisigAddressAddmultisigaddressPost**](MainApi.md#addMultisigAddressAddmultisigaddressPost) | **POST** /addmultisigaddress | Add a multisignature address |
| [**addNodeAddnodePost**](MainApi.md#addNodeAddnodePost) | **POST** /addnode | Add, remove, or try a connection to a node |
| [**backupWalletBackupwalletPost**](MainApi.md#backupWalletBackupwalletPost) | **POST** /backupwallet | Backup the wallet to a destination |
| [**changeWalletPassphraseWalletpassphrasechangePost**](MainApi.md#changeWalletPassphraseWalletpassphrasechangePost) | **POST** /walletpassphrasechange | Change the wallet passphrase |
| [**createMultisigCreatemultisigPost**](MainApi.md#createMultisigCreatemultisigPost) | **POST** /createmultisig | Create a multisig address |
| [**createRawTransactionCreaterawtransactionPost**](MainApi.md#createRawTransactionCreaterawtransactionPost) | **POST** /createrawtransaction | Create a raw transaction |
| [**decodeRawTransactionDecoderawtransactionPost**](MainApi.md#decodeRawTransactionDecoderawtransactionPost) | **POST** /decoderawtransaction | Decode a raw transaction |
| [**decodeScriptDecodescriptPost**](MainApi.md#decodeScriptDecodescriptPost) | **POST** /decodescript | Decode a hex-encoded script |
| [**disconnectNodeDisconnectnodePost**](MainApi.md#disconnectNodeDisconnectnodePost) | **POST** /disconnectnode | Disconnect from a specified node |
| [**dumpPrivKeyDumpprivkeyGet**](MainApi.md#dumpPrivKeyDumpprivkeyGet) | **GET** /dumpprivkey | Reveal the private key for a given address |
| [**dumpWalletDumpwalletPost**](MainApi.md#dumpWalletDumpwalletPost) | **POST** /dumpwallet | Dump wallet keys |
| [**encryptWalletEncryptwalletPost**](MainApi.md#encryptWalletEncryptwalletPost) | **POST** /encryptwallet | Encrypt the wallet with a passphrase |
| [**estimateFeeEstimatefeeGet**](MainApi.md#estimateFeeEstimatefeeGet) | **GET** /estimatefee | Estimate the transaction fee per kilobyte |
| [**estimateNftStorageFeeTicketsToolsEstimatenftstoragefeeGet**](MainApi.md#estimateNftStorageFeeTicketsToolsEstimatenftstoragefeeGet) | **GET** /tickets/tools/estimatenftstoragefee | Estimate storage fee for NFT registration |
| [**estimatePriorityEstimatepriorityGet**](MainApi.md#estimatePriorityEstimatepriorityGet) | **GET** /estimatepriority | Estimate the transaction priority for zero-fee confirmation |
| [**executeMasternodeCommandMasternodeCommandPost**](MainApi.md#executeMasternodeCommandMasternodeCommandPost) | **POST** /masternode/command | Execute masternode related actions |
| [**fixMissingTransactionsFixmissingtxsStartingHeightGet**](MainApi.md#fixMissingTransactionsFixmissingtxsStartingHeightGet) | **GET** /fixmissingtxs/{starting_height} | Fix Missing Transactions |
| [**fundRawTransactionFundrawtransactionPost**](MainApi.md#fundRawTransactionFundrawtransactionPost) | **POST** /fundrawtransaction | Add inputs to a transaction |
| [**generateBlocksGeneratePost**](MainApi.md#generateBlocksGeneratePost) | **POST** /generate | Mine blocks immediately |
| [**generatePastelIdNewkeyPastelidNewkeyPost**](MainApi.md#generatePastelIdNewkeyPastelidNewkeyPost) | **POST** /pastelid/newkey | Generate new Pastel ID and keys |
| [**generateReportGenerateReportReportNameGet**](MainApi.md#generateReportGenerateReportReportNameGet) | **GET** /generate-report/{report_name} | Generate various reports |
| [**getAccountAddressGetaccountaddressGet**](MainApi.md#getAccountAddressGetaccountaddressGet) | **GET** /getaccountaddress | Get the current Pastel address for receiving payments |
| [**getAccountGetaccountZcashaddressGet**](MainApi.md#getAccountGetaccountZcashaddressGet) | **GET** /getaccount/{zcashaddress} | Get the account associated with a Pastel address |
| [**getActionFeesStoragefeeGetactionfeesGet**](MainApi.md#getActionFeesStoragefeeGetactionfeesGet) | **GET** /storagefee/getactionfees | Get action fees based on data size |
| [**getAddedNodeInfoGetaddednodeinfoGet**](MainApi.md#getAddedNodeInfoGetaddednodeinfoGet) | **GET** /getaddednodeinfo | Get information about added nodes |
| [**getAddressMempoolGetaddressmempoolGet**](MainApi.md#getAddressMempoolGetaddressmempoolGet) | **GET** /getaddressmempool | Get all mempool deltas for an address |
| [**getAddressesByAccountGetaddressesbyaccountGet**](MainApi.md#getAddressesByAccountGetaddressesbyaccountGet) | **GET** /getaddressesbyaccount | Get addresses by account |
| [**getBalanceGetbalanceGet**](MainApi.md#getBalanceGetbalanceGet) | **GET** /getbalance | Get the server&#39;s total available balance |
| [**getBestBlockHashGetbestblockhashGet**](MainApi.md#getBestBlockHashGetbestblockhashGet) | **GET** /getbestblockhash | Get the hash of the best block |
| [**getBlockCountGetblockcountGet**](MainApi.md#getBlockCountGetblockcountGet) | **GET** /getblockcount | Get the current block count |
| [**getBlockDeltasGetblockdeltasBlockHashGet**](MainApi.md#getBlockDeltasGetblockdeltasBlockHashGet) | **GET** /getblockdeltas/{block_hash} | Get block deltas |
| [**getBlockGetblockGet**](MainApi.md#getBlockGetblockGet) | **GET** /getblock | Get block data |
| [**getBlockHashGetblockhashGet**](MainApi.md#getBlockHashGetblockhashGet) | **GET** /getblockhash | Get the hash of a block at a specific index |
| [**getBlockHeaderGetblockheaderBlockHashGet**](MainApi.md#getBlockHeaderGetblockheaderBlockHashGet) | **GET** /getblockheader/{block_hash} | Get information about a block header |
| [**getBlockSubsidyGetblocksubsidyGet**](MainApi.md#getBlockSubsidyGetblocksubsidyGet) | **GET** /getblocksubsidy | Get block subsidy reward information |
| [**getBlockTemplateGetblocktemplatePost**](MainApi.md#getBlockTemplateGetblocktemplatePost) | **POST** /getblocktemplate | Get data needed to construct a block to work on |
| [**getBlockchainInfoGetblockchaininfoGet**](MainApi.md#getBlockchainInfoGetblockchaininfoGet) | **GET** /getblockchaininfo | Get blockchain information |
| [**getChainTipsGetchaintipsGet**](MainApi.md#getChainTipsGetchaintipsGet) | **GET** /getchaintips | Get information about all known chain tips |
| [**getConnectionCountGetconnectioncountGet**](MainApi.md#getConnectionCountGetconnectioncountGet) | **GET** /getconnectioncount | Get the number of connections to other nodes |
| [**getDeprecationInfoGetdeprecationinfoGet**](MainApi.md#getDeprecationInfoGetdeprecationinfoGet) | **GET** /getdeprecationinfo | Get deprecation information of the current version |
| [**getDifficultyGetdifficultyGet**](MainApi.md#getDifficultyGetdifficultyGet) | **GET** /getdifficulty | Get the current proof-of-work difficulty |
| [**getFeeScheduleGetfeescheduleGet**](MainApi.md#getFeeScheduleGetfeescheduleGet) | **GET** /getfeeschedule | Get the current fee schedule |
| [**getGenerateGetgenerateGet**](MainApi.md#getGenerateGetgenerateGet) | **GET** /getgenerate | Check if the server is set to generate coins |
| [**getInfoGetinfoGet**](MainApi.md#getInfoGetinfoGet) | **GET** /getinfo | Get various state info |
| [**getLocalSolpsGetlocalsolpsGet**](MainApi.md#getLocalSolpsGetlocalsolpsGet) | **GET** /getlocalsolps | Get average local solutions per second |
| [**getMemoryInfoGetmemoryinfoGet**](MainApi.md#getMemoryInfoGetmemoryinfoGet) | **GET** /getmemoryinfo | Get memory usage information |
| [**getMempoolInfoGetmempoolinfoGet**](MainApi.md#getMempoolInfoGetmempoolinfoGet) | **GET** /getmempoolinfo | Get active state of the TX memory pool |
| [**getMiningInfoGetmininginfoGet**](MainApi.md#getMiningInfoGetmininginfoGet) | **GET** /getmininginfo | Get mining-related information |
| [**getNetTotalsGetnettotalsGet**](MainApi.md#getNetTotalsGetnettotalsGet) | **GET** /getnettotals | Get network traffic information |
| [**getNetworkInfoGetnetworkinfoGet**](MainApi.md#getNetworkInfoGetnetworkinfoGet) | **GET** /getnetworkinfo | Get various state info regarding P2P networking |
| [**getNetworkSolpsGetnetworksolpsGet**](MainApi.md#getNetworkSolpsGetnetworksolpsGet) | **GET** /getnetworksolps | Get estimated network solutions per second |
| [**getNetworksInfoGetnetworksinfoGet**](MainApi.md#getNetworksInfoGetnetworksinfoGet) | **GET** /getnetworksinfo | Get information about all the networks |
| [**getNewAddressGetnewaddressGet**](MainApi.md#getNewAddressGetnewaddressGet) | **GET** /getnewaddress | Generate a new Pastel address |
| [**getNextBlockSubsidyGetnextblocksubsidyGet**](MainApi.md#getNextBlockSubsidyGetnextblocksubsidyGet) | **GET** /getnextblocksubsidy | Get subsidy rewards for the next block |
| [**getPeerInfoGetpeerinfoGet**](MainApi.md#getPeerInfoGetpeerinfoGet) | **GET** /getpeerinfo | Get data about each connected network node |
| [**getRawChangeAddressGetrawchangeaddressGet**](MainApi.md#getRawChangeAddressGetrawchangeaddressGet) | **GET** /getrawchangeaddress | Get a new Pastel address for receiving change |
| [**getRawMempoolGetrawmempoolGet**](MainApi.md#getRawMempoolGetrawmempoolGet) | **GET** /getrawmempool | Get all transaction IDs in memory pool |
| [**getRawTransactionGetrawtransactionPost**](MainApi.md#getRawTransactionGetrawtransactionPost) | **POST** /getrawtransaction | Get the raw transaction data |
| [**getReceivedByAccountGetreceivedbyaccountGet**](MainApi.md#getReceivedByAccountGetreceivedbyaccountGet) | **GET** /getreceivedbyaccount | Get the total amount received by an account |
| [**getReceivedByAddressGetreceivedbyaddressGet**](MainApi.md#getReceivedByAddressGetreceivedbyaddressGet) | **GET** /getreceivedbyaddress | Get the total amount received by a Pastel address |
| [**getStorageFeeGetFeeStoragefeeGetfeeGet**](MainApi.md#getStorageFeeGetFeeStoragefeeGetfeeGet) | **GET** /storagefee/getfee | Get the storage fee |
| [**getStorageFeesStoragefeeGetfeesGet**](MainApi.md#getStorageFeesStoragefeeGetfeesGet) | **GET** /storagefee/getfees | Get the current storage fees |
| [**getTotalStorageFeeTicketsToolsGettotalstoragefeePost**](MainApi.md#getTotalStorageFeeTicketsToolsGettotalstoragefeePost) | **POST** /tickets/tools/gettotalstoragefee | Calculate Total Storage Fee for NFT Registration |
| [**getTransactionGettransactionTxidGet**](MainApi.md#getTransactionGettransactionTxidGet) | **GET** /gettransaction/{txid} | Get detailed information about a transaction |
| [**getTxOutGettxoutGet**](MainApi.md#getTxOutGettxoutGet) | **GET** /gettxout | Get details about an unspent transaction output |
| [**getTxOutProofGettxoutproofGet**](MainApi.md#getTxOutProofGettxoutproofGet) | **GET** /gettxoutproof | Get proof of transaction inclusion in a block |
| [**getTxOutSetInfoGettxoutsetinfoGet**](MainApi.md#getTxOutSetInfoGettxoutsetinfoGet) | **GET** /gettxoutsetinfo | Get statistics about the unspent transaction output set |
| [**getTxfeeGettxfeeTxidGet**](MainApi.md#getTxfeeGettxfeeTxidGet) | **GET** /gettxfee/{txid} | Get transaction fee by txid |
| [**getWalletInfoGetwalletinfoGet**](MainApi.md#getWalletInfoGetwalletinfoGet) | **GET** /getwalletinfo | Get wallet state information |
| [**governanceActionGovernancePost**](MainApi.md#governanceActionGovernancePost) | **POST** /governance | Cast a vote or list governance tickets |
| [**importAddressImportaddressPost**](MainApi.md#importAddressImportaddressPost) | **POST** /importaddress | Import an address |
| [**importPrivKeyImportprivkeyPost**](MainApi.md#importPrivKeyImportprivkeyPost) | **POST** /importprivkey | Import a private key |
| [**importWalletImportwalletPost**](MainApi.md#importWalletImportwalletPost) | **POST** /importwallet | Import a wallet from a dump file |
| [**initializeMasternodeMasternodeInitPost**](MainApi.md#initializeMasternodeMasternodeInitPost) | **POST** /masternode/init | Initialize masternode |
| [**invalidateBlockInvalidateblockPost**](MainApi.md#invalidateBlockInvalidateblockPost) | **POST** /invalidateblock | Mark a block as permanently invalid |
| [**keypoolRefillKeypoolrefillPost**](MainApi.md#keypoolRefillKeypoolrefillPost) | **POST** /keypoolrefill | Refill the keypool |
| [**listAccountsListaccountsGet**](MainApi.md#listAccountsListaccountsGet) | **GET** /listaccounts | List account balances |
| [**listAddressAmountsListaddressamountsGet**](MainApi.md#listAddressAmountsListaddressamountsGet) | **GET** /listaddressamounts | List balance on each address |
| [**listAddressGroupingsListaddressgroupingsGet**](MainApi.md#listAddressGroupingsListaddressgroupingsGet) | **GET** /listaddressgroupings | List groups of addresses with common ownership |
| [**listBannedListbannedGet**](MainApi.md#listBannedListbannedGet) | **GET** /listbanned | List all banned IPs/Subnets |
| [**listLockUnspentListlockunspentGet**](MainApi.md#listLockUnspentListlockunspentGet) | **GET** /listlockunspent | List Temporarily Unspendable Outputs |
| [**listMasternodeOutputsMasternodeOutputsGet**](MainApi.md#listMasternodeOutputsMasternodeOutputsGet) | **GET** /masternode/outputs | List masternode outputs |
| [**listReceivedByAddressListreceivedbyaddressGet**](MainApi.md#listReceivedByAddressListreceivedbyaddressGet) | **GET** /listreceivedbyaddress | List balances by receiving address |
| [**listShieldedAddressesZListaddressesGet**](MainApi.md#listShieldedAddressesZListaddressesGet) | **GET** /z_listaddresses | List Shielded Addresses |
| [**listSinceBlockListsinceblockPost**](MainApi.md#listSinceBlockListsinceblockPost) | **POST** /listsinceblock | List transactions since a specific block |
| [**listTicketsTicketsListGet**](MainApi.md#listTicketsTicketsListGet) | **GET** /tickets/list | List tickets of a specific type |
| [**listTransactionsListtransactionsGet**](MainApi.md#listTransactionsListtransactionsGet) | **GET** /listtransactions | List recent transactions |
| [**listUnspentListunspentGet**](MainApi.md#listUnspentListunspentGet) | **GET** /listunspent | List Unspent Transaction Outputs |
| [**lockUnspentLockunspentPost**](MainApi.md#lockUnspentLockunspentPost) | **POST** /lockunspent | Lock or unlock unspent transaction outputs |
| [**masternodeBroadcastMasternodebroadcastPost**](MainApi.md#masternodeBroadcastMasternodebroadcastPost) | **POST** /masternodebroadcast | Create and relay masternode broadcast messages |
| [**masternodeClearCacheMasternodeClearCachePost**](MainApi.md#masternodeClearCacheMasternodeClearCachePost) | **POST** /masternode/clear-cache | Clear Masternode Cache Items |
| [**masternodeMakeConfMasternodeMakeConfPost**](MainApi.md#masternodeMakeConfMasternodeMakeConfPost) | **POST** /masternode/make_conf | Create Masternode Configuration |
| [**masternodeMessageMasternodeMessagePost**](MainApi.md#masternodeMessageMasternodeMessagePost) | **POST** /masternode/message | Interact with Masternode messages |
| [**masternodePoseBanScoreMasternodePoseBanScorePost**](MainApi.md#masternodePoseBanScoreMasternodePoseBanScorePost) | **POST** /masternode_pose_ban_score | Manage MasterNode PoSe Ban Score |
| [**masternodelistMasternodelistGet**](MainApi.md#masternodelistMasternodelistGet) | **GET** /masternodelist | Get a list of masternodes in different modes |
| [**moveMovePost**](MainApi.md#moveMovePost) | **POST** /move | Move amount from one account to another |
| [**pastelidNewkeyPastelidNewkeyPost**](MainApi.md#pastelidNewkeyPastelidNewkeyPost) | **POST** /pastelid_newkey | Generate new Pastel ID and associated keys |
| [**pastelidPasswdPastelidPasswdPost**](MainApi.md#pastelidPasswdPastelidPasswdPost) | **POST** /pastelid/passwd | Change passphrase for PastelID secure container |
| [**pastelidSignFilePastelidSignfilePost**](MainApi.md#pastelidSignFilePastelidSignfilePost) | **POST** /pastelid/signfile | Sign a file with a Pastel ID |
| [**pastelidVerifyFilePastelidVerifyFilePost**](MainApi.md#pastelidVerifyFilePastelidVerifyFilePost) | **POST** /pastelid/verify-file | Verify a file&#39;s signature with a Pastel ID |
| [**pastelidVerifyPastelidVerifyPost**](MainApi.md#pastelidVerifyPastelidVerifyPost) | **POST** /pastelid/verify | Verify a signature with PastelID |
| [**pingPingGet**](MainApi.md#pingPingGet) | **GET** /ping | Send a ping to all nodes |
| [**prioritiseTransactionPrioritisetransactionPost**](MainApi.md#prioritiseTransactionPrioritisetransactionPost) | **POST** /prioritisetransaction | Prioritise a transaction for mining |
| [**reconsiderBlockReconsiderblockPost**](MainApi.md#reconsiderBlockReconsiderblockPost) | **POST** /reconsiderblock | Reconsider a previously invalidated block |
| [**refreshMiningMnidInfoRefreshminingmnidinfoGet**](MainApi.md#refreshMiningMnidInfoRefreshminingmnidinfoGet) | **GET** /refreshminingmnidinfo | Refresh mining MNID information |
| [**registerActionTicketTicketsRegisterActionPost**](MainApi.md#registerActionTicketTicketsRegisterActionPost) | **POST** /tickets/register_action | Register new Action ticket |
| [**registerNftTicketTicketsRegisterNftPost**](MainApi.md#registerNftTicketTicketsRegisterNftPost) | **POST** /tickets/register/nft | Register a new NFT ticket |
| [**registerRoyaltyTicketTicketsRegisterRoyaltyPost**](MainApi.md#registerRoyaltyTicketTicketsRegisterRoyaltyPost) | **POST** /tickets/register_royalty | Register new change payee of the NFT royalty ticket |
| [**registerTransferTicketTicketsRegisterTransferPost**](MainApi.md#registerTransferTicketTicketsRegisterTransferPost) | **POST** /tickets/register/transfer | Register a transfer ticket |
| [**registerUsernameTicketsRegisterUsernamePost**](MainApi.md#registerUsernameTicketsRegisterUsernamePost) | **POST** /tickets/register/username | Register a Username Change Request ticket |
| [**resendWalletTransactionsResendwallettransactionsPost**](MainApi.md#resendWalletTransactionsResendwallettransactionsPost) | **POST** /resendwallettransactions | Re-broadcast unconfirmed wallet transactions |
| [**retrieveChaindataChaindataRetrievePost**](MainApi.md#retrieveChaindataChaindataRetrievePost) | **POST** /chaindata/retrieve | Retrieve data from the blockchain |
| [**scanForMissingTxsScanformissingtxsPost**](MainApi.md#scanForMissingTxsScanformissingtxsPost) | **POST** /scanformissingtxs | Scan for missing transactions |
| [**sendFromSendfromPost**](MainApi.md#sendFromSendfromPost) | **POST** /sendfrom | Send amount from an account to a Pastel address |
| [**sendManySendmanyPost**](MainApi.md#sendManySendmanyPost) | **POST** /sendmany | Send multiple transactions |
| [**sendRawTransactionSendrawtransactionPost**](MainApi.md#sendRawTransactionSendrawtransactionPost) | **POST** /sendrawtransaction | Submit a raw transaction to the network |
| [**sendToAddressSendtoaddressPost**](MainApi.md#sendToAddressSendtoaddressPost) | **POST** /sendtoaddress | Send an amount to a given address |
| [**setAccountSetaccountPost**](MainApi.md#setAccountSetaccountPost) | **POST** /setaccount | Associate a Pastel address with an account |
| [**setBanSetbanPost**](MainApi.md#setBanSetbanPost) | **POST** /setban | Add or Remove an IP/Subnet from the Ban List |
| [**setGenerateSetgeneratePost**](MainApi.md#setGenerateSetgeneratePost) | **POST** /setgenerate | Set generation on or off |
| [**setTxFeeSettxfeePost**](MainApi.md#setTxFeeSettxfeePost) | **POST** /settxfee | Set the transaction fee per kB |
| [**signMessageSignmessagePost**](MainApi.md#signMessageSignmessagePost) | **POST** /signmessage | Sign a message with the private key of a t-addr |
| [**signRawTransactionSignrawtransactionPost**](MainApi.md#signRawTransactionSignrawtransactionPost) | **POST** /signrawtransaction | Sign a raw transaction |
| [**signWithPastelIdPastelidSignPost**](MainApi.md#signWithPastelIdPastelidSignPost) | **POST** /pastelid/sign | Sign a text with Pastel ID |
| [**storageFeeStoragefeePost**](MainApi.md#storageFeeStoragefeePost) | **POST** /storagefee | Interact with Storage Fee and related actions |
| [**storagefeeSetfeeStoragefeeSetfeePost**](MainApi.md#storagefeeSetfeeStoragefeeSetfeePost) | **POST** /storagefee/setfee | Set a new fee for a specified fee type |
| [**storeChaindataChaindataStorePost**](MainApi.md#storeChaindataChaindataStorePost) | **POST** /chaindata/store | Store data in the blockchain |
| [**submitBlockSubmitblockPost**](MainApi.md#submitBlockSubmitblockPost) | **POST** /submitblock | Submit a new block to the network |
| [**ticketsFindByLabelTicketsFindbylabelTicketTypeLabelGet**](MainApi.md#ticketsFindByLabelTicketsFindbylabelTicketTypeLabelGet) | **GET** /tickets/findbylabel/{ticket_type}/{label} | Find tickets by label |
| [**ticketsFindTicketsFindGet**](MainApi.md#ticketsFindTicketsFindGet) | **GET** /tickets/find | Find Pastel tickets |
| [**ticketsGetTicketsGetGet**](MainApi.md#ticketsGetTicketsGetGet) | **GET** /tickets/get | Get a Pastel ticket by transaction ID |
| [**ticketsRegisterAcceptTicketsRegisterAcceptPost**](MainApi.md#ticketsRegisterAcceptTicketsRegisterAcceptPost) | **POST** /tickets/register/accept | Register an accept ticket |
| [**ticketsRegisterCollectionTicketsRegistercollectionPost**](MainApi.md#ticketsRegisterCollectionTicketsRegistercollectionPost) | **POST** /tickets/registercollection | Register a collection ticket |
| [**ticketsRegisterDownTicketsRegisterDownPost**](MainApi.md#ticketsRegisterDownTicketsRegisterDownPost) | **POST** /tickets/register/down | Register a Take Down Request Ticket |
| [**ticketsRegisterEthereumAddressTicketsRegisterEthereumaddressPost**](MainApi.md#ticketsRegisterEthereumAddressTicketsRegisterEthereumaddressPost) | **POST** /tickets/register/ethereumaddress | Register Ethereum Address Change Request |
| [**ticketsRegisterIdTicketsRegisterIdPost**](MainApi.md#ticketsRegisterIdTicketsRegisterIdPost) | **POST** /tickets/register_id | Register Pastel ID identity |
| [**ticketsRegisterMnidTicketsRegisterMnidPost**](MainApi.md#ticketsRegisterMnidTicketsRegisterMnidPost) | **POST** /tickets/register/mnid | Register Masternode PastelID |
| [**ticketsRegisterOfferTicketsRegisterOfferPost**](MainApi.md#ticketsRegisterOfferTicketsRegisterOfferPost) | **POST** /tickets/register/offer | Register an offer ticket |
| [**ticketsTicketsCommandGet**](MainApi.md#ticketsTicketsCommandGet) | **GET** /tickets/{command} | Execute Pastel Ticket Commands |
| [**ticketsToolsSearchthumbidsTicketsToolsSearchthumbidsPost**](MainApi.md#ticketsToolsSearchthumbidsTicketsToolsSearchthumbidsPost) | **POST** /tickets/tools/searchthumbids | Search for NFT registration tickets and thumbnail hash |
| [**ticketsToolsTicketsToolsPost**](MainApi.md#ticketsToolsTicketsToolsPost) | **POST** /tickets/tools | Execute various ticket tools commands |
| [**validateAddressValidateaddressPost**](MainApi.md#validateAddressValidateaddressPost) | **POST** /validateaddress | Validate a Pastel address |
| [**validateOwnershipTicketsToolsValidateownershipPost**](MainApi.md#validateOwnershipTicketsToolsValidateownershipPost) | **POST** /tickets/tools/validateownership | Validate item ownership by Pastel ID |
| [**verifyChainVerifychainGet**](MainApi.md#verifyChainVerifychainGet) | **GET** /verifychain | Verify the blockchain database |
| [**verifyMessageVerifymessagePost**](MainApi.md#verifyMessageVerifymessagePost) | **POST** /verifymessage | Verify a signed message |
| [**walletPassphraseWalletpassphrasePost**](MainApi.md#walletPassphraseWalletpassphrasePost) | **POST** /walletpassphrase | Unlock the wallet |
| [**walletlockWalletlockPost**](MainApi.md#walletlockWalletlockPost) | **POST** /walletlock | Lock the wallet |
| [**zExportKeyZExportkeyPost**](MainApi.md#zExportKeyZExportkeyPost) | **POST** /z_exportkey | Reveal the private key corresponding to a z-address |
| [**zExportViewingKeyZExportviewingkeyGet**](MainApi.md#zExportViewingKeyZExportviewingkeyGet) | **GET** /z_exportviewingkey | Export the viewing key for a Z-address |
| [**zExportWalletZExportwalletPost**](MainApi.md#zExportWalletZExportwalletPost) | **POST** /z_exportwallet | Export wallet keys |
| [**zGetBalanceZGetbalanceAddressGet**](MainApi.md#zGetBalanceZGetbalanceAddressGet) | **GET** /z_getbalance/{address} | Get the balance of an address |
| [**zGetNewAddressZGetnewaddressGet**](MainApi.md#zGetNewAddressZGetnewaddressGet) | **GET** /z_getnewaddress | Generate a new shielded address |
| [**zGetNotesCountZGetnotescountGet**](MainApi.md#zGetNotesCountZGetnotescountGet) | **GET** /z_getnotescount | Get the count of sapling notes in the wallet |
| [**zGetOperationStatusZGetoperationstatusGet**](MainApi.md#zGetOperationStatusZGetoperationstatusGet) | **GET** /z_getoperationstatus | Get the status of asynchronous operations |
| [**zGetTotalBalanceZGettotalbalanceGet**](MainApi.md#zGetTotalBalanceZGettotalbalanceGet) | **GET** /z_gettotalbalance | Get the total balance of both transparent and private funds |
| [**zGetoperationresultZGetoperationresultGet**](MainApi.md#zGetoperationresultZGetoperationresultGet) | **GET** /z_getoperationresult | Retrieve the result and status of Zcash operations |
| [**zImportKeyZImportkeyGet**](MainApi.md#zImportKeyZImportkeyGet) | **GET** /z_importkey | Import a Z key into the wallet |
| [**zImportViewingKeyZImportviewingkeyPost**](MainApi.md#zImportViewingKeyZImportviewingkeyPost) | **POST** /z_importviewingkey | Import a viewing key into the wallet |
| [**zImportWalletZImportwalletPost**](MainApi.md#zImportWalletZImportwalletPost) | **POST** /z_importwallet | Import keys from a wallet export file |
| [**zListOperationIdsZListoperationidsGet**](MainApi.md#zListOperationIdsZListoperationidsGet) | **GET** /z_listoperationids | List Operation IDs |
| [**zListReceivedByAddressZListreceivedbyaddressGet**](MainApi.md#zListReceivedByAddressZListreceivedbyaddressGet) | **GET** /z_listreceivedbyaddress | List amounts received by a z-address |
| [**zListunspentZListunspentGet**](MainApi.md#zListunspentZListunspentGet) | **GET** /z_listunspent | List unspent shielded notes |
| [**zMergetoaddressZMergetoaddressPost**](MainApi.md#zMergetoaddressZMergetoaddressPost) | **POST** /z_mergetoaddress | Merge multiple UTXOs and notes into a single UTXO or note |
| [**zSendManyZSendmanyPost**](MainApi.md#zSendManyZSendmanyPost) | **POST** /z_sendmany | Send multiple times to multiple recipients |
| [**zShieldcoinbaseZShieldcoinbasePost**](MainApi.md#zShieldcoinbaseZShieldcoinbasePost) | **POST** /z_shieldcoinbase | Shield transparent coinbase funds to a shielded zaddr |
| [**zValidateAddressZValidateaddressGet**](MainApi.md#zValidateAddressZValidateaddressGet) | **GET** /z_validateaddress | Validate a Z address |
| [**zViewTransactionZViewtransactionTxidGet**](MainApi.md#zViewTransactionZViewtransactionTxidGet) | **GET** /z_viewtransaction/{txid} | Get detailed shielded information about in-wallet transaction |
| [**zcBenchmarkZcbenchmarkPost**](MainApi.md#zcBenchmarkZcbenchmarkPost) | **POST** /zcbenchmark | Runs a benchmark of the selected type |


<a name="addMultisigAddressAddmultisigaddressPost"></a>
# **addMultisigAddressAddmultisigaddressPost**
> AddMultisigAddressResponse addMultisigAddressAddmultisigaddressPost(AddMultisigAddressRequest)

Add a multisignature address

    Add a nrequired-to-sign multisignature address to the wallet.                              Each key is a Pastel address or hex-encoded public key.  ### Description - This endpoint adds a multisignature address to the wallet which requires a specified number of signatures to authorize a transaction. - Each key in the &#x60;keysobject&#x60; list can be either a Pastel address or a hex-encoded public key.  ### Input Parameters - &#x60;nrequired&#x60; (int): The number of required signatures out of the n keys or addresses. - &#x60;keysobject&#x60; (List[str]): A list of Pastel addresses or hex-encoded public keys. - &#x60;account&#x60; (str, optional): DEPRECATED. Must be set to an empty string \&quot;\&quot; for the default account. Any other string will result in an error.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;nrequired\&quot;: 2,     \&quot;keysobject\&quot;: [\&quot;PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n\&quot;, \&quot;PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n\&quot;],     \&quot;account\&quot;: \&quot;\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object with the newly created Pastel address.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;zcashaddress\&quot;: \&quot;pZc4pUvczxNG1Sfh5Zx3n2fuFjGjTDbB4qu\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **AddMultisigAddressRequest** | [**AddMultisigAddressRequest**](../Models/AddMultisigAddressRequest.md)|  | |

### Return type

[**AddMultisigAddressResponse**](../Models/AddMultisigAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="addNodeAddnodePost"></a>
# **addNodeAddnodePost**
> AddNodeResponse addNodeAddnodePost(AddNodeRequest)

Add, remove, or try a connection to a node

    Attempt to add or remove a node from the addnode list, or try a connection to a node once.  ### Description - This endpoint manages nodes in the addnode list. It can add a node to the list, remove a node from the list, or try a connection to a node once. - The &#39;node&#39; parameter specifies the node (IP address and port), and the &#39;command&#39; parameter specifies the action to be taken (&#39;add&#39;, &#39;remove&#39;, or &#39;onetry&#39;).  ### Input Parameters - &#x60;node&#x60; (string, required): The node&#39;s address in the format &#x60;IP:port&#x60;. - &#x60;command&#x60; (string, required): The command to execute, which can be &#39;add&#39;, &#39;remove&#39;, or &#39;onetry&#39;.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;node\&quot;: \&quot;192.168.0.6:9933\&quot;,     \&quot;command\&quot;: \&quot;onetry\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a success message or null if the command is executed successfully.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;result\&quot;: \&quot;Node added successfully\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Use this method cautiously as it can modify the node&#39;s peer connections.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **AddNodeRequest** | [**AddNodeRequest**](../Models/AddNodeRequest.md)|  | |

### Return type

[**AddNodeResponse**](../Models/AddNodeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="backupWalletBackupwalletPost"></a>
# **backupWalletBackupwalletPost**
> BackupWalletResponse backupWalletBackupwalletPost(BackupWalletRequest)

Backup the wallet to a destination

    Backup the wallet.dat file to a specified destination filename.  ### Description - Safely copies the wallet.dat file to the specified destination. The destination is a filename and should be saved in the directory set by the &#x60;-exportdir&#x60; option.  ### Input Parameters - &#x60;destination&#x60;: (string, required) The destination filename.  ### Example Request - &#x60;POST /backupwallet&#x60; with JSON body &#x60;{\&quot;destination\&quot;: \&quot;backupdata\&quot;}&#x60;  ### Response - Returns a JSON object containing the full path of the destination file where the wallet was backed up.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;path\&quot;: \&quot;/path/to/backup/backupdata\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the destination filename is invalid or not provided. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request, such as if the &#x60;-exportdir&#x60; option is not set or the wallet backup fails.  ### Note - It&#39;s crucial to regularly backup your wallet to prevent loss of funds in case of system failures.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **BackupWalletRequest** | [**BackupWalletRequest**](../Models/BackupWalletRequest.md)|  | |

### Return type

[**BackupWalletResponse**](../Models/BackupWalletResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="changeWalletPassphraseWalletpassphrasechangePost"></a>
# **changeWalletPassphraseWalletpassphrasechangePost**
> WalletPassphraseChangeResponse changeWalletPassphraseWalletpassphrasechangePost(WalletPassphraseChangeRequest)

Change the wallet passphrase

    Change the wallet passphrase from &#39;oldpassphrase&#39; to &#39;newpassphrase&#39;.  ### Description - This endpoint allows for the change of the existing wallet passphrase to a new passphrase. It&#39;s essential for maintaining wallet security and should be used with caution.  ### Input Parameters - &#x60;oldpassphrase&#x60;: The current passphrase of the wallet. - &#x60;newpassphrase&#x60;: The new passphrase that will replace the current passphrase.  ### Example Request &#x60;&#x60;&#x60;json POST /walletpassphrasechange {     \&quot;oldpassphrase\&quot;: \&quot;oldpassword123\&quot;,     \&quot;newpassphrase\&quot;: \&quot;newpassword456\&quot; } &#x60;&#x60;&#x60;  ### Response - On successful change, the response is a confirmation message.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;result\&quot;: \&quot;Passphrase changed successfully\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are incorrect or missing. - HTTP 500: Internal Server Error if there&#39;s an issue processing the request or if the old passphrase is incorrect.  ### Note - The wallet needs to be encrypted for this operation to succeed. If the wallet is unencrypted, this method will return an error.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **WalletPassphraseChangeRequest** | [**WalletPassphraseChangeRequest**](../Models/WalletPassphraseChangeRequest.md)|  | |

### Return type

[**WalletPassphraseChangeResponse**](../Models/WalletPassphraseChangeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="createMultisigCreatemultisigPost"></a>
# **createMultisigCreatemultisigPost**
> CreateMultisigResponse createMultisigCreatemultisigPost(CreateMultisigRequest)

Create a multisig address

    Creates a multi-signature address with n signatures of m keys required.  ### Description - This endpoint creates a multi-signature address requiring a specified number of signatures from a set of provided keys. - It returns the new multisig address and the hex-encoded redemption script.  ### Input Parameters - &#x60;nrequired&#x60;: The number of required signatures out of the n keys or addresses. - &#x60;keys&#x60;: A list of Pastel addresses or hex-encoded public keys.  ### Example Request - &#x60;POST /createmultisig&#x60; &#x60;&#x60;&#x60;json {     \&quot;nrequired\&quot;: 2,     \&quot;keys\&quot;: [\&quot;Ptor9ydHJuGpNWFAX3ZTu3bXevEhCaDVrsY\&quot;, \&quot;Ptor9ydHJuGpNWFAX3ZTu3bXevEhCaDVrsY\&quot;] } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the multisig address and the hex-encoded redemption script.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;address\&quot;: \&quot;multisigaddress\&quot;,     \&quot;redeemScript\&quot;: \&quot;script\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **CreateMultisigRequest** | [**CreateMultisigRequest**](../Models/CreateMultisigRequest.md)|  | |

### Return type

[**CreateMultisigResponse**](../Models/CreateMultisigResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="createRawTransactionCreaterawtransactionPost"></a>
# **createRawTransactionCreaterawtransactionPost**
> CreateRawTransactionResponse createRawTransactionCreaterawtransactionPost(CreateRawTransactionRequest)

Create a raw transaction

    Create a transaction spending the given inputs and sending to the given addresses.  ### Description - This endpoint creates a hex-encoded raw transaction that spends the given inputs and sends to the specified addresses. - The transaction&#39;s inputs are not signed, and it is not stored in the wallet or transmitted to the network.  ### Input Parameters - &#x60;transactions&#x60;: A list of transaction inputs, each containing:     - &#x60;txid&#x60;: The transaction id.     - &#x60;vout&#x60;: The output number.     - &#x60;sequence&#x60;: (Optional) The sequence number. - &#x60;addresses&#x60;: A dictionary with addresses as keys and amounts as values. - &#x60;locktime&#x60;: (Optional) Raw locktime. Non-0 value also activates inputs. - &#x60;expiryheight&#x60;: (Optional) Expiry height of transaction (if Overwinter is active).  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;transactions\&quot;: [{\&quot;txid\&quot;: \&quot;myid\&quot;, \&quot;vout\&quot;: 0}],     \&quot;addresses\&quot;: {\&quot;address\&quot;: 0.01},     \&quot;locktime\&quot;: 0,     \&quot;expiryheight\&quot;: 1000 } &#x60;&#x60;&#x60;  ### Response - Returns a hex string of the transaction.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;transaction\&quot;: \&quot;hex-encoded-transaction\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **CreateRawTransactionRequest** | [**CreateRawTransactionRequest**](../Models/CreateRawTransactionRequest.md)|  | |

### Return type

[**CreateRawTransactionResponse**](../Models/CreateRawTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="decodeRawTransactionDecoderawtransactionPost"></a>
# **decodeRawTransactionDecoderawtransactionPost**
> DecodeRawTransactionResponse decodeRawTransactionDecoderawtransactionPost(DecodeRawTransactionRequest)

Decode a raw transaction

    Decode a serialized, hex-encoded transaction and return a JSON object representing it.  ### Description - This endpoint decodes a raw, serialized, hex-encoded transaction and provides detailed information about it.  ### Input Parameters - &#x60;hexstring&#x60; (string, required): The hex-encoded transaction string to decode.  ### Example Request - &#x60;POST /decoderawtransaction&#x60; with body &#x60;{\&quot;hexstring\&quot;: \&quot;hex-encoded-string\&quot;}&#x60;  ### Response - Returns a JSON object containing detailed information about the transaction, including &#x60;txid&#x60;, &#x60;size&#x60;, &#x60;overwintered&#x60; flag, &#x60;version&#x60;, &#x60;locktime&#x60;, &#x60;vin&#x60;, and &#x60;vout&#x60; fields.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;txid\&quot;: \&quot;id\&quot;,     \&quot;size\&quot;: n,     \&quot;overwintered\&quot;: true,     \&quot;version\&quot;: n,     \&quot;versiongroupid\&quot;: \&quot;hex\&quot;,     \&quot;locktime\&quot;: ttt,     \&quot;expiryheight\&quot;: n,     \&quot;vin\&quot;: [         {             \&quot;txid\&quot;: \&quot;id\&quot;,             \&quot;vout\&quot;: n,             \&quot;scriptSig\&quot;: {                 \&quot;asm\&quot;: \&quot;asm\&quot;,                 \&quot;hex\&quot;: \&quot;hex\&quot;             },             \&quot;sequence\&quot;: n         }     ],     \&quot;vout\&quot;: [         {             \&quot;value\&quot;: x.xxx,             \&quot;n\&quot;: n,             \&quot;scriptPubKey\&quot;: {                 \&quot;asm\&quot;: \&quot;asm\&quot;,                 \&quot;hex\&quot;: \&quot;hex\&quot;,                 \&quot;reqSigs\&quot;: n,                 \&quot;type\&quot;: \&quot;pubkeyhash\&quot;,                 \&quot;addresses\&quot;: [                     \&quot;Ptor9ydHJuGpNWFAX3ZTu3bXevEhCaDVrsY\&quot;                 ]             }         }     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the &#x60;hexstring&#x60; parameter is invalid or missing. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for debugging transactions and understanding their structure.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **DecodeRawTransactionRequest** | [**DecodeRawTransactionRequest**](../Models/DecodeRawTransactionRequest.md)|  | |

### Return type

[**DecodeRawTransactionResponse**](../Models/DecodeRawTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="decodeScriptDecodescriptPost"></a>
# **decodeScriptDecodescriptPost**
> DecodeScriptResponse decodeScriptDecodescriptPost(DecodeScriptRequest)

Decode a hex-encoded script

    Decode a hex-encoded script.  ### Description - This endpoint decodes a hex-encoded script and returns detailed information about it.  ### Input Parameters - &#x60;hex&#x60;: A string representing the hex-encoded script.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;hex\&quot;: \&quot;hexstring\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing details about the script, such as its assembly representation, type, required signatures, associated addresses, and P2SH.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;asm\&quot;: \&quot;asm\&quot;,     \&quot;hex\&quot;: \&quot;hex\&quot;,     \&quot;type\&quot;: \&quot;type\&quot;,     \&quot;reqSigs\&quot;: 1,     \&quot;addresses\&quot;: [\&quot;address1\&quot;, \&quot;address2\&quot;],     \&quot;p2sh\&quot;: \&quot;address\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the hex parameter is invalid or missing. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **DecodeScriptRequest** | [**DecodeScriptRequest**](../Models/DecodeScriptRequest.md)|  | |

### Return type

[**DecodeScriptResponse**](../Models/DecodeScriptResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="disconnectNodeDisconnectnodePost"></a>
# **disconnectNodeDisconnectnodePost**
> DisconnectNodeResponse disconnectNodeDisconnectnodePost(DisconnectNodeRequest)

Disconnect from a specified node

    Disconnect immediately from a specified node in the Pastel network.  ### Description - This endpoint allows for immediate disconnection from a specified node. It&#39;s useful for network management and control.  ### Input Parameters - &#x60;node&#x60;: The IP address and port of the node to disconnect from, in the format \&quot;IP:PORT\&quot;.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;node\&quot;: \&quot;192.168.0.6:9933\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object indicating the status of the disconnection.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;status\&quot;: \&quot;Node disconnected successfully\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Use this endpoint with caution as it modifies the network connections of the Pastel node.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **DisconnectNodeRequest** | [**DisconnectNodeRequest**](../Models/DisconnectNodeRequest.md)|  | |

### Return type

[**DisconnectNodeResponse**](../Models/DisconnectNodeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="dumpPrivKeyDumpprivkeyGet"></a>
# **dumpPrivKeyDumpprivkeyGet**
> DumpPrivKeyResponse dumpPrivKeyDumpprivkeyGet(DumpPrivKeyRequest)

Reveal the private key for a given address

    Reveals the private key corresponding to the specified transparent address.  ### Description - This endpoint is used to retrieve the private key associated with a given transparent address.  - It&#39;s important to handle the output with care as the private key controls access to the assets held in the address.  ### Input Parameters - &#x60;t_addr&#x60;: The transparent address for which the private key is to be revealed.  ### Example Request - &#x60;GET /dumpprivkey?t_addr&#x3D;myaddress&#x60;  ### Response - Returns a JSON object containing the private key in a string format.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;key\&quot;: \&quot;5J1m2B2K5m3...\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the address is invalid or not specified. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The output should be kept secure as it provides complete control over the assets in the address.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **DumpPrivKeyRequest** | [**DumpPrivKeyRequest**](../Models/DumpPrivKeyRequest.md)|  | |

### Return type

[**DumpPrivKeyResponse**](../Models/DumpPrivKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="dumpWalletDumpwalletPost"></a>
# **dumpWalletDumpwalletPost**
> DumpWalletResponse dumpWalletDumpwalletPost(filename)

Dump wallet keys

    Dumps taddr wallet keys in a human-readable format.  ### Description - Dumps transparent address (taddr) wallet keys to a specified file. Overwriting an existing file is not permitted.  ### Input Parameters - &#x60;filename&#x60;: A string representing the filename to which the wallet keys will be dumped. The file will be saved in the folder set by the &#x60;pasteld -exportdir&#x60; option.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;filename\&quot;: \&quot;my_wallet_dump\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the full path of the destination file where the wallet keys are dumped.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;path\&quot;: \&quot;/path/to/dumped/file/my_wallet_dump\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request. - HTTP 400: Bad Request if the filename parameter is not provided or if the file already exists.  ### Note - Use this endpoint for transparent address wallet key backups.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **filename** | **String**|  | [default to null] |

### Return type

[**DumpWalletResponse**](../Models/DumpWalletResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="encryptWalletEncryptwalletPost"></a>
# **encryptWalletEncryptwalletPost**
> EncryptWalletResponse encryptWalletEncryptwalletPost(passphrase)

Encrypt the wallet with a passphrase

    Encrypt the wallet with a given passphrase.                             ### Description              - This endpoint encrypts the wallet with the provided passphrase. It&#39;s used for the first time encryption of the wallet. After encryption, any operations that interact with private keys (like sending or signing) will require the passphrase.              - If the wallet is already encrypted, this operation will fail, and you should use the &#x60;walletpassphrasechange&#x60; call instead.              - Note that encrypting the wallet will shutdown the server.               ### Input Parameters              - &#x60;passphrase&#x60;: A string representing the passphrase to encrypt the wallet with. It must be at least 1 character long, but a longer passphrase is recommended for security.               ### Example Request              &#x60;&#x60;&#x60;json              {                  \&quot;passphrase\&quot;: \&quot;my secure passphrase\&quot;              }              &#x60;&#x60;&#x60;               ### Response              - Returns a message indicating the encryption status and server shutdown.               ### Example Response              &#x60;&#x60;&#x60;json              {                  \&quot;message\&quot;: \&quot;wallet encrypted; Pastel server stopping, restart to run with encrypted wallet. The keypool has been flushed, you need to make a new backup.\&quot;              }              &#x60;&#x60;&#x60;               ### Possible Errors              - HTTP 400: Bad Request if wallet encryption is disabled or the wallet is already encrypted.              - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.               ### Note              - This is a critical operation that changes the state of the wallet and requires server restart.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **passphrase** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |

### Return type

[**EncryptWalletResponse**](../Models/EncryptWalletResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="estimateFeeEstimatefeeGet"></a>
# **estimateFeeEstimatefeeGet**
> EstimateFeeResponse estimateFeeEstimatefeeGet(nblocks)

Estimate the transaction fee per kilobyte

    Estimate the approximate fee per kilobyte needed for a transaction to begin confirmation within a specified number of blocks.   ### Description - This endpoint provides an estimate of the fee per kilobyte for a transaction to be confirmed within a specified number of blocks.  ### Input Parameters - &#x60;nblocks&#x60;: The number of blocks within which the transaction should begin confirmation.  ### Example Request - &#x60;GET /estimatefee?nblocks&#x3D;6&#x60;  ### Response - Returns a JSON object containing the estimated fee per kilobyte.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;estimated_fee_per_kb\&quot;: 0.0001 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - A return value of -1.0 indicates insufficient data to make an estimate.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **nblocks** | **Integer**|  | [default to null] |

### Return type

[**EstimateFeeResponse**](../Models/EstimateFeeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="estimateNftStorageFeeTicketsToolsEstimatenftstoragefeeGet"></a>
# **estimateNftStorageFeeTicketsToolsEstimatenftstoragefeeGet**
> EstimateNftStorageFeeResponse estimateNftStorageFeeTicketsToolsEstimatenftstoragefeeGet(image\_size\_in\_mb)

Estimate storage fee for NFT registration

    Estimate the storage fee for NFT registration based on the image size.   ### Description - This endpoint estimates the storage fee in PSL for NFT registration for a given image size.  ### Input Parameters - &#x60;image_size_in_mb&#x60;: The estimated size of the image in megabytes (MB).  ### Example Request - &#x60;GET /tickets/tools/estimatenftstoragefee?image_size_in_mb&#x3D;3&#x60;  ### Response - Returns a JSON object containing the estimated minimum, average, and maximum storage fees for the NFT.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;estimated_nft_storage_fee_min\&quot;: 100,     \&quot;estimated_nft_storage_fee_average\&quot;: 150,     \&quot;estimated_nft_storage_fee_max\&quot;: 200 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the image size is not provided or invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for users and applications to estimate the cost of NFT registration.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **image\_size\_in\_mb** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |

### Return type

[**EstimateNftStorageFeeResponse**](../Models/EstimateNftStorageFeeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="estimatePriorityEstimatepriorityGet"></a>
# **estimatePriorityEstimatepriorityGet**
> BigDecimal estimatePriorityEstimatepriorityGet(nblocks)

Estimate the transaction priority for zero-fee confirmation

    Estimate the approximate priority a zero-fee transaction needs to begin confirmation within a specified number of blocks.  ### Description - This endpoint estimates the priority that a zero-fee transaction needs to start confirming within a certain number of blocks. - It&#39;s useful for determining the priority required for a transaction to be included in a block without incurring fees.  ### Input Parameters - &#x60;nblocks&#x60;: The number of blocks within which the transaction should begin confirmation.  ### Example Request - &#x60;GET /estimatepriority?nblocks&#x3D;6&#x60;  ### Response - Returns a numeric value representing the estimated priority.  ### Example Response &#x60;&#x60;&#x60;json 3.4567 &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the &#x60;nblocks&#x60; parameter is not a valid number. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Returns &#x60;-1.0&#x60; if not enough transactions and blocks have been observed to make an estimate.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **nblocks** | **Integer**|  | [default to null] |

### Return type

**BigDecimal**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="executeMasternodeCommandMasternodeCommandPost"></a>
# **executeMasternodeCommandMasternodeCommandPost**
> Response_Execute_Masternode_Command_Masternode_Command_Post executeMasternodeCommandMasternodeCommandPost(MasternodeCommandRequest)

Execute masternode related actions

    Execute various masternode related actions based on the provided command.  ### Description - This endpoint allows for executing different masternode related commands such as count, current, winner, genkey, and others.  ### Input Parameters - &#x60;command&#x60;: The masternode command to execute. - &#x60;additional_args&#x60;: Additional arguments required for specific commands.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;command\&quot;: \&quot;count\&quot;,     \&quot;additional_args\&quot;: {\&quot;count_type\&quot;: \&quot;enabled\&quot;} } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the result based on the executed command.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;count\&quot;: 150 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the command or additional arguments are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **MasternodeCommandRequest** | [**MasternodeCommandRequest**](../Models/MasternodeCommandRequest.md)|  | |

### Return type

[**Response_Execute_Masternode_Command_Masternode_Command_Post**](../Models/Response_Execute_Masternode_Command_Masternode_Command_Post.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="fixMissingTransactionsFixmissingtxsStartingHeightGet"></a>
# **fixMissingTransactionsFixmissingtxsStartingHeightGet**
> FixMissingTransactionsResponse fixMissingTransactionsFixmissingtxsStartingHeightGet(starting\_height)

Fix Missing Transactions

    Scan for missing transactions in the wallet starting from the given height and add to the wallet all missing transactions found in the blockchain.  ### Description - Scans the blockchain starting from the specified block height for any transactions that are missing in the wallet and adds them.  ### Input Parameters - &#x60;starting_height&#x60;: (integer, required) The block height from which the scan for missing transactions should begin.  ### Example Request - &#x60;GET /fixmissingtxs/100000&#x60;  ### Response - Returns a JSON array of transaction IDs for transactions that were missing in the wallet and have been added.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;missing_transactions\&quot;: [\&quot;missing_transaction1_txid\&quot;, \&quot;missing_transaction2_txid\&quot;, ...] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the starting height is invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is useful for wallet recovery and synchronization purposes.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **starting\_height** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |

### Return type

[**FixMissingTransactionsResponse**](../Models/FixMissingTransactionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="fundRawTransactionFundrawtransactionPost"></a>
# **fundRawTransactionFundrawtransactionPost**
> FundRawTransactionResponse fundRawTransactionFundrawtransactionPost(FundRawTransactionRequest)

Add inputs to a transaction

    Add inputs to a transaction until it has enough in value to meet its out value.  ### Description - This endpoint adds inputs to a raw transaction represented by a hex string. It ensures the transaction has enough value to meet its output value. - It will not modify existing inputs and will add one change output to the outputs. - Note that inputs which were signed may need to be re-signed after completion since inputs/outputs have been added. - The inputs added by this method will not be signed; use &#x60;signrawtransaction&#x60; for that.  ### Input Parameters - &#x60;hexstring&#x60;: A string representing the raw transaction in hexadecimal format.  ### Example Request - &#x60;POST /fundrawtransaction&#x60; with JSON body &#x60;{\&quot;hexstring\&quot;: \&quot;rawtransactionhex\&quot;}&#x60;  ### Response - Returns a JSON object containing the resulting raw transaction, the fee added, and the position of the added change output.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;hex\&quot;: \&quot;fundedtransactionhex\&quot;,     \&quot;fee\&quot;: 0.0012,     \&quot;changepos\&quot;: 1 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the &#x60;hexstring&#x60; parameter is invalid or missing. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This method is part of the transaction creation process, typically followed by &#x60;signrawtransaction&#x60; and &#x60;sendrawtransaction&#x60;.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **FundRawTransactionRequest** | [**FundRawTransactionRequest**](../Models/FundRawTransactionRequest.md)|  | |

### Return type

[**FundRawTransactionResponse**](../Models/FundRawTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="generateBlocksGeneratePost"></a>
# **generateBlocksGeneratePost**
> GenerateBlocksResponse generateBlocksGeneratePost(GenerateBlocksRequest)

Mine blocks immediately

    Mine a specified number of blocks immediately on the regtest network.  ### Description - This endpoint mines a given number of blocks instantly and returns their hashes. Only available on the regtest network.  ### Input Parameters - &#x60;num_blocks&#x60;: The number of blocks to generate immediately. - &#x60;pastel_id&#x60;: (Optional) The Pastel ID eligible to mine the block.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;num_blocks\&quot;: 11,     \&quot;pastel_id\&quot;: \&quot;pastelid_example\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns an array of hashes of the blocks generated.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;block_hashes\&quot;: [         \&quot;00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e\&quot;,         ...     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request. - HTTP 403: Forbidden if the method is used outside the regtest network.  ### Note - This method is primarily used for testing and development purposes on the regtest network.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **GenerateBlocksRequest** | [**GenerateBlocksRequest**](../Models/GenerateBlocksRequest.md)|  | |

### Return type

[**GenerateBlocksResponse**](../Models/GenerateBlocksResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="generatePastelIdNewkeyPastelidNewkeyPost"></a>
# **generatePastelIdNewkeyPastelidNewkeyPost**
> PastelIDNewKeyResponse generatePastelIdNewkeyPastelidNewkeyPost(PastelIDNewKeyRequest)

Generate new Pastel ID and keys

    Generate a new Pastel ID and associated keys (EdDSA448 and LegRoast signing keys).  ### Description - This endpoint generates a new Pastel ID and associated keys using the specified passphrase for encryption.  ### Input Parameters - &#x60;passphrase&#x60;: A string passphrase used to encrypt the key file.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;passphrase\&quot;: \&quot;your_secure_passphrase\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the Pastel ID and public key in base58-encoded format.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;pastel_id\&quot;: \&quot;paxxxxxxxxxxxxxxxxxxxxxx\&quot;,     \&quot;public_key\&quot;: \&quot;pubxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **PastelIDNewKeyRequest** | [**PastelIDNewKeyRequest**](../Models/PastelIDNewKeyRequest.md)|  | |

### Return type

[**PastelIDNewKeyResponse**](../Models/PastelIDNewKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="generateReportGenerateReportReportNameGet"></a>
# **generateReportGenerateReportReportNameGet**
> GenerateReportResponse generateReportGenerateReportReportNameGet(report\_name)

Generate various reports

    Generate various reports from the Pastel Network.   ### Description - This endpoint generates different types of reports based on the Pastel Network&#39;s blockchain data.  ### Input Parameters - &#x60;report_name&#x60;: The name of the report to generate. Currently supported: &#39;fees-and-burn&#39;.  ### Example Request - &#x60;GET /generate-report/fees-and-burn&#x60;  ### Response - Returns a JSON object containing the generated report data.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;report_data\&quot;: {         // Example report data here     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the report name is not supported. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for analysis and insight into various aspects of the Pastel Network.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **report\_name** | **String**|  | [default to null] |

### Return type

[**GenerateReportResponse**](../Models/GenerateReportResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getAccountAddressGetaccountaddressGet"></a>
# **getAccountAddressGetaccountaddressGet**
> GetAccountAddressResponse getAccountAddressGetaccountaddressGet(account)

Get the current Pastel address for receiving payments

    Get the current Pastel address for receiving payments to a specified account.  ### Description - This endpoint returns the current Pastel address for receiving payments to the specified account.  - Note: This method is deprecated.  ### Input Parameters - &#x60;account&#x60;: (string, required) MUST be set to the empty string \&quot;\&quot; to represent the default account. Passing any other string will result in an error.  ### Example Request - &#x60;GET /getaccountaddress?account&#x3D;\&quot;\&quot;&#x60;  ### Response - Returns a JSON object containing the Pastel address for the account.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;zcashaddress\&quot;: \&quot;t1KSLVSVdZD1Cz8TCr7FBG8m5xKwKMBrMT6\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if an invalid account name is provided. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is deprecated and may be removed in future versions.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **account** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |

### Return type

[**GetAccountAddressResponse**](../Models/GetAccountAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getAccountGetaccountZcashaddressGet"></a>
# **getAccountGetaccountZcashaddressGet**
> GetAccountResponse getAccountGetaccountZcashaddressGet(zcashaddress)

Get the account associated with a Pastel address

    Retrieve the account name associated with the given Pastel address.   ### Description - This endpoint is used to get the account name linked to a specific Pastel address. It is important to note that this method is marked as deprecated.  ### Input Parameters - &#x60;zcashaddress&#x60;: A string representing the Pastel address for the account lookup.  ### Example Request - &#x60;GET /getaccount/PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n&#x60;  ### Response - Returns a JSON object containing the account name associated with the given Pastel address.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;account_name\&quot;: \&quot;exampleAccountName\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the address is invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This method is deprecated and might be removed in future versions of the Pastel network.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **zcashaddress** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |

### Return type

[**GetAccountResponse**](../Models/GetAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getActionFeesStoragefeeGetactionfeesGet"></a>
# **getActionFeesStoragefeeGetactionfeesGet**
> GetActionFeesResponse getActionFeesStoragefeeGetactionfeesGet(data\_size, height)

Get action fees based on data size

    Get action fees based on data size.  ### Description - This endpoint calculates the action fees based on the given data size in MB.  ### Input Parameters - &#x60;data_size&#x60;: (Required) Data size in MB. - &#x60;height&#x60;: (Optional) Block height to get action fees for.  ### Example Request - &#x60;GET /storagefee/getactionfees?data_size&#x3D;10&amp;height&#x3D;12345&#x60;  ### Response - Returns a JSON object containing action fees for different actions based on the data size.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;datasize\&quot;: 10,     \&quot;height\&quot;: 12345,     \&quot;fee_deflator_factor\&quot;: 1.5,     \&quot;action_fees\&quot;: {         \&quot;actionTypeFee\&quot;: 200,         \&quot;actionTypeFeePat\&quot;: 200000,         ...     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **data\_size** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **height** | [**Height**](../Models/.md)|  | [optional] [default to null] |

### Return type

[**GetActionFeesResponse**](../Models/GetActionFeesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getAddedNodeInfoGetaddednodeinfoGet"></a>
# **getAddedNodeInfoGetaddednodeinfoGet**
> GetAddedNodeInfoResponse getAddedNodeInfoGetaddednodeinfoGet(dns, node)

Get information about added nodes

    Get information about the given added node or all added nodes.  ### Description - This endpoint returns information about nodes that have been added using the &#x60;addnode&#x60; RPC command.  - It can return information about all added nodes or a specific node, if specified.  ### Input Parameters - &#x60;dns&#x60;: A boolean value indicating whether detailed information is required. - &#x60;node&#x60;: (Optional) The specific node to get information about.  ### Example Request - &#x60;GET /getaddednodeinfo?dns&#x3D;true&amp;node&#x3D;192.168.0.201&#x60;  ### Response - Returns a JSON object containing information about added nodes.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;nodes\&quot;: [         {             \&quot;addednode\&quot;: \&quot;192.168.0.201\&quot;,             \&quot;connected\&quot;: true,             \&quot;addresses\&quot;: [                 {                     \&quot;address\&quot;: \&quot;192.168.0.201:9933\&quot;,                     \&quot;connected\&quot;: \&quot;outbound\&quot;                 }             ]         }     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **dns** | **Boolean**|  | [default to null] |
| **node** | **String**|  | [optional] [default to null] |

### Return type

[**GetAddedNodeInfoResponse**](../Models/GetAddedNodeInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getAddressMempoolGetaddressmempoolGet"></a>
# **getAddressMempoolGetaddressmempoolGet**
> GetAddressMempoolResponse getAddressMempoolGetaddressmempoolGet(request\_body)

Get all mempool deltas for an address

    Retrieve all mempool deltas for a specified address.  ### Description - This endpoint returns all mempool deltas (transaction differences) for a given address. - It&#39;s useful for tracking the unconfirmed transactions involving a specific address.  ### Input Parameters - &#x60;addresses&#x60;: A list of base58check encoded addresses.  ### Example Request - &#x60;GET /getaddressmempool?addresses&#x3D;[\&quot;tPp3pfmLi57S8qoccfWnn2o4tXyoQ23wVSp\&quot;]&#x60;  ### Response - Returns a JSON array of objects, each representing a mempool delta for the given address(es).  ### Example Response &#x60;&#x60;&#x60;json [     {         \&quot;address\&quot;: \&quot;tPp3pfmLi57S8qoccfWnn2o4tXyoQ23wVSp\&quot;,         \&quot;txid\&quot;: \&quot;txid123\&quot;,         \&quot;index\&quot;: 1,         \&quot;patoshis\&quot;: 5000000,         \&quot;timestamp\&quot;: 1617184000,         \&quot;prevtxid\&quot;: \&quot;txid456\&quot;,         \&quot;prevout\&quot;: 0     } ] &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **request\_body** | [**List**](../Models/string.md)|  | |

### Return type

[**GetAddressMempoolResponse**](../Models/GetAddressMempoolResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="getAddressesByAccountGetaddressesbyaccountGet"></a>
# **getAddressesByAccountGetaddressesbyaccountGet**
> oas_any_type_not_mapped getAddressesByAccountGetaddressesbyaccountGet(account)

Get addresses by account

    Get the list of addresses for the given account.  ### Description - **DEPRECATED**: This endpoint is deprecated and might be removed in future versions. It returns the list of addresses associated with a specified account. - The account argument must be set to the empty string &#x60;\&quot;\&quot;&#x60; to represent the default account. Passing any other string will result in an error.  ### Input Parameters - &#x60;account&#x60;: (string, required) The account name. Must be set to &#x60;\&quot;\&quot;&#x60; for the default account.  ### Example Request - &#x60;GET /getaddressesbyaccount?account&#x3D;\&quot;\&quot;&#x60;  ### Response - Returns a JSON array of strings, each representing a Pastel address associated with the given account.  ### Example Response &#x60;&#x60;&#x60;json [   \&quot;paxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\&quot;,   \&quot;payyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\&quot; ] &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the account parameter is not the empty string. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This method is primarily used for wallet management and account balance tracking.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **account** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |

### Return type

[**oas_any_type_not_mapped**](../Models/AnyType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getBalanceGetbalanceGet"></a>
# **getBalanceGetbalanceGet**
> GetBalanceResponse getBalanceGetbalanceGet(account, minconf, includeWatchonly)

Get the server&#39;s total available balance

    Get the server&#39;s total available balance.  ### Description - This endpoint returns the total available balance in the server&#39;s wallet. It can be filtered by a minimum number of confirmations and can include balances in watch-only addresses.  ### Input Parameters - &#x60;account&#x60;: (Optional) DEPRECATED. Must be an empty string \&quot;\&quot; or \&quot;*\&quot;, either of which will give the total available balance. Any other string will result in an error. - &#x60;minconf&#x60;: (Optional) Only include transactions confirmed at least this many times. Default is 1. - &#x60;includeWatchonly&#x60;: (Optional) Also include balance in watchonly addresses. Default is false.  ### Example Request - &#x60;GET /getbalance?account&#x3D;*&amp;minconf&#x3D;1&amp;includeWatchonly&#x3D;false&#x60;  ### Response - Returns a JSON object containing the available balance amount.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;balance\&quot;: 1000.00 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The account argument is deprecated and should be set to \&quot;\&quot; or \&quot;*\&quot;.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **account** | [**Account_1**](../Models/.md)|  | [optional] [default to null] |
| **minconf** | [**Minconf_1**](../Models/.md)|  | [optional] [default to 1] |
| **includeWatchonly** | [**Includewatchonly**](../Models/.md)|  | [optional] [default to false] |

### Return type

[**GetBalanceResponse**](../Models/GetBalanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getBestBlockHashGetbestblockhashGet"></a>
# **getBestBlockHashGetbestblockhashGet**
> GetBestBlockHashResponse getBestBlockHashGetbestblockhashGet()

Get the hash of the best block

    Get the hash of the best (tip) block in the longest blockchain.   ### Description - This endpoint returns the hash of the latest block added to the Pastel blockchain, representing the most current and up-to-date state of the network.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getbestblockhash&#x60;  ### Response - Returns a JSON object containing the hash of the best block in hexadecimal format.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;block_hash\&quot;: \&quot;00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Primarily used by blockchain explorers and wallets to identify the current end of the blockchain.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetBestBlockHashResponse**](../Models/GetBestBlockHashResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getBlockCountGetblockcountGet"></a>
# **getBlockCountGetblockcountGet**
> GetBlockCountResponse getBlockCountGetblockcountGet()

Get the current block count

    Get the number of blocks in the best valid block chain.  ### Description - This endpoint returns the current block count in the blockchain, which is the number of blocks in the longest valid blockchain. - It reflects the height of the blockchain and is useful for tracking the growth of the blockchain over time.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getblockcount&#x60;  ### Response - Returns a JSON object containing the current block count as a numeric value.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;block_count\&quot;: 650000 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This is a commonly used method for blockchain explorers, wallets, and other tools that need to know the current height of the blockchain.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetBlockCountResponse**](../Models/GetBlockCountResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getBlockDeltasGetblockdeltasBlockHashGet"></a>
# **getBlockDeltasGetblockdeltasBlockHashGet**
> GetBlockDeltasResponse getBlockDeltasGetblockdeltasBlockHashGet(block\_hash)

Get block deltas

    Retrieve detailed information about inputs and outputs of all transactions in a block.  ### Description - This endpoint returns detailed information about each transaction in the specified block, including inputs and outputs.  ### Input Parameters - &#x60;block_hash&#x60;: The hash of the block for which information is requested.  ### Example Request - &#x60;GET /getblockdeltas/00227e566682aebd6a7a5b772c96d7a999cadaebeaf1ce96f4191a3aad58b00b&#x60;  ### Response - Returns a JSON object containing detailed information about the block and its transactions.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;hash\&quot;: \&quot;00227e566682aebd6a7a5b772c96d7a999cadaebeaf1ce96f4191a3aad58b00b\&quot;,     \&quot;confirmations\&quot;: 10,     \&quot;size\&quot;: 190,     ... } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request. - HTTP 404: Not Found if the specified block hash does not exist.  ### Note - This endpoint requires the &#39;insightexplorer&#39; mode to be enabled on the Pastel node.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **block\_hash** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |

### Return type

[**GetBlockDeltasResponse**](../Models/GetBlockDeltasResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getBlockGetblockGet"></a>
# **getBlockGetblockGet**
> GetBlockResponse getBlockGetblockGet(block\_identifier, verbosity)

Get block data

    Get data of a specific block in the Pastel blockchain.   ### Description - Depending on the verbosity level, this endpoint returns different details about the specified block.  ### Input Parameters - &#x60;block_identifier&#x60;: The block hash or height. - &#x60;verbosity&#x60;: (Optional) Verbosity level (0, 1, or 2). Defaults to 1.  ### Example Request - &#x60;GET /getblock?block_identifier&#x3D;\&quot;00000000febc373a...\&quot;&amp;verbosity&#x3D;1&#x60;  ### Response - Depending on the verbosity, the response structure varies. Refer to the Pydantic models for details.  ### Example Response (verbosity &#x3D; 1) &#x60;&#x60;&#x60;json {     \&quot;hash\&quot;: \&quot;00000000febc373a...\&quot;,     \&quot;confirmations\&quot;: 10,     \&quot;size\&quot;: 800,     \&quot;height\&quot;: 12800,     ... } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Invalid parameters. - HTTP 404: Block not found. - HTTP 500: Internal Server Error.  ### Note - Used for detailed blockchain exploration and data analysis.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **block\_identifier** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **verbosity** | [**oas_any_type_not_mapped**](../Models/.md)|  | [optional] [default to 1] |

### Return type

[**GetBlockResponse**](../Models/GetBlockResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getBlockHashGetblockhashGet"></a>
# **getBlockHashGetblockhashGet**
> GetBlockHashResponse getBlockHashGetblockhashGet(GetBlockHashRequest)

Get the hash of a block at a specific index

    Get the hash of a block in the best-block-chain at the provided index.  ### Description - This endpoint returns the hash of the block at a given index in the blockchain. The index refers to the height of the block in the blockchain.  ### Input Parameters - &#x60;index&#x60; (int, required): The block index (height) in the blockchain.  ### Example Request - &#x60;GET /getblockhash?index&#x3D;1000&#x60;  ### Response - Returns a JSON object containing the hash of the block at the specified index.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;hash\&quot;: \&quot;00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the index parameter is invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - It&#39;s important to ensure the block index is within the valid range of the blockchain.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **GetBlockHashRequest** | [**GetBlockHashRequest**](../Models/GetBlockHashRequest.md)|  | |

### Return type

[**GetBlockHashResponse**](../Models/GetBlockHashResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="getBlockHeaderGetblockheaderBlockHashGet"></a>
# **getBlockHeaderGetblockheaderBlockHashGet**
> oas_any_type_not_mapped getBlockHeaderGetblockheaderBlockHashGet(block\_hash, verbose)

Get information about a block header

    Retrieve information about a block header by its hash.  ### Description - Returns either detailed information about the block header or its serialized, hex-encoded data, based on the &#39;verbose&#39; flag.  ### Input Parameters - &#x60;block_hash&#x60;: The hash of the block. - &#x60;verbose&#x60;: Boolean flag to determine the response format. Defaults to true.  ### Example Request - &#x60;GET /getblockheader/00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09?verbose&#x3D;true&#x60;  ### Response - If verbose is true, returns a JSON object with detailed block header information. - If verbose is false, returns a JSON object with serialized, hex-encoded block header data.  ### Example Response - If verbose is true: &#x60;&#x60;&#x60;json {   \&quot;hash\&quot;: \&quot;hash\&quot;,   \&quot;confirmations\&quot;: 5,   \&quot;height\&quot;: 123456,   ... } &#x60;&#x60;&#x60; - If verbose is false: &#x60;&#x60;&#x60;json {   \&quot;data\&quot;: \&quot;hex-encoded data\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 404: Block not found. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **block\_hash** | **String**|  | [default to null] |
| **verbose** | **Boolean**|  | [optional] [default to true] |

### Return type

[**oas_any_type_not_mapped**](../Models/AnyType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getBlockSubsidyGetblocksubsidyGet"></a>
# **getBlockSubsidyGetblocksubsidyGet**
> GetBlockSubsidyResponse getBlockSubsidyGetblocksubsidyGet(height)

Get block subsidy reward information

    Get the block subsidy reward for a given block height, considering the mining slow start.  ### Description - This endpoint returns the block subsidy reward, which includes the mining reward, masternode reward, and governance reward for the specified block height. - If the height is not provided, the subsidy for the current height of the chain is returned.  ### Input Parameters - &#x60;height&#x60;: (Optional, numeric) The block height. Defaults to the current height if not provided.  ### Example Request - &#x60;GET /getblocksubsidy?height&#x3D;1000&#x60;  ### Response - Returns a JSON object containing the subsidy rewards in each category.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;miner\&quot;: 12.345,     \&quot;masternode\&quot;: 3.210,     \&quot;governance\&quot;: 1.050 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the block height is out of range or invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for understanding the distribution of rewards in the blockchain at a given height.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **height** | **Integer**|  | [optional] [default to null] |

### Return type

[**GetBlockSubsidyResponse**](../Models/GetBlockSubsidyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getBlockTemplateGetblocktemplatePost"></a>
# **getBlockTemplateGetblocktemplatePost**
> GetBlockTemplateResponse getBlockTemplateGetblocktemplatePost(GetBlockTemplateRequest)

Get data needed to construct a block to work on

    Get data needed to construct a block to work on.  ### Description - This endpoint returns data necessary for constructing a block. It&#39;s primarily used by miners. - The method supports a &#39;template&#39; mode for requesting block template data and a &#39;proposal&#39; mode for submitting a block proposal.  ### Input Parameters - &#x60;jsonrequestobject&#x60; (string, optional): A JSON object specifying request details.  ### Example Request - &#x60;POST /getblocktemplate {\&quot;jsonrequestobject\&quot;: \&quot;{\&quot;mode\&quot;:\&quot;template\&quot;}\&quot;}&#x60;  ### Response - Returns a JSON object with details required to construct a block, including transactions to include, block version, target, and more.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;capabilities\&quot;: [\&quot;proposal\&quot;],     \&quot;version\&quot;: 4,     \&quot;previousblockhash\&quot;: \&quot;00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e\&quot;,     ... } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Detailed specification can be found at https://en.bitcoin.it/wiki/BIP_0022.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **GetBlockTemplateRequest** | [**GetBlockTemplateRequest**](../Models/GetBlockTemplateRequest.md)|  | |

### Return type

[**GetBlockTemplateResponse**](../Models/GetBlockTemplateResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="getBlockchainInfoGetblockchaininfoGet"></a>
# **getBlockchainInfoGetblockchaininfoGet**
> BlockchainInfoResponse getBlockchainInfoGetblockchaininfoGet()

Get blockchain information

    Get detailed information about the state of the blockchain.   ### Description - This endpoint returns various state info regarding blockchain processing.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getblockchaininfo&#x60;  ### Response - Returns a JSON object containing detailed information about the blockchain.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;chain\&quot;: \&quot;main\&quot;,     \&quot;blocks\&quot;: 680000,     \&quot;headers\&quot;: 680000,     \&quot;bestblockhash\&quot;: \&quot;00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e\&quot;,     \&quot;difficulty\&quot;: 19298087186262.61,     \&quot;verificationprogress\&quot;: 0.999998,     \&quot;chainwork\&quot;: \&quot;0000000000000000000000000000000000000000014d1e4fe926a7b5e76e7c6e\&quot;,     \&quot;commitments\&quot;: 289431,     \&quot;softforks\&quot;: [         {             \&quot;id\&quot;: \&quot;bip34\&quot;,             \&quot;version\&quot;: 2,             \&quot;enforce\&quot;: {\&quot;status\&quot;: true, \&quot;found\&quot;: 1000, \&quot;required\&quot;: 750, \&quot;window\&quot;: 1000},             \&quot;reject\&quot;: {\&quot;status\&quot;: true, \&quot;found\&quot;: 1000, \&quot;required\&quot;: 950, \&quot;window\&quot;: 1000}         }         // Include other softforks as needed     ],     \&quot;upgrades\&quot;: {         \&quot;upgrade1\&quot;: {             \&quot;name\&quot;: \&quot;example_upgrade\&quot;,             \&quot;activationheight\&quot;: 123456,             \&quot;status\&quot;: \&quot;active\&quot;,             \&quot;info\&quot;: \&quot;Additional information\&quot;         }         // Include other upgrades as needed     },     \&quot;consensus\&quot;: {         \&quot;chaintip\&quot;: \&quot;abcd1234\&quot;,         \&quot;nextblock\&quot;: \&quot;efgh5678\&quot;     },     \&quot;pruned\&quot;: false,     \&quot;pruneheight\&quot;: 12345 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for obtaining a variety of data about the blockchain&#39;s current state and history.

### Parameters
This endpoint does not need any parameter.

### Return type

[**BlockchainInfoResponse**](../Models/BlockchainInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getChainTipsGetchaintipsGet"></a>
# **getChainTipsGetchaintipsGet**
> GetChainTipsResponse getChainTipsGetchaintipsGet()

Get information about all known chain tips

    Return information about all known tips in the block tree, including the main chain as well as orphaned branches.  ### Description - This endpoint provides details about all known chain tips in the block tree. This includes information about the main chain and any orphaned or detached branches. - The response includes the height, hash, branch length, and status for each chain tip.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getchaintips&#x60;  ### Response - Returns a JSON array of objects, each representing a chain tip with its associated details.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;tips\&quot;: [         {             \&quot;height\&quot;: 123456,             \&quot;hash\&quot;: \&quot;00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e\&quot;,             \&quot;branchlen\&quot;: 0,             \&quot;status\&quot;: \&quot;active\&quot;         },         {             \&quot;height\&quot;: 123455,             \&quot;hash\&quot;: \&quot;00000000000000000007abc8d2b16cd689bd44e2f7f8f36b7e4f938b8b9c6f4f\&quot;,             \&quot;branchlen\&quot;: 1,             \&quot;status\&quot;: \&quot;valid-fork\&quot;         }     ] } &#x60;&#x60;&#x60;  ### Possible Status Values 1. &#x60;invalid&#x60;: Contains at least one invalid block. 2. &#x60;headers-only&#x60;: Not all blocks are available, but the headers are valid. 3. &#x60;valid-headers&#x60;: All blocks are available but were never fully validated. 4. &#x60;valid-fork&#x60;: Fully validated but not part of the active chain. 5. &#x60;active&#x60;: Part of the active main chain.  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for understanding the structure and different branches of the blockchain.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetChainTipsResponse**](../Models/GetChainTipsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getConnectionCountGetconnectioncountGet"></a>
# **getConnectionCountGetconnectioncountGet**
> GetConnectionCountResponse getConnectionCountGetconnectioncountGet()

Get the number of connections to other nodes

    Get the number of connections to other nodes in the Pastel network.  ### Description - This endpoint returns the total number of connections that the node has to other nodes in the network. It&#39;s an indicator of the node&#39;s connectivity and participation in the network.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getconnectioncount&#x60;  ### Response - Returns a JSON object containing the total number of connections.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;connection_count\&quot;: 15 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for network diagnostics and monitoring the node&#39;s network activity.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetConnectionCountResponse**](../Models/GetConnectionCountResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getDeprecationInfoGetdeprecationinfoGet"></a>
# **getDeprecationInfoGetdeprecationinfoGet**
> GetDeprecationInfoResponse getDeprecationInfoGetdeprecationinfoGet()

Get deprecation information of the current version

    Get information about the deprecation of the current server version.   ### Description - This endpoint returns an object containing details about the current server version, its subversion, and the block height at which this version will deprecate and shut down. This endpoint is applicable only on mainnet.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getdeprecationinfo&#x60;  ### Response - Returns a JSON object containing the server version, subversion, and deprecation block height.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;version\&quot;: 5000500,     \&quot;subversion\&quot;: \&quot;/MagicBean:5.0.5[-v]/\&quot;,     \&quot;deprecationheight\&quot;: 100000 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is typically used for software maintenance and upgrade planning.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetDeprecationInfoResponse**](../Models/GetDeprecationInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getDifficultyGetdifficultyGet"></a>
# **getDifficultyGetdifficultyGet**
> GetDifficultyResponse getDifficultyGetdifficultyGet()

Get the current proof-of-work difficulty

    Get the current proof-of-work difficulty as a multiple of the minimum difficulty.  ### Description - This endpoint returns the current network difficulty for proof-of-work. It&#39;s a measure of how difficult it is to find a new block compared to the easiest it can ever be.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getdifficulty&#x60;  ### Response - Returns a JSON object containing the current proof-of-work difficulty as a numeric value.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;difficulty\&quot;: 874.625 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This information is particularly useful for miners and analysts interested in the network&#39;s mining difficulty.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetDifficultyResponse**](../Models/GetDifficultyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getFeeScheduleGetfeescheduleGet"></a>
# **getFeeScheduleGetfeescheduleGet**
> GetFeeScheduleResponse getFeeScheduleGetfeescheduleGet()

Get the current fee schedule

    Get the current fee schedule including the chain deflation rate and related fees.  ### Description - This endpoint returns the current fee schedule of the network, which includes various fees associated with operations like PastelID registration, username registration, and username change. - It also provides the fee deflator factor, which is used to adjust fees based on the chain deflation rate.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getfeeschedule&#x60;  ### Response - Returns a JSON object containing the current fee schedule.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;fee_deflator_factor\&quot;: 1.5,     \&quot;pastelid_registration_fee\&quot;: 100.0,     \&quot;username_registration_fee\&quot;: 50.0,     \&quot;username_change_fee\&quot;: 20.0 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This information is crucial for users and applications that interact with the network, especially for those involving registrations and updates.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetFeeScheduleResponse**](../Models/GetFeeScheduleResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getGenerateGetgenerateGet"></a>
# **getGenerateGetgenerateGet**
> GetGenerateResponse getGenerateGetgenerateGet()

Check if the server is set to generate coins

    Check if the server is currently set to generate coins.  ### Description - This endpoint checks the server&#39;s coin generation status, which indicates whether the server is set to mine new coins.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getgenerate&#x60;  ### Response - Returns a JSON object indicating whether the server is set to generate coins.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;is_generating\&quot;: false } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The coin generation status is controlled by the &#x60;-gen&#x60; command line argument or the &#x60;gen&#x60; setting in &#x60;pastel.conf&#x60;. It can also be modified using the &#x60;setgenerate&#x60; call.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetGenerateResponse**](../Models/GetGenerateResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getInfoGetinfoGet"></a>
# **getInfoGetinfoGet**
> GetInfoResponse getInfoGetinfoGet()

Get various state info

    Get an object containing various state info about the Pastel server.  ### Description - This endpoint provides information about the server&#39;s state, including wallet balance, block count, connections, and other relevant details.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getinfo&#x60;  ### Response - Returns a JSON object containing various state information of the server.  ### Example Response &#x60;&#x60;&#x60;json {   \&quot;version\&quot;: 50000,   \&quot;protocolversion\&quot;: 70015,   \&quot;walletversion\&quot;: 60000,   \&quot;balance\&quot;: 15.0,   \&quot;blocks\&quot;: 120987,   \&quot;timeoffset\&quot;: 0,   \&quot;connections\&quot;: 8,   \&quot;proxy\&quot;: \&quot;127.0.0.1:9050\&quot;,   \&quot;difficulty\&quot;: 1.23456789,   \&quot;testnet\&quot;: false,   \&quot;keypoololdest\&quot;: 1577836800,   \&quot;keypoolsize\&quot;: 1000,   \&quot;unlocked_until\&quot;: 1596240000,   \&quot;paytxfee\&quot;: 0.0001,   \&quot;relayfee\&quot;: 0.00001,   \&quot;errors\&quot;: \&quot;Warning: unknown new rules activated (versionbit 28)\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is useful for getting a quick overview of the state of the server and its wallet.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetInfoResponse**](../Models/GetInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getLocalSolpsGetlocalsolpsGet"></a>
# **getLocalSolpsGetlocalsolpsGet**
> GetLocalSolpsResponse getLocalSolpsGetlocalsolpsGet()

Get average local solutions per second

    Get the average local solutions per second since this node was started.   ### Description - This endpoint returns the average number of solutions per second that the local node has been generating since it was started. This metric is an indicator of the mining or hashing power of the local node.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getlocalsolps&#x60;  ### Response - Returns a JSON object containing the average solutions per second.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;sols_per_second\&quot;: 123.456 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This information is typically shown on the metrics screen of the node, if enabled.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetLocalSolpsResponse**](../Models/GetLocalSolpsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getMemoryInfoGetmemoryinfoGet"></a>
# **getMemoryInfoGetmemoryinfoGet**
> GetMemoryInfoResponse getMemoryInfoGetmemoryinfoGet()

Get memory usage information

    Get detailed information about memory usage by the Pastel node.   ### Description - This endpoint returns information about the memory usage, including details about used and free memory, total memory managed, amount of memory locked, and the number of chunks used and free.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getmemoryinfo&#x60;  ### Response - Returns a JSON object containing detailed memory usage information.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;locked\&quot;: {         \&quot;used\&quot;: 123456,         \&quot;free\&quot;: 654321,         \&quot;total\&quot;: 1000000,         \&quot;locked\&quot;: 500000,         \&quot;chunks_used\&quot;: 20,         \&quot;chunks_free\&quot;: 80     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for monitoring the memory performance and health of the Pastel node.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetMemoryInfoResponse**](../Models/GetMemoryInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getMempoolInfoGetmempoolinfoGet"></a>
# **getMempoolInfoGetmempoolinfoGet**
> GetMempoolInfoResponse getMempoolInfoGetmempoolinfoGet()

Get active state of the TX memory pool

    Returns details on the active state of the TX memory pool.  ### Description - This endpoint provides information about the current state of the transaction memory pool.  - It includes details such as the total number of transactions in the pool, the sum of all transaction sizes, and the total memory usage of the mempool.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getmempoolinfo&#x60;  ### Response - Returns a JSON object containing details about the transaction memory pool.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;size\&quot;: 45,     \&quot;bytes\&quot;: 123456,     \&quot;usage\&quot;: 98765 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is useful for understanding the load and capacity of the transaction memory pool.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetMempoolInfoResponse**](../Models/GetMempoolInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getMiningInfoGetmininginfoGet"></a>
# **getMiningInfoGetmininginfoGet**
> GetMiningInfoResponse getMiningInfoGetmininginfoGet()

Get mining-related information

    Retrieve mining-related information from the blockchain.  ### Description - Returns a JSON object containing various details about the state of mining on the Pastel blockchain, such as the current block, block size, transactions, difficulty, and network solution rate.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getmininginfo&#x60;  ### Response - Returns a JSON object containing detailed mining information.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;blocks\&quot;: 100,     \&quot;currentblocksize\&quot;: 1000,     \&quot;currentblocktx\&quot;: 10,     \&quot;difficulty\&quot;: 1.23456789,     \&quot;errors\&quot;: \&quot;None\&quot;,     \&quot;generate\&quot;: false,     \&quot;genproclimit\&quot;: -1,     \&quot;localsolps\&quot;: 2.345678,     \&quot;networksolps\&quot;: 1234567,     \&quot;pooledtx\&quot;: 5,     \&quot;testnet\&quot;: false,     \&quot;chain\&quot;: \&quot;main\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for miners and network analysts to understand the current mining environment and network health.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetMiningInfoResponse**](../Models/GetMiningInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getNetTotalsGetnettotalsGet"></a>
# **getNetTotalsGetnettotalsGet**
> GetNetTotalsResponse getNetTotalsGetnettotalsGet()

Get network traffic information

    Get information about network traffic, including total bytes received, total bytes sent, and current time.  ### Description - This endpoint returns statistics about the network traffic, including the total number of bytes received and sent by the node since startup, as well as the current time in milliseconds.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getnettotals&#x60;  ### Response - Returns a JSON object containing the network traffic statistics.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;totalbytesrecv\&quot;: 123456,     \&quot;totalbytessent\&quot;: 654321,     \&quot;timemillis\&quot;: 1627891234567 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for monitoring and diagnostics of the node&#39;s network activity.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetNetTotalsResponse**](../Models/GetNetTotalsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getNetworkInfoGetnetworkinfoGet"></a>
# **getNetworkInfoGetnetworkinfoGet**
> GetNetworkInfoResponse getNetworkInfoGetnetworkinfoGet()

Get various state info regarding P2P networking

    Get an object containing various state information regarding P2P networking.  ### Description - This endpoint returns an object containing various state information regarding the P2P networking of the Pastel node. - It provides details like server version, protocol version, connections, and network information.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getnetworkinfo&#x60;  ### Response - Returns a JSON object containing various state info regarding P2P networking.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;version\&quot;: 5000000,     \&quot;subversion\&quot;: \&quot;/MagicBean:5.0.0[-v]/\&quot;,     \&quot;protocolversion\&quot;: 170013,     \&quot;localservices\&quot;: \&quot;000000000000040d\&quot;,     \&quot;timeoffset\&quot;: 0,     \&quot;connections\&quot;: 10,     \&quot;networks\&quot;: [         {             \&quot;name\&quot;: \&quot;ipv4\&quot;,             \&quot;limited\&quot;: false,             \&quot;reachable\&quot;: true,             \&quot;proxy\&quot;: \&quot;\&quot;         }     ],     \&quot;relayfee\&quot;: 0.00001000,     \&quot;localaddresses\&quot;: [         {             \&quot;address\&quot;: \&quot;123.45.67.89\&quot;,             \&quot;port\&quot;: 8333,             \&quot;score\&quot;: 1         }     ],     \&quot;warnings\&quot;: \&quot;\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetNetworkInfoResponse**](../Models/GetNetworkInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getNetworkSolpsGetnetworksolpsGet"></a>
# **getNetworkSolpsGetnetworksolpsGet**
> GetNetworkSolpsResponse getNetworkSolpsGetnetworksolpsGet(GetNetworkSolpsRequest)

Get estimated network solutions per second

    Get the estimated network solutions per second based on the last n blocks.  ### Description - This endpoint estimates the network&#39;s solutions per second based on the last specified number of blocks.  - You can override the number of blocks to consider, or use -1 to specify the blocks over the difficulty averaging window. - You can also provide a block height to estimate the network speed at the time when that specific block was found.  ### Input Parameters - &#x60;blocks&#x60; (int, optional, default&#x3D;120): The number of blocks to consider, or -1 for blocks over the difficulty averaging window. - &#x60;height&#x60; (int, optional, default&#x3D;-1): The block height for estimating the network speed.  ### Example Request - &#x60;GET /getnetworksolps?blocks&#x3D;100&amp;height&#x3D;5000&#x60;  ### Response - Returns a JSON object containing the estimated solutions per second.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;solutions_per_second\&quot;: 1234567.89 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **GetNetworkSolpsRequest** | [**GetNetworkSolpsRequest**](../Models/GetNetworkSolpsRequest.md)|  | |

### Return type

[**GetNetworkSolpsResponse**](../Models/GetNetworkSolpsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="getNetworksInfoGetnetworksinfoGet"></a>
# **getNetworksInfoGetnetworksinfoGet**
> GetNetworksInfoResponse getNetworksInfoGetnetworksinfoGet()

Get information about all the networks

    Get detailed information about all the networks known to the node.  ### Description - This endpoint provides information about each network that the node is aware of. It includes details like the network&#39;s name, its accessibility status, and any associated proxy settings.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getnetworksinfo&#x60;  ### Response - Returns a JSON array of objects, each representing a network with its specific details.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;networks\&quot;: [         {             \&quot;name\&quot;: \&quot;ipv4\&quot;,             \&quot;limited\&quot;: false,             \&quot;reachable\&quot;: true,             \&quot;proxy\&quot;: \&quot;192.168.1.1:9050\&quot;,             \&quot;proxy_randomize_credentials\&quot;: true         },         {             \&quot;name\&quot;: \&quot;ipv6\&quot;,             \&quot;limited\&quot;: false,             \&quot;reachable\&quot;: true,             \&quot;proxy\&quot;: \&quot;\&quot;,             \&quot;proxy_randomize_credentials\&quot;: false         }     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is useful for network diagnostics and for understanding the node&#39;s perspective of the network topology.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetNetworksInfoResponse**](../Models/GetNetworksInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getNewAddressGetnewaddressGet"></a>
# **getNewAddressGetnewaddressGet**
> GetNewAddressResponse getNewAddressGetnewaddressGet(account)

Generate a new Pastel address

    Generate a new Pastel address for receiving payments.  ### Description - This endpoint creates a new Pastel address which can be used to receive payments. - The new address is automatically associated with the default account.  ### Input Parameters - &#x60;account&#x60;: (string, optional) DEPRECATED. The account name for the address. It must be the empty string &#x60;\&quot;\&quot;&#x60; for the default account. Any other value will result in an error.  ### Example Request - &#x60;GET /getnewaddress?account&#x3D;\&quot;\&quot;&#x60;  ### Response - Returns a JSON object containing the new Pastel address in string format.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;address\&quot;: \&quot;pZb7J2fg9BpM1Kj3n3FjR5Bn25S55hKx2x\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The generated address is added to the wallet and can be used immediately for receiving funds.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **account** | [**Account**](../Models/.md)|  | [optional] [default to ] |

### Return type

[**GetNewAddressResponse**](../Models/GetNewAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getNextBlockSubsidyGetnextblocksubsidyGet"></a>
# **getNextBlockSubsidyGetnextblocksubsidyGet**
> GetNextBlockSubsidyResponse getNextBlockSubsidyGetnextblocksubsidyGet()

Get subsidy rewards for the next block

    Get the block subsidy rewards of the next block in the Pastel blockchain.  ### Description - This endpoint returns the subsidy rewards for the next block, including the amounts for the miner, masternode, and governance.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getnextblocksubsidy&#x60;  ### Response - Returns a JSON object containing the subsidy rewards for the next block.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;miner\&quot;: 12.5,     \&quot;masternode\&quot;: 6.25,     \&quot;governance\&quot;: 1.25 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint provides crucial information for understanding the reward distribution in the upcoming block.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetNextBlockSubsidyResponse**](../Models/GetNextBlockSubsidyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getPeerInfoGetpeerinfoGet"></a>
# **getPeerInfoGetpeerinfoGet**
> GetPeerInfoResponse getPeerInfoGetpeerinfoGet()

Get data about each connected network node

    Get data about each connected network node as a json array of objects.  ### Description - This endpoint returns detailed information about each peer connected to the Pastel network.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getpeerinfo&#x60;  ### Response - Returns a JSON array containing information about each connected network node.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;peers\&quot;: [         {             \&quot;id\&quot;: 1,             \&quot;addr\&quot;: \&quot;host:port\&quot;,             \&quot;addrlocal\&quot;: \&quot;ip:port\&quot;,             \&quot;services\&quot;: \&quot;xxxxxxxxxxxxxxxx\&quot;,             \&quot;lastsend\&quot;: 1617704837,             \&quot;lastrecv\&quot;: 1617704837,             ...         },         ...     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for network diagnostics and analysis.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetPeerInfoResponse**](../Models/GetPeerInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getRawChangeAddressGetrawchangeaddressGet"></a>
# **getRawChangeAddressGetrawchangeaddressGet**
> oas_any_type_not_mapped getRawChangeAddressGetrawchangeaddressGet()

Get a new Pastel address for receiving change

    Get a new Pastel address for receiving change. This is for use with raw transactions, NOT for normal use.  ### Description - This endpoint generates and returns a new Pastel address that can be used for receiving change in raw transactions. - It is important to note that this address should not be used for regular transactions.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getrawchangeaddress&#x60;  ### Response - Returns a string representing the new Pastel address.  ### Example Response &#x60;&#x60;&#x60;json \&quot;mnX4Ph6uhz2ez5y9Yb9hWPiPH5G9Wp2VWJ\&quot; &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request. - RPC_WALLET_KEYPOOL_RAN_OUT: Error message if the keypool has run out. In this case, the &#x60;keypoolrefill&#x60; RPC method should be called first.  ### Note - This address should only be used for change in raw transactions and not for general transaction purposes.

### Parameters
This endpoint does not need any parameter.

### Return type

[**oas_any_type_not_mapped**](../Models/AnyType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getRawMempoolGetrawmempoolGet"></a>
# **getRawMempoolGetrawmempoolGet**
> oas_any_type_not_mapped getRawMempoolGetrawmempoolGet(verbose)

Get all transaction IDs in memory pool

    Get the transaction IDs in the memory pool.   ### Description - Returns all transaction IDs in the memory pool as an array of strings or a detailed JSON object.  ### Input Parameters - &#x60;verbose&#x60;: (boolean, optional, default&#x3D;false) Set to true for a detailed JSON object, false for an array of transaction IDs.  ### Example Request - &#x60;GET /getrawmempool?verbose&#x3D;false&#x60;  ### Response - For &#x60;verbose&#x3D;false&#x60;, returns an array of transaction IDs. - For &#x60;verbose&#x3D;true&#x60;, returns a detailed JSON object with information about each transaction.  ### Example Response for &#x60;verbose&#x3D;false&#x60; &#x60;&#x60;&#x60;json {     \&quot;transaction_ids\&quot;: [\&quot;txid1\&quot;, \&quot;txid2\&quot;, \&quot;txid3\&quot;] } &#x60;&#x60;&#x60;  ### Example Response for &#x60;verbose&#x3D;true&#x60; &#x60;&#x60;&#x60;json {     \&quot;transactions\&quot;: {         \&quot;txid1\&quot;: {             \&quot;size\&quot;: 250,             \&quot;fee\&quot;: 0.0001,             \&quot;time\&quot;: 1617184000,             \&quot;height\&quot;: 675000,             \&quot;startingpriority\&quot;: 1000000,             \&quot;currentpriority\&quot;: 1200000,             \&quot;depends\&quot;: [\&quot;txidA\&quot;, \&quot;txidB\&quot;]         },         ...     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for retrieving detailed information about transactions in the mempool.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **verbose** | **Boolean**|  | [optional] [default to null] |

### Return type

[**oas_any_type_not_mapped**](../Models/AnyType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getRawTransactionGetrawtransactionPost"></a>
# **getRawTransactionGetrawtransactionPost**
> oas_any_type_not_mapped getRawTransactionGetrawtransactionPost(GetRawTransactionRequest)

Get the raw transaction data

    Get the raw transaction data for a given transaction id.  ### Description - This endpoint returns the raw transaction data based on the given transaction ID. - If &#x60;verbose&#x60; is 0 or not set, it returns a string that is serialized, hex-encoded data for the transaction. - If &#x60;verbose&#x60; is non-zero, it returns a JSON object with detailed information about the transaction.  ### Input Parameters - &#x60;txid&#x60; (string, required): The transaction id. - &#x60;verbose&#x60; (int, optional, default&#x3D;0): If 0, return a string, otherwise return a JSON object. - &#x60;blockhash&#x60; (string, optional): The block hash to look for the transaction in.  ### Example Request - &#x60;POST /getrawtransaction&#x60; with JSON body &#x60;{\&quot;txid\&quot;: \&quot;mytxid\&quot;, \&quot;verbose\&quot;: 1}&#x60;  ### Response - Depending on the &#x60;verbose&#x60; parameter, either a string or a JSON object with detailed transaction information.  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **GetRawTransactionRequest** | [**GetRawTransactionRequest**](../Models/GetRawTransactionRequest.md)|  | |

### Return type

[**oas_any_type_not_mapped**](../Models/AnyType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="getReceivedByAccountGetreceivedbyaccountGet"></a>
# **getReceivedByAccountGetreceivedbyaccountGet**
> GetReceivedByAccountResponse getReceivedByAccountGetreceivedbyaccountGet(GetReceivedByAccountRequest)

Get the total amount received by an account

    Get the total amount received by addresses with a specified account in transactions with at least a certain number of confirmations.  ### Description - This endpoint returns the total amount received by addresses associated with a given account, considering transactions with at least the specified number of confirmations. - Note: The &#39;account&#39; parameter is deprecated and should be set to an empty string \&quot;\&quot; to represent the default account.  ### Input Parameters - &#x60;account&#x60; (string, required): Must be set to the empty string \&quot;\&quot; to represent the default account. Passing any other string will result in an error. - &#x60;minconf&#x60; (int, optional, default&#x3D;1): Only include transactions confirmed at least this many times.  ### Example Request - &#x60;GET /getreceivedbyaccount?account&#x3D;\&quot;\&quot;&amp;minconf&#x3D;1&#x60;  ### Response - Returns the total amount received by the specified account.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;amount\&quot;: 123.45 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **GetReceivedByAccountRequest** | [**GetReceivedByAccountRequest**](../Models/GetReceivedByAccountRequest.md)|  | |

### Return type

[**GetReceivedByAccountResponse**](../Models/GetReceivedByAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="getReceivedByAddressGetreceivedbyaddressGet"></a>
# **getReceivedByAddressGetreceivedbyaddressGet**
> GetReceivedByAddressResponse getReceivedByAddressGetreceivedbyaddressGet(zcashaddress, minconf)

Get the total amount received by a Pastel address

    Get the total amount received by the given Pastel address in transactions with at least a specified number of confirmations.  ### Description - This endpoint returns the total amount received by a specific Pastel address in transactions that are confirmed at least a specified number of times.  ### Input Parameters - &#x60;zcashaddress&#x60;: The Pastel address for transactions. - &#x60;minconf&#x60;: (Optional) The minimum number of confirmations for transactions. Defaults to 1.  ### Example Request - &#x60;GET /getreceivedbyaddress?zcashaddress&#x3D;PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n&amp;minconf&#x3D;1&#x60;  ### Response - Returns a JSON object containing the total amount received at the given address.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;total_amount\&quot;: 10.5 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the address is invalid or not provided. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for retrieving the total amount received at a particular Pastel address.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **zcashaddress** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **minconf** | [**Minconf**](../Models/.md)|  | [optional] [default to 1] |

### Return type

[**GetReceivedByAddressResponse**](../Models/GetReceivedByAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getStorageFeeGetFeeStoragefeeGetfeeGet"></a>
# **getStorageFeeGetFeeStoragefeeGetfeeGet**
> StorageFeeGetFeeResponse getStorageFeeGetFeeStoragefeeGetfeeGet(fee\_type, is\_local, height)

Get the storage fee

    Get the current storage fee based on the specified fee type and blockchain height.  ### Description - This endpoint returns the current storage fee based on the given fee type, optional local/global flag, and blockchain height.  ### Input Parameters - &#x60;fee_type&#x60;: The type of fee to retrieve (e.g., \&quot;nftTicketFee\&quot;). - &#x60;is_local&#x60;: (Optional) A boolean to specify if the fee is local or global. Defaults to &#x60;False&#x60;. - &#x60;height&#x60;: (Optional) The blockchain height for which to retrieve the fee. If not provided, the current height is used.  ### Example Request - &#x60;GET /storagefee/getfee?fee_type&#x3D;nftTicketFee&amp;is_local&#x3D;true&amp;height&#x3D;100000&#x60;  ### Response - Returns a JSON object containing the storage fee, fee in &#39;pat&#39; units, blockchain height, and chain deflator factor.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;fee\&quot;: 0.002,     \&quot;fee_pat\&quot;: 200000,     \&quot;height\&quot;: 100000,     \&quot;chain_deflator_factor\&quot;: 1.5 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Used to determine the current storage fee for various operations on the blockchain.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fee\_type** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **is\_local** | [**Is_Local**](../Models/.md)|  | [optional] [default to false] |
| **height** | [**Height**](../Models/.md)|  | [optional] [default to null] |

### Return type

[**StorageFeeGetFeeResponse**](../Models/StorageFeeGetFeeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getStorageFeesStoragefeeGetfeesGet"></a>
# **getStorageFeesStoragefeeGetfeesGet**
> GetFeesResponse getStorageFeesStoragefeeGetfeesGet()

Get the current storage fees

    Get the current storage fees adjusted by the network median and local factors.  ### Description - This endpoint returns the current storage fees based on the network&#39;s median fee and local fee for various actions. - The fees are adjusted by a fee deflator factor, which is based on the blockchain&#39;s state.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /storagefee/getfees&#x60;  ### Response - Returns a JSON object containing storage fees for different actions.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;height\&quot;: 12345,     \&quot;chain_deflator_factor\&quot;: 1.5,     \&quot;fees\&quot;: {         \&quot;actionName\&quot;: {             \&quot;fee\&quot;: 100,             \&quot;fee_pat\&quot;: 100000         },         ...     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetFeesResponse**](../Models/GetFeesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getTotalStorageFeeTicketsToolsGettotalstoragefeePost"></a>
# **getTotalStorageFeeTicketsToolsGettotalstoragefeePost**
> GetTotalStorageFeeResponse getTotalStorageFeeTicketsToolsGettotalstoragefeePost(GetTotalStorageFeeRequest)

Calculate Total Storage Fee for NFT Registration

    Calculate the total storage fee for the NFT registration ticket.  ### Description - This endpoint calculates the full storage fee for NFT registration based on the provided ticket details and image size.  ### Input Parameters - &#x60;ticket&#x60;: Base64 encoded ticket created by the creator. - &#x60;signatures&#x60;: Base64 encoded signatures and Pastel IDs of the creator and verifying masternodes. - &#x60;pastelid&#x60;: The registering masternode (MN1) Pastel ID. - &#x60;passphrase&#x60;: Passphrase for the private key associated with the Pastel ID. - &#x60;label&#x60;: Label for the ticket. - &#x60;fee&#x60;: Agreed upon storage fee. - &#x60;imagesize&#x60;: Size of the image in MB.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;ticket\&quot;: \&quot;ticket-blob\&quot;,     \&quot;signatures\&quot;: \&quot;{signatures}\&quot;,     \&quot;pastelid\&quot;: \&quot;jXYqZNPj21RVnwxnEJ654wEdzi7GZTZ5LAdiotBmPrF7pDMkpX1JegDMQZX55WZLkvy9fxNpZcbBJuE8QYUqBF\&quot;,     \&quot;passphrase\&quot;: \&quot;passphrase\&quot;,     \&quot;label\&quot;: \&quot;label\&quot;,     \&quot;fee\&quot;: 100,     \&quot;imagesize\&quot;: 3 } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the total storage fee for the NFT registration.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;totalstoragefee\&quot;: 500 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Used during the NFT registration process to calculate the storage fee.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **GetTotalStorageFeeRequest** | [**GetTotalStorageFeeRequest**](../Models/GetTotalStorageFeeRequest.md)|  | |

### Return type

[**GetTotalStorageFeeResponse**](../Models/GetTotalStorageFeeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="getTransactionGettransactionTxidGet"></a>
# **getTransactionGettransactionTxidGet**
> GetTransactionResponse getTransactionGettransactionTxidGet(txid, includeWatchonly)

Get detailed information about a transaction

    Retrieve detailed information about an in-wallet transaction by its ID.  ### Description - Fetches detailed data of a specified transaction from the wallet, including amounts, confirmations, and related addresses.  ### Input Parameters - &#x60;txid&#x60;: The transaction ID to query. - &#x60;includeWatchonly&#x60;: (Optional) Include watch-only addresses in balance calculation and details.  ### Example Request - &#x60;GET /gettransaction/1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d&#x60;  ### Response - Returns detailed information about the specified transaction.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;status\&quot;: \&quot;mined\&quot;,     \&quot;amount\&quot;: 10.0,     \&quot;amountPat\&quot;: 10000,     \&quot;confirmations\&quot;: 15,     \&quot;blockhash\&quot;: \&quot;00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e\&quot;,     \&quot;blockindex\&quot;: 1,     \&quot;blocktime\&quot;: 1625097600,     \&quot;txid\&quot;: \&quot;1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d\&quot;,     \&quot;time\&quot;: 1625097600,     \&quot;timereceived\&quot;: 1625097600,     \&quot;details\&quot;: [         {             \&quot;account\&quot;: \&quot;\&quot;,             \&quot;address\&quot;: \&quot;t1Xin4H451oBDwrKcQeY1VGgMWivLs2hhuR\&quot;,             \&quot;category\&quot;: \&quot;receive\&quot;,             \&quot;amount\&quot;: 10.0,             \&quot;amountPat\&quot;: 10000,             \&quot;vout\&quot;: 0         }     ],     \&quot;hex\&quot;: \&quot;010000000...\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the transaction ID is invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is used to obtain transaction details for wallet transactions.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **txid** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **includeWatchonly** | [**Includewatchonly_1**](../Models/.md)|  | [optional] [default to false] |

### Return type

[**GetTransactionResponse**](../Models/GetTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getTxOutGettxoutGet"></a>
# **getTxOutGettxoutGet**
> GetTxOutResponse getTxOutGettxoutGet(txid, n, includemempool)

Get details about an unspent transaction output

    Get details about an unspent transaction output.   ### Description - This endpoint returns detailed information about an unspent transaction output (UTXO) from the Pastel blockchain.  ### Input Parameters - &#x60;txid&#x60;: (string, required) The transaction id. - &#x60;n&#x60;: (int, required) The output number (vout) of the transaction. - &#x60;includemempool&#x60;: (bool, optional) Whether to include the mempool. Defaults to True.  ### Example Request - &#x60;GET /gettxout?txid&#x3D;&lt;txid&gt;&amp;n&#x3D;1&amp;includemempool&#x3D;true&#x60;  ### Response - Returns a JSON object containing details of the specified unspent transaction output.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;bestblock\&quot;: \&quot;00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e\&quot;,     \&quot;confirmations\&quot;: 10,     \&quot;value\&quot;: 12.34,     \&quot;valuePat\&quot;: 1234000000,     \&quot;scriptPubKey\&quot;: {         \&quot;asm\&quot;: \&quot;code\&quot;,         \&quot;hex\&quot;: \&quot;hex\&quot;,         \&quot;reqSigs\&quot;: 1,         \&quot;type\&quot;: \&quot;pubkeyhash\&quot;,         \&quot;addresses\&quot;: [\&quot;address1\&quot;, \&quot;address2\&quot;]     },     \&quot;version\&quot;: 2,     \&quot;coinbase\&quot;: false } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 404: Not Found if the specified transaction output is not found or is already spent. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is useful for verifying the existence and details of specific transaction outputs.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **txid** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **n** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **includemempool** | [**Includemempool**](../Models/.md)|  | [optional] [default to true] |

### Return type

[**GetTxOutResponse**](../Models/GetTxOutResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getTxOutProofGettxoutproofGet"></a>
# **getTxOutProofGettxoutproofGet**
> GetTxOutProofResponse getTxOutProofGettxoutproofGet(body, block\_hash)

Get proof of transaction inclusion in a block

    Get a hex-encoded proof that one or more transactions were included in a block.  ### Description - This endpoint returns a serialized, hex-encoded data for the proof that specified transaction(s) were included in a block. - By default, this function only works if there is an unspent output in the UTXO for these transactions. To make it always work, maintain a transaction index with the -txindex command line option, or specify the block hash manually.  ### Input Parameters - &#x60;txids&#x60;: A list of transaction IDs to filter. - &#x60;block_hash&#x60; (Optional): The hash of the block in which to look for the transactions.  ### Example Request - &#x60;GET /gettxoutproof?txids&#x3D;[\&quot;txid1\&quot;,\&quot;txid2\&quot;]&amp;block_hash&#x3D;00000000abc123&#x60;  ### Response - Returns a string that is a serialized, hex-encoded data for the proof.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;data\&quot;: \&quot;serialized-hex-encoded-proof-data\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Ensure that the transaction index is maintained for accurate results.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | **oas_any_type_not_mapped**|  | |
| **block\_hash** | [**Block_Hash**](../Models/.md)|  | [optional] [default to null] |

### Return type

[**GetTxOutProofResponse**](../Models/GetTxOutProofResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="getTxOutSetInfoGettxoutsetinfoGet"></a>
# **getTxOutSetInfoGettxoutsetinfoGet**
> GetTxOutSetInfoResponse getTxOutSetInfoGettxoutsetinfoGet()

Get statistics about the unspent transaction output set

    Returns statistics about the unspent transaction output set.  ### Description - This endpoint provides detailed information about the state of the unspent transaction output set. It&#39;s useful for getting a snapshot of the blockchain&#39;s UTXO set at the current moment. - Note: This call may take some time due to the calculations involved.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /gettxoutsetinfo&#x60;  ### Response - Returns a JSON object containing various statistics about the UTXO set.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;height\&quot;: 650000,     \&quot;bestblock\&quot;: \&quot;0000000000000000000c6da2c440...\&quot;,     \&quot;transactions\&quot;: 2500000,     \&quot;txouts\&quot;: 5000000,     \&quot;bytes_serialized\&quot;: 300000000,     \&quot;hash_serialized\&quot;: \&quot;3e9cc7000...\&quot;,     \&quot;total_amount\&quot;: 18446744.07370955 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is particularly useful for analysis and understanding the overall state of the blockchain.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetTxOutSetInfoResponse**](../Models/GetTxOutSetInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getTxfeeGettxfeeTxidGet"></a>
# **getTxfeeGettxfeeTxidGet**
> GetTxfeeResponse getTxfeeGettxfeeTxidGet(txid)

Get transaction fee by txid

    Get the transaction fee for a specific transaction by its transaction ID (txid).  ### Description - This endpoint retrieves the transaction fee for a given transaction ID in the Pastel blockchain.  ### Input Parameters - &#x60;txid&#x60;: The transaction ID for which the transaction fee is requested.  ### Example Request - &#x60;GET /gettxfee/e4ee20e436d33f59cc313647bacff0c5b0df5b7b1c1fa13189ea7bc8b9df15a4&#x60;  ### Response - Returns a JSON object containing details of the transaction fee.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;txid\&quot;: \&quot;e4ee20e436d33f59cc313647bacff0c5b0df5b7b1c1fa13189ea7bc8b9df15a4\&quot;,     \&quot;height\&quot;: 123456,     \&quot;blockHash\&quot;: \&quot;00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e\&quot;,     \&quot;txFeePat\&quot;: 50000,     \&quot;txFee\&quot;: 0.0005 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the txid is invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for wallets and explorers to determine the fee associated with a particular transaction.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **txid** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |

### Return type

[**GetTxfeeResponse**](../Models/GetTxfeeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getWalletInfoGetwalletinfoGet"></a>
# **getWalletInfoGetwalletinfoGet**
> WalletInfoResponse getWalletInfoGetwalletinfoGet()

Get wallet state information

    Returns an object containing various wallet state info.  ### Description - This endpoint provides information about the wallet, including balances, transaction count, key pool size, and other relevant data.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getwalletinfo&#x60;  ### Response - Returns a JSON object containing detailed information about the wallet.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;walletversion\&quot;: 169900,     \&quot;balance\&quot;: 0.015,     \&quot;unconfirmed_balance\&quot;: 0.0,     \&quot;immature_balance\&quot;: 0.0,     \&quot;txcount\&quot;: 2,     \&quot;keypoololdest\&quot;: 1600000000,     \&quot;keypoolsize\&quot;: 1000,     \&quot;unlocked_until\&quot;: null,     \&quot;paytxfee\&quot;: 0.00001,     \&quot;seedfp\&quot;: \&quot;d1f1a9fc\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters
This endpoint does not need any parameter.

### Return type

[**WalletInfoResponse**](../Models/WalletInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="governanceActionGovernancePost"></a>
# **governanceActionGovernancePost**
> Response_Governance_Action_Governance_Post governanceActionGovernancePost(mode, subcommand, body)

Cast a vote or list governance tickets

    Perform governance-related actions such as voting for tickets or listing tickets/winners.  ### Description - This endpoint allows casting votes for governance tickets or listing all governance tickets or winners.  ### Input Parameters - &#x60;mode&#x60;: &#39;ticket&#39; or &#39;list&#39; to specify the action. - &#x60;subcommand&#x60;: Depending on the mode, additional parameters for the action.  ### Example Request - &#x60;POST /governance&#x60;   &#x60;&#x60;&#x60;json   {       \&quot;mode\&quot;: \&quot;ticket\&quot;,       \&quot;subcommand\&quot;: \&quot;add\&quot;,       \&quot;parameters\&quot;: [\&quot;address\&quot;, 10, \&quot;note\&quot;, \&quot;yes\&quot;]   }   &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the result of the governance action.  ### Example Response   &#x60;&#x60;&#x60;json   {       \&quot;result\&quot;: \&quot;success\&quot;,       \&quot;ticketId\&quot;: \&quot;ticket_id_here\&quot;   }   &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Used for participating in the governance of the Pastel Network.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **mode** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **subcommand** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **body** | **oas_any_type_not_mapped**|  | |

### Return type

[**Response_Governance_Action_Governance_Post**](../Models/Response_Governance_Action_Governance_Post.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="importAddressImportaddressPost"></a>
# **importAddressImportaddressPost**
> ImportAddressResponse importAddressImportaddressPost(ImportAddressRequest)

Import an address

    Import an address or script (in hex) that can be watched as if it were in your wallet but cannot be used to spend.  ### Description - This endpoint adds an address or script to your wallet as a watch-only address. This means you can see incoming transactions to it, but not spend its funds. - The &#x60;rescan&#x60; option will rescan the wallet for transactions, but this can be time-consuming.  ### Input Parameters - &#x60;address&#x60;: The address to import. - &#x60;label&#x60;: An optional label for the address. - &#x60;rescan&#x60;: A boolean indicating whether to rescan the wallet for transactions. Default is true.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;address\&quot;: \&quot;myaddress\&quot;,     \&quot;label\&quot;: \&quot;testing\&quot;,     \&quot;rescan\&quot;: false } &#x60;&#x60;&#x60;  ### Response - Returns &#x60;null&#x60; on successful addition of the address. In case of an error, an error message is returned.  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Use this endpoint with caution as rescanning can take a considerable amount of time.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ImportAddressRequest** | [**ImportAddressRequest**](../Models/ImportAddressRequest.md)|  | |

### Return type

[**ImportAddressResponse**](../Models/ImportAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="importPrivKeyImportprivkeyPost"></a>
# **importPrivKeyImportprivkeyPost**
> ImportPrivKeyResponse importPrivKeyImportprivkeyPost(zcashprivkey, label, rescan)

Import a private key

    Import a private key into the wallet.  ### Description - Adds a Zcash-format private key to your wallet, allowing the wallet to use funds associated with the key&#39;s address.  ### Input Parameters - &#x60;zcashprivkey&#x60;: The Zcash private key to be imported (required). - &#x60;label&#x60;: An optional label for the address (optional, default empty string). - &#x60;rescan&#x60;: A boolean indicating whether the wallet should be rescanned for transactions after importing the key (optional, default true).  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;zcashprivkey\&quot;: \&quot;mykey\&quot;,     \&quot;label\&quot;: \&quot;testing\&quot;,     \&quot;rescan\&quot;: false } &#x60;&#x60;&#x60;  ### Response - Returns the address associated with the imported private key.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;address\&quot;: \&quot;t1XYZabc123...\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Importing a private key can take minutes if rescan is true.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **zcashprivkey** | **String**|  | [default to null] |
| **label** | **String**|  | [optional] [default to null] |
| **rescan** | **Boolean**|  | [optional] [default to true] |

### Return type

[**ImportPrivKeyResponse**](../Models/ImportPrivKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="importWalletImportwalletPost"></a>
# **importWalletImportwalletPost**
> ImportWalletResponse importWalletImportwalletPost(filename)

Import a wallet from a dump file

    Import taddr keys from a wallet dump file.  ### Description - This endpoint imports taddr keys from a specified wallet dump file. This is useful for restoring a wallet from a backup.  ### Input Parameters - &#x60;filename&#x60;: The path to the wallet dump file to be imported.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;filename\&quot;: \&quot;path/to/exportdir/nameofbackup\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a confirmation message upon successful import.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;message\&quot;: \&quot;Wallet imported successfully\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Ensure that the wallet dump file exists at the specified path before calling this endpoint.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **filename** | **String**|  | [default to null] |

### Return type

[**ImportWalletResponse**](../Models/ImportWalletResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="initializeMasternodeMasternodeInitPost"></a>
# **initializeMasternodeMasternodeInitPost**
> MasternodeInitResponse initializeMasternodeMasternodeInitPost(MasternodeInitRequest)

Initialize masternode

    Initialize masternode with existing outpoint (collateral txid &amp; index).  ### Description - Initializes a masternode with the provided collateral from the local wallet.    Generates new Pastel ID, registers mnid, and generates masternode private key.  ### Input Parameters - &#x60;passphrase&#x60;: Passphrase for new PastelID. - &#x60;txid&#x60;: ID of transaction with the collateral amount. - &#x60;index&#x60;: Index in the transaction with the collateral amount.  ### Request JSON Format &#x60;&#x60;&#x60;json {     \&quot;passphrase\&quot;: \&quot;secure-passphrase\&quot;,     \&quot;txid\&quot;: \&quot;bc1c5243284272dbb22c301a549d112e8bc9bc454b5ff50b1e5f7959d6b56726\&quot;,     \&quot;index\&quot;: 4 } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object with the generated and registered Pastel ID and other key details.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;mnid\&quot;: \&quot;Generated and registered Pastel ID\&quot;,     \&quot;legRoastKey\&quot;: \&quot;Generated and registered LegRoast private key\&quot;,     \&quot;txid\&quot;: \&quot;bc1c5243284272dbb22c301a549d112e8bc9bc454b5ff50b1e5f7959d6b56726\&quot;,     \&quot;outIndex\&quot;: 4,     \&quot;privKey\&quot;: \&quot;Generated masternode private key\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **MasternodeInitRequest** | [**MasternodeInitRequest**](../Models/MasternodeInitRequest.md)|  | |

### Return type

[**MasternodeInitResponse**](../Models/MasternodeInitResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="invalidateBlockInvalidateblockPost"></a>
# **invalidateBlockInvalidateblockPost**
> InvalidateBlockResponse invalidateBlockInvalidateblockPost(block\_hash)

Mark a block as permanently invalid

    Mark a block as permanently invalid, as if it violated a consensus rule.  ### Description - This endpoint marks a specific block in the blockchain as invalid. This operation is irreversible and treats the block as though it has violated a consensus rule.  ### Input Parameters - &#x60;block_hash&#x60;: The hash of the block to mark as invalid.  ### Example Request &#x60;&#x60;&#x60;json POST /invalidateblock {     \&quot;block_hash\&quot;: \&quot;00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object indicating the success or failure of the operation.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;success\&quot;: true,     \&quot;message\&quot;: \&quot;Block marked as invalid\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the block hash is not provided or invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This is a critical operation and should be used with caution. Invalidating a block can have significant implications on the blockchain state.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **block\_hash** | **String**|  | [default to null] |

### Return type

[**InvalidateBlockResponse**](../Models/InvalidateBlockResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="keypoolRefillKeypoolrefillPost"></a>
# **keypoolRefillKeypoolrefillPost**
> oas_any_type_not_mapped keypoolRefillKeypoolrefillPost(KeypoolRefillRequest)

Refill the keypool

    Refill the keypool to the specified size.  ### Description - This endpoint is used to refill the keypool of the wallet to a new size. The keypool keeps a buffer of keys available for use in transactions. Refilling the keypool is important to maintain anonymity and security.  ### Input Parameters - &#x60;newsize&#x60;: (Optional, numeric) The new size for the keypool. Default is 100.  ### Example Request - &#x60;POST /keypoolrefill&#x60; with payload &#x60;{\&quot;newsize\&quot;: 150}&#x60;  ### Response - This method does not return any specific data, but a successful request indicates that the keypool was refilled successfully.  ### Possible Errors - HTTP 400: Bad Request if the newsize parameter is invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - It&#39;s recommended to refill the keypool periodically for operational security and efficiency.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **KeypoolRefillRequest** | [**KeypoolRefillRequest**](../Models/KeypoolRefillRequest.md)|  | |

### Return type

[**oas_any_type_not_mapped**](../Models/AnyType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="listAccountsListaccountsGet"></a>
# **listAccountsListaccountsGet**
> ListAccountsResponse listAccountsListaccountsGet(minconf, includeWatchonly)

List account balances

    List the balances of all accounts in the wallet.  ### Description - Returns a list of accounts with their respective balances. Accounts are identified by their names.  ### Input Parameters - &#x60;minconf&#x60; (optional): Minimum number of confirmations for a transaction to be included. - &#x60;includeWatchonly&#x60; (optional): Include balances in watch-only addresses.  ### Example Request - &#x60;GET /listaccounts?minconf&#x3D;1&amp;includeWatchonly&#x3D;false&#x60;  ### Response - Returns a JSON object containing account names and their balances.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;accounts\&quot;: [         {\&quot;account\&quot;: \&quot;account_name\&quot;, \&quot;balance\&quot;: 123.45},         ...     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **minconf** | [**Minconf_1**](../Models/.md)|  | [optional] [default to 1] |
| **includeWatchonly** | [**Includewatchonly_1**](../Models/.md)|  | [optional] [default to false] |

### Return type

[**ListAccountsResponse**](../Models/ListAccountsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="listAddressAmountsListaddressamountsGet"></a>
# **listAddressAmountsListaddressamountsGet**
> ListAddressAmountsResponse listAddressAmountsListaddressamountsGet(include\_empty, ismine\_filter)

List balance on each address

    List the balance on each address in the wallet.  ### Description - This endpoint lists the balances associated with each address in the wallet. - It allows filtering of addresses based on whether they have a balance and the type of ownership (all, watchOnly, spendableOnly).  ### Input Parameters - &#x60;include_empty&#x60;: (bool, optional, default&#x3D;false) Include addresses with empty balances. - &#x60;ismine_filter&#x60;: (str, optional, default&#x3D;all) Filter for \&quot;all\&quot;, \&quot;watchOnly\&quot;, or \&quot;spendableOnly\&quot; addresses.  ### Example Request - &#x60;GET /listaddressamounts?include_empty&#x3D;true&amp;ismine_filter&#x3D;spendableOnly&#x60;  ### Response - Returns a JSON object with addresses as keys and their corresponding balances as values.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;balances\&quot;: {         \&quot;t1XYZ...abc\&quot;: 0.5,         \&quot;t1ABC...xyz\&quot;: 1.2     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for obtaining an overview of wallet balances distributed across different addresses.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **include\_empty** | [**Include_Empty**](../Models/.md)|  | [optional] [default to false] |
| **ismine\_filter** | [**Ismine_Filter**](../Models/.md)|  | [optional] [default to all] |

### Return type

[**ListAddressAmountsResponse**](../Models/ListAddressAmountsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="listAddressGroupingsListaddressgroupingsGet"></a>
# **listAddressGroupingsListaddressgroupingsGet**
> AddressGroupingsResponse listAddressGroupingsListaddressgroupingsGet()

List groups of addresses with common ownership

    List groups of addresses which have had their common ownership made public by common use as inputs or as the resulting change in past transactions.  ### Description - This endpoint returns groups of addresses that are grouped together based on their common ownership, which is inferred from their usage in past transactions.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Response - Returns a JSON object containing groups of addresses. Each group is a list of addresses, where each address is represented by its Pastel address, the amount associated with it, and optionally the account name.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;groupings\&quot;: [         [             {\&quot;address\&quot;: \&quot;pasteladdress1\&quot;, \&quot;amount\&quot;: 10.5, \&quot;account\&quot;: \&quot;myaccount\&quot;},             {\&quot;address\&quot;: \&quot;pasteladdress2\&quot;, \&quot;amount\&quot;: 2.3}         ],         [             {\&quot;address\&quot;: \&quot;pasteladdress3\&quot;, \&quot;amount\&quot;: 5.0}         ]     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for understanding wallet organization and for tracking common ownership of addresses.

### Parameters
This endpoint does not need any parameter.

### Return type

[**AddressGroupingsResponse**](../Models/AddressGroupingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="listBannedListbannedGet"></a>
# **listBannedListbannedGet**
> ListBannedResponse listBannedListbannedGet()

List all banned IPs/Subnets

    List all banned IPs/Subnets in the network.  ### Description - This endpoint retrieves a list of all IP addresses and subnets that have been banned from the network.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /listbanned&#x60;  ### Response - Returns a JSON array of objects, each containing the banned address and the timestamp until which it is banned.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;banned_addresses\&quot;: [         {             \&quot;address\&quot;: \&quot;192.168.1.0/24\&quot;,             \&quot;banned_until\&quot;: 1625097600         },         {             \&quot;address\&quot;: \&quot;10.0.0.5\&quot;,             \&quot;banned_until\&quot;: 1625098000         }     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is useful for network administrators and developers to audit and manage network access.

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListBannedResponse**](../Models/ListBannedResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="listLockUnspentListlockunspentGet"></a>
# **listLockUnspentListlockunspentGet**
> ListLockUnspentResponse listLockUnspentListlockunspentGet()

List Temporarily Unspendable Outputs

    List all temporarily unspendable outputs.  ### Description - This endpoint returns a list of outputs that are temporarily unspendable.  - Useful for viewing transactions that have been locked using the &#x60;lockunspent&#x60; call.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /listlockunspent&#x60;  ### Response - Returns a JSON array containing objects with &#39;txid&#39; and &#39;vout&#39; fields for each temporarily locked output.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;lock_unspent_outputs\&quot;: [         {             \&quot;txid\&quot;: \&quot;a08e6907dbbd3d809776dbfc5d82e371b764ed838b5655e72f463568df1aadf0\&quot;,             \&quot;vout\&quot;: 1         },         ...     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The &#39;txid&#39; represents the transaction id of the locked output, and &#39;vout&#39; is its output index.

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListLockUnspentResponse**](../Models/ListLockUnspentResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="listMasternodeOutputsMasternodeOutputsGet"></a>
# **listMasternodeOutputsMasternodeOutputsGet**
> MasternodeOutputsResponse listMasternodeOutputsMasternodeOutputsGet()

List masternode outputs

    List masternode outputs (collateral txid+index).  ### Description - This endpoint lists possible coin candidates for masternode collateral,    including transaction ID and index of each output.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /masternode/outputs&#x60;  ### Response - Returns a JSON object containing the masternode outputs.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;outputs\&quot;: {         \&quot;txid1\&quot;: \&quot;index1\&quot;,         \&quot;txid2\&quot;: \&quot;index2\&quot;,         ...     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters
This endpoint does not need any parameter.

### Return type

[**MasternodeOutputsResponse**](../Models/MasternodeOutputsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="listReceivedByAddressListreceivedbyaddressGet"></a>
# **listReceivedByAddressListreceivedbyaddressGet**
> oas_any_type_not_mapped listReceivedByAddressListreceivedbyaddressGet(minconf, includeempty, includeWatchonly)

List balances by receiving address

    List balances by receiving address.  ### Description - This endpoint returns the list of balances associated with each receiving address.  ### Input Parameters - &#x60;minconf&#x60;: The minimum number of confirmations before payments are included. Default is 1. - &#x60;includeempty&#x60;: Whether to include addresses that haven&#39;t received any payments. Default is false. - &#x60;includeWatchonly&#x60;: Whether to include watchonly addresses (see &#39;importaddress&#39;). Default is false.  ### Example Request - &#x60;GET /listreceivedbyaddress?minconf&#x3D;1&amp;includeempty&#x3D;true&amp;includeWatchonly&#x3D;false&#x60;  ### Response - Returns a JSON array with information about each address and its associated balance.  ### Example Response &#x60;&#x60;&#x60;json [     {         \&quot;involvesWatchonly\&quot;: true,         \&quot;address\&quot;: \&quot;receivingaddress\&quot;,         \&quot;account\&quot;: \&quot;accountname\&quot;,         \&quot;amount\&quot;: 1.234,         \&quot;confirmations\&quot;: 5     },     ... ] &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The &#x60;account&#x60; field is deprecated and will be removed in future versions.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **minconf** | [**oas_any_type_not_mapped**](../Models/.md)|  | [optional] [default to 1] |
| **includeempty** | [**oas_any_type_not_mapped**](../Models/.md)|  | [optional] [default to false] |
| **includeWatchonly** | [**oas_any_type_not_mapped**](../Models/.md)|  | [optional] [default to false] |

### Return type

[**oas_any_type_not_mapped**](../Models/AnyType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="listShieldedAddressesZListaddressesGet"></a>
# **listShieldedAddressesZListaddressesGet**
> ListShieldedAddressesResponse listShieldedAddressesZListaddressesGet(include\_watchonly)

List Shielded Addresses

    List all Sapling shielded addresses belonging to the wallet.  ### Description - This endpoint returns a list of Sapling shielded addresses that are owned by the wallet.  - It can optionally include watch-only addresses.  ### Input Parameters - &#x60;include_watchonly&#x60;: (bool, optional, default&#x3D;false) Set to true to include watch-only addresses.  ### Example Request - &#x60;GET /z_listaddresses?include_watchonly&#x3D;true&#x60;  ### Response - Returns a JSON object containing an array of shielded addresses.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;addresses\&quot;: [\&quot;zs1...address1\&quot;, \&quot;zs1...address2\&quot;] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for retrieving all shielded addresses associated with the user&#39;s wallet.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **include\_watchonly** | [**oas_any_type_not_mapped**](../Models/.md)|  | [optional] [default to false] |

### Return type

[**ListShieldedAddressesResponse**](../Models/ListShieldedAddressesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="listSinceBlockListsinceblockPost"></a>
# **listSinceBlockListsinceblockPost**
> ListSinceBlockResponse listSinceBlockListsinceblockPost(ListSinceBlockRequest)

List transactions since a specific block

    List all transactions in blocks since a specified block, or all transactions if no block is specified.  ### Description - This endpoint retrieves all transactions that occurred after a specified block.  - It can be used to update a client with all new transactions if it already knows the old state up to a certain block.  ### Input Parameters - &#x60;blockhash&#x60; (string, optional): The block hash to list transactions since. - &#x60;target_confirmations&#x60; (numeric, optional): The confirmations required, must be 1 or more. - &#x60;include_watchonly&#x60; (bool, optional, default&#x3D;false): Include transactions to watch-only addresses.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;blockhash\&quot;: \&quot;000000000000000bacf66f7497b7dc45ef753ee9a7d38571037cdb1a57f663ad\&quot;,     \&quot;target_confirmations\&quot;: 6,     \&quot;include_watchonly\&quot;: false } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object with an array of transactions since the specified block and the hash of the last block.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;transactions\&quot;: [         {             \&quot;account\&quot;: \&quot;\&quot;,             \&quot;address\&quot;: \&quot;zcashaddress\&quot;,             \&quot;category\&quot;: \&quot;receive\&quot;,             \&quot;amount\&quot;: 10.0,             \&quot;vout\&quot;: 1,             ...         }     ],     \&quot;lastblock\&quot;: \&quot;lastblockhash\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ListSinceBlockRequest** | [**ListSinceBlockRequest**](../Models/ListSinceBlockRequest.md)|  | |

### Return type

[**ListSinceBlockResponse**](../Models/ListSinceBlockResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="listTicketsTicketsListGet"></a>
# **listTicketsTicketsListGet**
> TicketsListResponse listTicketsTicketsListGet(ticket\_type, filter, min\_height)

List tickets of a specific type

    List all tickets of a specific type registered in the system.  ### Description - This endpoint allows querying different types of tickets in the Pastel network, such as PastelID, NFT, and Act tickets.  - It supports various filters to narrow down the results based on specific criteria.  ### Input Parameters - &#x60;ticket_type&#x60;: The type of ticket to list. Example: &#39;id&#39;, &#39;nft&#39;, &#39;act&#39;, etc. - &#x60;filter&#x60;: Optional filter to apply when listing tickets. Example: &#39;all&#39;, &#39;active&#39;, &#39;inactive&#39;, etc. - &#x60;min_height&#x60;: Optional minimum block height for returned tickets.  ### Example Request - &#x60;GET /tickets/list?ticket_type&#x3D;id&amp;filter&#x3D;all&amp;min_height&#x3D;250000&#x60;  ### Response - Returns a JSON object containing a list of tickets as per the requested type and filters.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;tickets\&quot;: [         {             \&quot;ticket_type\&quot;: \&quot;id\&quot;,             \&quot;ticket_details\&quot;: {...}         },         ...     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are incorrect. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The endpoint&#39;s flexibility allows for extensive querying capabilities across different ticket types.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ticket\_type** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **filter** | [**Filter**](../Models/.md)|  | [optional] [default to null] |
| **min\_height** | [**Min_Height**](../Models/.md)|  | [optional] [default to null] |

### Return type

[**TicketsListResponse**](../Models/TicketsListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="listTransactionsListtransactionsGet"></a>
# **listTransactionsListtransactionsGet**
> ListTransactionsResponse listTransactionsListtransactionsGet(ListTransactionsRequest)

List recent transactions

    List up to &#39;count&#39; most recent transactions skipping the first &#39;from&#39; transactions for account &#39;account&#39;.  ### Description - This endpoint returns up to &#39;count&#39; most recent transactions skipping the first &#39;from&#39; transactions for account &#39;account&#39;. - It can include transactions to watch-only addresses if specified.  ### Input Parameters - &#x60;account&#x60;: (Optional) The account name. Should be \&quot;*\&quot;. - &#x60;count&#x60;: (Optional, default&#x3D;10) The number of transactions to return. - &#x60;from&#x60;: (Optional, default&#x3D;0) The number of transactions to skip. - &#x60;include_watch_only&#x60;: (Optional, default&#x3D;false) Include transactions to watchonly addresses.  ### Example Request - &#x60;GET /listtransactions?account&#x3D;*&amp;count&#x3D;20&amp;from&#x3D;100&amp;include_watch_only&#x3D;true&#x60;  ### Response - Returns a list of transaction information.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;transactions\&quot;: [         {             \&quot;account\&quot;: \&quot;...\&quot;,             \&quot;address\&quot;: \&quot;...\&quot;,             \&quot;category\&quot;: \&quot;...\&quot;,             \&quot;amount\&quot;: ...,             \&quot;vout\&quot;: ...,             ...         },         ...     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ListTransactionsRequest** | [**ListTransactionsRequest**](../Models/ListTransactionsRequest.md)|  | |

### Return type

[**ListTransactionsResponse**](../Models/ListTransactionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="listUnspentListunspentGet"></a>
# **listUnspentListunspentGet**
> ListUnspentResponse listUnspentListunspentGet(minconf, maxconf, Addresses)

List Unspent Transaction Outputs

    List unspent transaction outputs (UTXOs) with specified confirmations and optionally filtered by addresses.  ### Description - Returns an array of UTXOs with confirmations between the specified minimum and maximum.  ### Input Parameters - &#x60;minconf&#x60;: (Optional) Minimum number of confirmations. Default is 1. - &#x60;maxconf&#x60;: (Optional) Maximum number of confirmations. Default is 9999999. - &#x60;addresses&#x60;: (Optional) A list of Pastel addresses to filter.  ### Example Request - &#x60;GET /listunspent?minconf&#x3D;1&amp;maxconf&#x3D;9999999&#x60;  ### Response - Returns an array of UTXOs with detailed information about each.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;unspent_transactions\&quot;: [         {             \&quot;txid\&quot;: \&quot;12345\&quot;,             \&quot;vout\&quot;: 0,             \&quot;generated\&quot;: false,             \&quot;address\&quot;: \&quot;PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n\&quot;,             \&quot;account\&quot;: \&quot;account_name\&quot;,             \&quot;scriptPubKey\&quot;: \&quot;76a914...\&quot;,             \&quot;amount\&quot;: 0.0001,             \&quot;confirmations\&quot;: 10,             \&quot;redeemScript\&quot;: \&quot;abcd...\&quot;,             \&quot;spendable\&quot;: true         },         ...     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for wallets and other applications to determine spendable balances.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **minconf** | [**oas_any_type_not_mapped**](../Models/.md)|  | [optional] [default to 1] |
| **maxconf** | [**oas_any_type_not_mapped**](../Models/.md)|  | [optional] [default to 9999999] |
| **Addresses** | [**Addresses**](../Models/Addresses.md)|  | [optional] |

### Return type

[**ListUnspentResponse**](../Models/ListUnspentResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="lockUnspentLockunspentPost"></a>
# **lockUnspentLockunspentPost**
> LockUnspentResponse lockUnspentLockunspentPost(LockUnspentRequest)

Lock or unlock unspent transaction outputs

    Lock or unlock specified transaction outputs.  ### Description - Temporarily lock (unlock&#x3D;false) or unlock (unlock&#x3D;true) specified transaction outputs. - A locked transaction output will not be chosen by automatic coin selection when spending Pastel. - Locks are stored in memory only and are cleared upon node restart.  ### Input Parameters - &#x60;request&#x60;: A JSON object containing the unlock flag and a list of transaction outputs to be locked or unlocked.  ### Request JSON Format &#x60;&#x60;&#x60;json {     \&quot;unlock\&quot;: false,     \&quot;transactions\&quot;: [         {             \&quot;txid\&quot;: \&quot;a08e6907dbbd3d809776dbfc5d82e371b764ed838b5655e72f463568df1aadf0\&quot;,             \&quot;vout\&quot;: 1         }     ] } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object indicating the success of the operation.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;success\&quot;: true } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **LockUnspentRequest** | [**LockUnspentRequest**](../Models/LockUnspentRequest.md)|  | |

### Return type

[**LockUnspentResponse**](../Models/LockUnspentResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="masternodeBroadcastMasternodebroadcastPost"></a>
# **masternodeBroadcastMasternodebroadcastPost**
> MasternodeBroadcastResponse masternodeBroadcastMasternodebroadcastPost(MasternodeBroadcastRequest)

Create and relay masternode broadcast messages

    Set of commands to create and relay masternode broadcast messages.  ### Description - This endpoint is used for creating and relaying masternode broadcast messages. It supports multiple commands for different operations related to masternode broadcasts.  ### Input Parameters - &#x60;command&#x60;: (String) The command to execute. Available commands: create-alias, create-all, decode, relay. - &#x60;parameters&#x60;: (String, Optional) Additional parameters based on the command. - &#x60;fast&#x60;: (Boolean, Optional) If set to true, uses a fast method for the &#39;relay&#39; command.  ### Example Request - &#x60;POST /masternodebroadcast&#x60; with JSON body &#x60;{\&quot;command\&quot;: \&quot;create-alias\&quot;, \&quot;parameters\&quot;: \&quot;aliasName\&quot;}&#x60;  ### Response - Returns a JSON object containing details of the operation based on the command executed.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;overall\&quot;: \&quot;Successfully created broadcast messages for 1 masternodes, failed to create 0, total 1\&quot;,     \&quot;detail\&quot;: [         {             \&quot;outpoint\&quot;: \&quot;0000000000000000000000000000000000000000000000000000000000000000-1\&quot;,             \&quot;addr\&quot;: \&quot;127.0.0.1:9933\&quot;,             \&quot;error_message\&quot;: null         }     ],     \&quot;hex\&quot;: \&quot;0100000000abcdef...\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Depending on the command, the response structure may vary.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **MasternodeBroadcastRequest** | [**MasternodeBroadcastRequest**](../Models/MasternodeBroadcastRequest.md)|  | |

### Return type

[**MasternodeBroadcastResponse**](../Models/MasternodeBroadcastResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="masternodeClearCacheMasternodeClearCachePost"></a>
# **masternodeClearCacheMasternodeClearCachePost**
> MasternodeClearCacheResponse masternodeClearCacheMasternodeClearCachePost(cache\_item)

Clear Masternode Cache Items

    Clear specific Masternode cache items.   ### Description - This endpoint clears specific cache items related to Masternodes in the network. The cache items include the masternode list, seen masternodes, recovery cache, asked masternode cache, and historical top masternodes cache.  ### Input Parameters - &#x60;cache_item&#x60;: A string specifying the cache item to clear. Possible values are &#39;all&#39;, &#39;mns&#39;, &#39;seen&#39;, &#39;recovery&#39;, &#39;asked&#39;, &#39;top-mns&#39;.  ### Example Request - &#x60;POST /masternode/clear-cache&#x60;   &#x60;&#x60;&#x60;json   {       \&quot;cache_item\&quot;: \&quot;mns\&quot;   }   &#x60;&#x60;&#x60;  ### Response - Returns a JSON object indicating the status of the cache clearing operation.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;status\&quot;: \&quot;Cache cleared successfully\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if an invalid cache item is provided. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is primarily used for network maintenance and troubleshooting.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **cache\_item** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |

### Return type

[**MasternodeClearCacheResponse**](../Models/MasternodeClearCacheResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="masternodeMakeConfMasternodeMakeConfPost"></a>
# **masternodeMakeConfMasternodeMakeConfPost**
> MasternodeMakeConfResponse masternodeMakeConfMasternodeMakeConfPost(MasternodeMakeConfRequest)

Create Masternode Configuration

    Create masternode configuration in JSON format.   ### Description - Generates MasterNode Private Key (mnPrivKey) and registers MasterNode PastelID (extKey). - If collateral txid and index are not provided, searches for the first available non-locked outpoint with the correct amount (1000000 PSL).  ### Input Parameters - &#x60;alias&#x60;: Local alias (name) of the Master Node. - &#x60;mn_address&#x60;: The address and port of the Master Node&#39;s cNode. - &#x60;ext_address&#x60;: The address and port of the Master Node&#39;s Storage Layer. - &#x60;ext_p2p&#x60;: The address and port of the Master Node&#39;s Kademlia point. - &#x60;passphrase&#x60;: Passphrase for new Pastel ID. - &#x60;txid&#x60;: (Optional) ID of transaction with the collateral amount. - &#x60;index&#x60;: (Optional) Index in the transaction with the collateral amount.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;alias\&quot;: \&quot;myMN\&quot;,     \&quot;mn_address\&quot;: \&quot;127.0.0.1:9933\&quot;,     \&quot;ext_address\&quot;: \&quot;127.0.0.1:4444\&quot;,     \&quot;ext_p2p\&quot;: \&quot;127.0.0.1:5545\&quot;,     \&quot;passphrase\&quot;: \&quot;securepassphrase\&quot;,     \&quot;txid\&quot;: \&quot;bc1c5243284272dbb22c301a549d112e8bc9bc454b5ff50b1e5f7959d6b56726\&quot;,     \&quot;index\&quot;: 4 } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object with the Masternode configuration details.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;alias\&quot;: \&quot;myMN\&quot;,     \&quot;config\&quot;: {         \&quot;mn_address\&quot;: \&quot;127.0.0.1:9933\&quot;,         \&quot;ext_address\&quot;: \&quot;127.0.0.1:4444\&quot;,         \&quot;ext_p2p\&quot;: \&quot;127.0.0.1:5545\&quot;,         \&quot;txid\&quot;: \&quot;bc1c5243284272dbb22c301a549d112e8bc9bc454b5ff50b1e5f7959d6b56726\&quot;,         \&quot;out_index\&quot;: \&quot;4\&quot;,         \&quot;mn_priv_key\&quot;: \&quot;generatedPrivateKey\&quot;,         \&quot;ext_key\&quot;: \&quot;generatedPastelID\&quot;     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is used for setting up new Masternodes on the network.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **MasternodeMakeConfRequest** | [**MasternodeMakeConfRequest**](../Models/MasternodeMakeConfRequest.md)|  | |

### Return type

[**MasternodeMakeConfResponse**](../Models/MasternodeMakeConfResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="masternodeMessageMasternodeMessagePost"></a>
# **masternodeMessageMasternodeMessagePost**
> MasternodeMessageResponse masternodeMessageMasternodeMessagePost(MasternodeMessageRequest)

Interact with Masternode messages

    Allows sending, listing, printing, and signing messages using Masternode.  ### Description - This endpoint interacts with Masternode messages based on the specified operation.  ### Input Parameters - &#x60;operation&#x60;: The operation to perform (&#x60;send&#x60;, &#x60;list&#x60;, &#x60;print&#x60;, &#x60;sign&#x60;). - &#x60;pub_key&#x60;: The Masternode public key (required for &#x60;send&#x60; operation). - &#x60;message&#x60;: The message text (required for &#x60;send&#x60; and &#x60;sign&#x60; operations). - &#x60;message_id&#x60;: The message ID (required for &#x60;print&#x60; operation). - &#x60;additional_param&#x60;: Additional parameter (optional, used in &#x60;sign&#x60; operation).  ### Example Request - &#x60;POST /masternode/message&#x60;  ### Response - Returns a JSON object containing the result of the operation.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;result\&quot;: \&quot;Success\&quot;,     \&quot;signature\&quot;: \&quot;abc123\&quot;,     \&quot;pubkey\&quot;: \&quot;def456\&quot;,     \&quot;messages\&quot;: {\&quot;msg1\&quot;: \&quot;Message content\&quot;} } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **MasternodeMessageRequest** | [**MasternodeMessageRequest**](../Models/MasternodeMessageRequest.md)|  | |

### Return type

[**MasternodeMessageResponse**](../Models/MasternodeMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="masternodePoseBanScoreMasternodePoseBanScorePost"></a>
# **masternodePoseBanScoreMasternodePoseBanScorePost**
> MasterNodePoseBanScoreResponse masternodePoseBanScoreMasternodePoseBanScorePost(MasterNodePoseBanScoreRequest)

Manage MasterNode PoSe Ban Score

    Manage the Proof-Of-Service (PoSe) ban score for a MasterNode.  ### Description - This endpoint allows getting or incrementing the PoSe ban score of a specified MasterNode. - The MasterNode is identified by the transaction ID (txid) and index of its collateral transaction.  ### Input Parameters - &#x60;command&#x60;: The operation to perform - \&quot;get\&quot; to retrieve the current score or \&quot;increment\&quot; to increase it. - &#x60;txid&#x60;: The transaction ID of the MasterNode&#39;s collateral transaction. - &#x60;index&#x60;: The index of the collateral output in the transaction.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;command\&quot;: \&quot;get\&quot;,     \&quot;txid\&quot;: \&quot;bc1c5243284272dbb22c301a549d112e8bc9bc454b5ff50b1e5f7959d6b56726\&quot;,     \&quot;index\&quot;: 1 } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the MasterNode&#39;s PoSe ban score, ban status, and ban height if applicable.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;txid\&quot;: \&quot;bc1c5243284272dbb22c301a549d112e8bc9bc454b5ff50b1e5f7959d6b56726\&quot;,     \&quot;index\&quot;: 1,     \&quot;pose_ban_score\&quot;: 10,     \&quot;pose_banned\&quot;: false } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **MasterNodePoseBanScoreRequest** | [**MasterNodePoseBanScoreRequest**](../Models/MasterNodePoseBanScoreRequest.md)|  | |

### Return type

[**MasterNodePoseBanScoreResponse**](../Models/MasterNodePoseBanScoreResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="masternodelistMasternodelistGet"></a>
# **masternodelistMasternodelistGet**
> MasternodeListResponse masternodelistMasternodelistGet(mode, filter, allnodes)

Get a list of masternodes in different modes

    Get a list of masternodes in different modes.  ### Description - Retrieves information about masternodes based on the specified mode. Each mode provides different types of data about the masternodes.  ### Input Parameters - &#x60;mode&#x60; (string, optional): The mode to run the list in. Defaults to &#39;status&#39;. Available modes:   - &#x60;activeseconds&#x60;: Number of seconds the masternode has been recognized as enabled.   - &#x60;addr&#x60;: IP address associated with a masternode.   - &#x60;full&#x60;: Info in the format &#39;status protocol payee lastseen activeseconds lastpaidtime lastpaidblock IP&#39;.   - &#x60;info&#x60;: Info in the format &#39;status protocol payee lastseen activeseconds sentinelversion sentinelstate IP&#39;.   - &#x60;lastpaidblock&#x60;: The last block height a node was paid on the network.   - &#x60;lastpaidtime&#x60;: The last time a node was paid on the network.   - &#x60;lastseen&#x60;: Timestamp of when a masternode was last seen on the network.   - &#x60;payee&#x60;: Pastel address associated with a masternode.   - &#x60;protocol&#x60;: Protocol of a masternode.   - &#x60;pubkey&#x60;: Masternode (not collateral) public key.   - &#x60;rank&#x60;: Rank of a masternode based on current block.   - &#x60;status&#x60;: Masternode status (e.g., ENABLED, EXPIRED).   - &#x60;extra&#x60;: PASTEL data associated with the masternode. - &#x60;filter&#x60; (string, optional): Filter results. Partial match by outpoint by default in all modes, additional matches in some modes are also available. - &#x60;allnodes&#x60; (string, optional): Force to show all masternodes including expired NEW_START_REQUIRED.  ### Example Request - &#x60;GET /masternodelist?mode&#x3D;full&amp;filter&#x3D;192.168.0.1&#x60;  ### Response - Depending on the mode, returns a JSON object containing various information about masternodes.  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **mode** | [**oas_any_type_not_mapped**](../Models/.md)|  | [optional] [default to status] |
| **filter** | [**oas_any_type_not_mapped**](../Models/.md)|  | [optional] [default to ] |
| **allnodes** | [**oas_any_type_not_mapped**](../Models/.md)|  | [optional] [default to ] |

### Return type

[**MasternodeListResponse**](../Models/MasternodeListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="moveMovePost"></a>
# **moveMovePost**
> MoveResponse moveMovePost(MoveRequest)

Move amount from one account to another

    Move a specified amount from one account in your wallet to another.  ### Description - **DEPRECATED**: This method is deprecated. However, it is still available for use. - Moves a specified amount from one account in your wallet to another. It is a local operation and does not involve a transaction on the blockchain.  ### Input Parameters - &#x60;fromaccount&#x60;: (string, required) The account to move funds from. Must be set to the empty string \&quot;\&quot; to represent the default account. - &#x60;toaccount&#x60;: (string, required) The account to move funds to. Must be set to the empty string \&quot;\&quot; to represent the default account. - &#x60;amount&#x60;: (numeric, required) The quantity of currency to move between accounts. - &#x60;minconf&#x60;: (numeric, optional, default&#x3D;1) The minimum number of confirmations for used funds. - &#x60;comment&#x60;: (string, optional) An optional comment, stored in the wallet only.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;fromaccount\&quot;: \&quot;\&quot;,     \&quot;toaccount\&quot;: \&quot;tabby\&quot;,     \&quot;amount\&quot;: 0.01,     \&quot;minconf\&quot;: 1,     \&quot;comment\&quot;: \&quot;Transfer to tabby\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a boolean indicating if the operation was successful.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;success\&quot;: true } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This method is deprecated and might be removed in future versions.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **MoveRequest** | [**MoveRequest**](../Models/MoveRequest.md)|  | |

### Return type

[**MoveResponse**](../Models/MoveResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="pastelidNewkeyPastelidNewkeyPost"></a>
# **pastelidNewkeyPastelidNewkeyPost**
> PastelIDNewKeyResponse pastelidNewkeyPastelidNewkeyPost(PastelIDNewKeyRequest)

Generate new Pastel ID and associated keys

    Generate a new Pastel ID and associated keys (EdDSA448) and LegRoast signing keys.  ### Description - This endpoint generates a new Pastel ID, which is a unique identifier for a user or entity on the Pastel network. - The endpoint also generates associated cryptographic keys using EdDSA448 and LegRoast algorithms. - The generated Pastel ID is base58-encoded.  ### Input Parameters - &#x60;passphrase&#x60;: A passphrase used for generating the new key. It cannot be empty.  ### Example Request - &#x60;POST /pastelid_newkey&#x60; with JSON body &#x60;{\&quot;passphrase\&quot;: \&quot;your_passphrase\&quot;}&#x60;  ### Response - Returns a JSON object containing the newly generated Pastel ID and LegRoast key.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;pastelid\&quot;: \&quot;base58EncodedPastelID\&quot;,     \&quot;legroast\&quot;: \&quot;base58EncodedLegRoastKey\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the passphrase is empty or invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This function is essential for user registration and identity management within the Pastel network.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **PastelIDNewKeyRequest** | [**PastelIDNewKeyRequest**](../Models/PastelIDNewKeyRequest.md)|  | |

### Return type

[**PastelIDNewKeyResponse**](../Models/PastelIDNewKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="pastelidPasswdPastelidPasswdPost"></a>
# **pastelidPasswdPastelidPasswdPost**
> PastelIDPasswdResponse pastelidPasswdPastelidPasswdPost(PastelIDPasswdRequest)

Change passphrase for PastelID secure container

    Change the passphrase used to encrypt the secure container associated with the PastelID.  ### Description - This endpoint is used to update the passphrase of the secure container for a given PastelID. - The secure container is encrypted, and this operation changes its encryption passphrase.  ### Input Parameters - &#x60;pastelid&#x60;: The PastelID for which the passphrase needs to be changed. - &#x60;old_passphrase&#x60;: The current passphrase of the secure container. - &#x60;new_passphrase&#x60;: The new passphrase to set for the secure container.  ### Example Request &#x60;&#x60;&#x60;json POST /pastelid/passwd {     \&quot;pastelid\&quot;: \&quot;jX9NfXhvnUJwDzB2z0wh\&quot;,     \&quot;old_passphrase\&quot;: \&quot;currentpass\&quot;,     \&quot;new_passphrase\&quot;: \&quot;newpass\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object indicating the success of the operation.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;result\&quot;: \&quot;success\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid or missing. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **PastelIDPasswdRequest** | [**PastelIDPasswdRequest**](../Models/PastelIDPasswdRequest.md)|  | |

### Return type

[**PastelIDPasswdResponse**](../Models/PastelIDPasswdResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="pastelidSignFilePastelidSignfilePost"></a>
# **pastelidSignFilePastelidSignfilePost**
> PastelIDSignFileResponse pastelidSignFilePastelidSignfilePost(PastelIDSignFileRequest)

Sign a file with a Pastel ID

    Sign a file with the internally stored private key associated with a Pastel ID.  ### Description - This endpoint allows users to sign a file using their Pastel ID. The file is specified by its path, and the signature is generated using the private key associated with the given Pastel ID. - Supported algorithms are &#39;ed448&#39; (default) and &#39;legroast&#39;.  ### Input Parameters - &#x60;file_path&#x60;: Path to the file that needs to be signed. - &#x60;pastel_id&#x60;: The Pastel ID to use for signing. - &#x60;passphrase&#x60;: The passphrase for the private key. - &#x60;algorithm&#x60;: (Optional) The algorithm to use for signing, either &#39;ed448&#39; or &#39;legroast&#39;.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;file_path\&quot;: \&quot;/path/to/file\&quot;,     \&quot;pastel_id\&quot;: \&quot;jXYWV...\&quot;,     \&quot;passphrase\&quot;: \&quot;your_passphrase\&quot;,     \&quot;algorithm\&quot;: \&quot;ed448\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the signature of the file.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;signature\&quot;: \&quot;HJG98uFomw...\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The private key must be stored internally and associated with the specified Pastel ID.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **PastelIDSignFileRequest** | [**PastelIDSignFileRequest**](../Models/PastelIDSignFileRequest.md)|  | |

### Return type

[**PastelIDSignFileResponse**](../Models/PastelIDSignFileResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="pastelidVerifyFilePastelidVerifyFilePost"></a>
# **pastelidVerifyFilePastelidVerifyFilePost**
> PastelIDVerifyFileResponse pastelidVerifyFilePastelidVerifyFilePost(file\_path, signature, pastelid, algorithm)

Verify a file&#39;s signature with a Pastel ID

    Verify a file&#39;s signature with the private key associated with a Pastel ID.  ### Description - This endpoint verifies the signature of a file using a Pastel ID. It supports two algorithms: ed448 or legroast.  ### Input Parameters - &#x60;file_path&#x60;: Path to the file whose signature needs to be verified. - &#x60;signature&#x60;: The signature string to verify. - &#x60;pastelid&#x60;: The Pastel ID associated with the private key. - &#x60;algorithm&#x60;: (Optional) The algorithm used for signing (ed448 or legroast). Default is ed448.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;file_path\&quot;: \&quot;/path/to/file\&quot;,     \&quot;signature\&quot;: \&quot;signature_string\&quot;,     \&quot;pastelid\&quot;: \&quot;pastel_id_string\&quot;,     \&quot;algorithm\&quot;: \&quot;ed448\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object indicating whether the verification was successful or failed.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;verification\&quot;: \&quot;OK\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if input parameters are missing or invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Used for validating the authenticity of a file using a Pastel ID.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **file\_path** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **signature** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **pastelid** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **algorithm** | [**Algorithm**](../Models/.md)|  | [optional] [default to ed448] |

### Return type

[**PastelIDVerifyFileResponse**](../Models/PastelIDVerifyFileResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="pastelidVerifyPastelidVerifyPost"></a>
# **pastelidVerifyPastelidVerifyPost**
> PastelIDVerifyResponse pastelidVerifyPastelidVerifyPost(PastelIDVerifyRequest)

Verify a signature with PastelID

    Verify a text&#39;s signature using the private key associated with the PastelID.  ### Description - This endpoint verifies the signature of a given text using the private key associated with a specified PastelID. - It supports two algorithms: &#x60;ed448&#x60; and &#x60;legroast&#x60;.  ### Input Parameters - &#x60;text&#x60;: The text (or base64-encoded text) to be verified. - &#x60;signature&#x60;: The signature of the text. - &#x60;pastelid&#x60;: The PastelID used for verification. - &#x60;algorithm&#x60;: (Optional) The algorithm used for signing (&#x60;ed448&#x60; or &#x60;legroast&#x60;). Default is &#x60;ed448&#x60;.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;text\&quot;: \&quot;Hello World\&quot;,     \&quot;signature\&quot;: \&quot;signature123\&quot;,     \&quot;pastelid\&quot;: \&quot;pastelid123\&quot;,     \&quot;algorithm\&quot;: \&quot;ed448\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object indicating whether the verification was successful or not.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;verification\&quot;: \&quot;OK\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Verification failure does not always imply the data or signature is incorrect; it might also indicate an issue with the algorithm used.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **PastelIDVerifyRequest** | [**PastelIDVerifyRequest**](../Models/PastelIDVerifyRequest.md)|  | |

### Return type

[**PastelIDVerifyResponse**](../Models/PastelIDVerifyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="pingPingGet"></a>
# **pingPingGet**
> PingResponse pingPingGet()

Send a ping to all nodes

    Request a ping to be sent to all other nodes, measuring ping time.  ### Description - This endpoint triggers a ping to all nodes in the network. It&#39;s used to measure the ping time and network responsiveness. - The ping time and wait time results are available in the &#x60;getpeerinfo&#x60; response, under &#x60;pingtime&#x60; and &#x60;pingwait&#x60; fields, represented in decimal seconds. - The ping command is queued with other commands, so it measures the total processing backlog, not just the network latency.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /ping&#x60;  ### Response - Returns a JSON object indicating whether the ping request was successfully queued.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;success\&quot;: true } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for network diagnostics and monitoring the responsiveness of the network.

### Parameters
This endpoint does not need any parameter.

### Return type

[**PingResponse**](../Models/PingResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="prioritiseTransactionPrioritisetransactionPost"></a>
# **prioritiseTransactionPrioritisetransactionPost**
> PrioritiseTransactionResponse prioritiseTransactionPrioritisetransactionPost(PrioritiseTransactionRequest)

Prioritise a transaction for mining

    Accepts the transaction into mined blocks at a higher (or lower) priority.  ### Description - This endpoint allows modifying the priority of a transaction in the mining queue. - It is useful for influencing the selection algorithm for transaction inclusion in upcoming blocks.  ### Input Parameters - &#x60;txid&#x60; (str): The transaction ID to be prioritised. - &#x60;priority_delta&#x60; (float): The priority to add or subtract. This alters how the transaction selection algorithm views the transaction&#39;s priority. - &#x60;fee_delta&#x60; (int): The fee value in patoshis to add (or subtract, if negative). It&#39;s a virtual change, affecting only the selection algorithm, not the actual transaction fee.  ### Example Request &#x60;&#x60;&#x60;json POST /prioritisetransaction Content-Type: application/json  {     \&quot;txid\&quot;: \&quot;123abc\&quot;,     \&quot;priority_delta\&quot;: 0.0,     \&quot;fee_delta\&quot;: 10000 } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object indicating whether the operation was successful.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;result\&quot;: true } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is particularly relevant for miners and services that require transaction prioritisation.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **PrioritiseTransactionRequest** | [**PrioritiseTransactionRequest**](../Models/PrioritiseTransactionRequest.md)|  | |

### Return type

[**PrioritiseTransactionResponse**](../Models/PrioritiseTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="reconsiderBlockReconsiderblockPost"></a>
# **reconsiderBlockReconsiderblockPost**
> ReconsiderBlockResponse reconsiderBlockReconsiderblockPost(ReconsiderBlockRequest)

Reconsider a previously invalidated block

    Removes invalidity status of a block and its descendants, reconsider them for activation.  ### Description - This endpoint is used to undo the effects of &#x60;invalidateblock&#x60;. - It reconsiders a block that was previously marked as invalid along with all its descendants.  ### Input Parameters - &#x60;hash&#x60;: (string, required) The hash of the block to reconsider.  ### Example Request - &#x60;POST /reconsiderblock {\&quot;hash\&quot;: \&quot;blockhash\&quot;}&#x60;  ### Response - Returns a JSON object indicating the success or failure of the operation.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;success\&quot;: true,     \&quot;message\&quot;: \&quot;Block and its descendants reconsidered successfully\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the block hash is invalid or missing. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Use this method with caution as it affects the blockchain state.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ReconsiderBlockRequest** | [**ReconsiderBlockRequest**](../Models/ReconsiderBlockRequest.md)|  | |

### Return type

[**ReconsiderBlockResponse**](../Models/ReconsiderBlockResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="refreshMiningMnidInfoRefreshminingmnidinfoGet"></a>
# **refreshMiningMnidInfoRefreshminingmnidinfoGet**
> RefreshMiningMnidInfoResponse refreshMiningMnidInfoRefreshminingmnidinfoGet()

Refresh mining MNID information

    Refreshes the mining information (MNIDs) from the pastel.conf file.  ### Description - This endpoint refreshes the list of Masternode IDs (MNIDs) used for mining, as specified in the pastel.conf file. It is useful for updating the mining configuration without restarting the node.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /refreshminingmnidinfo&#x60;  ### Response - Returns a JSON array containing the list of refreshed MNIDs.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;mnids\&quot;: [\&quot;mnid1\&quot;, \&quot;mnid2\&quot;, \&quot;mnid3\&quot;] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in refreshing the MNID information.  ### Note - This endpoint is particularly useful for miners who need to update their Masternode IDs dynamically.

### Parameters
This endpoint does not need any parameter.

### Return type

[**RefreshMiningMnidInfoResponse**](../Models/RefreshMiningMnidInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="registerActionTicketTicketsRegisterActionPost"></a>
# **registerActionTicketTicketsRegisterActionPost**
> ActionTicketResponse registerActionTicketTicketsRegisterActionPost(ActionTicketRequest)

Register new Action ticket

    Register a new Action ticket on the Pastel blockchain.  ### Description - This endpoint is used to register a new Action ticket, supporting action types like &#39;sense&#39; and &#39;cascade&#39;. - The ticket includes details like action type, caller PastelID, block number, and application-specific data.  ### Input Parameters - &#x60;action_ticket&#x60;: Base64 encoded Action ticket. - &#x60;signatures&#x60;: Signatures and Pastel IDs of the principal and verifying masternodes. - &#x60;pastelid&#x60;: The Pastel ID of the registering masternode. - &#x60;passphrase&#x60;: The passphrase to the private key associated with Pastel ID. - &#x60;label&#x60;: A label for the ticket. - &#x60;fee&#x60;: The storage fee. - &#x60;address&#x60;: (Optional) Pastel blockchain t-address for funding.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;action_ticket\&quot;: \&quot;&lt;encoded-ticket&gt;\&quot;,     \&quot;signatures\&quot;: \&quot;&lt;signatures-json&gt;\&quot;,     \&quot;pastelid\&quot;: \&quot;jXYqZNPj...\&quot;,     \&quot;passphrase\&quot;: \&quot;passphrase\&quot;,     \&quot;label\&quot;: \&quot;label\&quot;,     \&quot;fee\&quot;: 100,     \&quot;address\&quot;: \&quot;P_address\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns information about the registered Action ticket including transaction ID, height, and ticket details.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;txid\&quot;: \&quot;transaction_id\&quot;,     \&quot;height\&quot;: 123456,     \&quot;ticket\&quot;: {         // Ticket details     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ActionTicketRequest** | [**ActionTicketRequest**](../Models/ActionTicketRequest.md)|  | |

### Return type

[**ActionTicketResponse**](../Models/ActionTicketResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="registerNftTicketTicketsRegisterNftPost"></a>
# **registerNftTicketTicketsRegisterNftPost**
> RegisterNFTTicketResponse registerNftTicketTicketsRegisterNftPost(RegisterNFTTicketRequest)

Register a new NFT ticket

    Register a new NFT ticket in the Pastel blockchain.  ### Description - This endpoint registers a new NFT ticket on the Pastel blockchain. It requires authentication via Pastel ID and passphrase.  ### Input Parameters - &#x60;nft_ticket&#x60;: Base64 encoded NFT ticket created by the creator. - &#x60;signatures&#x60;: Signatures and Pastel IDs of the principal and verifying masternodes. - &#x60;pastelid&#x60;: The registering masternode&#39;s Pastel ID. - &#x60;passphrase&#x60;: Passphrase for the Pastel ID private key. - &#x60;label&#x60;: Label for the ticket. - &#x60;fee&#x60;: Storage fee for the NFT registration. - &#x60;address&#x60;: (Optional) Pastel blockchain t-address for funding the registration.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;nft_ticket\&quot;: \&quot;base64-encoded-ticket\&quot;,     \&quot;signatures\&quot;: \&quot;signatures-json\&quot;,     \&quot;pastelid\&quot;: \&quot;jXYqZNPj21RVnwxnEJ654wEdzi7GZTZ5LAdiotBmPrF7pDMkpX1JegDMQZX55WZLkvy9fxNpZcbBJuE8QYUqBF\&quot;,     \&quot;passphrase\&quot;: \&quot;passphrase\&quot;,     \&quot;label\&quot;: \&quot;My NFT\&quot;,     \&quot;fee\&quot;: 100,     \&quot;address\&quot;: \&quot;optional-address\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object with the transaction ID and ticket information.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;txid\&quot;: \&quot;transaction-id\&quot;,     \&quot;height\&quot;: 123456,     \&quot;ticket\&quot;: {         \&quot;type\&quot;: \&quot;nft-reg\&quot;,         \&quot;nft_ticket\&quot;: {},         ...     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Used for registering new NFTs on the blockchain.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **RegisterNFTTicketRequest** | [**RegisterNFTTicketRequest**](../Models/RegisterNFTTicketRequest.md)|  | |

### Return type

[**RegisterNFTTicketResponse**](../Models/RegisterNFTTicketResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="registerRoyaltyTicketTicketsRegisterRoyaltyPost"></a>
# **registerRoyaltyTicketTicketsRegisterRoyaltyPost**
> RegisterRoyaltyTicketResponse registerRoyaltyTicketTicketsRegisterRoyaltyPost(RegisterRoyaltyTicketRequest)

Register new change payee of the NFT royalty ticket

    Register a new change payee of the NFT royalty ticket. If successful, the method returns the transaction ID.  ### Description - This endpoint registers a new recipient for NFT royalty payments, effectively changing the payee. - It requires the transaction ID of the NFT register ticket, PastelIDs of the new and current royalty recipients, and the passphrase for the old PastelID.  ### Input Parameters - &#x60;nft_txid&#x60; (string, required): The txid of the NFT register ticket. - &#x60;new_pastelid&#x60; (string, required): The PastelID of the new royalty recipient. - &#x60;old_pastelid&#x60; (string, required): The PastelID of the current royalty recipient. - &#x60;passphrase&#x60; (string, required): The passphrase to the private key associated with &#39;old-pastelid&#39;. - &#x60;address&#x60; (string, optional): The Pastel blockchain t-address for funding the registration.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;nft_txid\&quot;: \&quot;907e5e4c6fc4d14660a22afe2bdf6d27a3c8762abf0a89355bb19b7d9e7dc440\&quot;,     \&quot;new_pastelid\&quot;: \&quot;newPastelID123\&quot;,     \&quot;old_pastelid\&quot;: \&quot;oldPastelID456\&quot;,     \&quot;passphrase\&quot;: \&quot;yourPassphrase\&quot;,     \&quot;address\&quot;: \&quot;P_address\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the details of the registered NFT royalty ticket.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;txid\&quot;: \&quot;generatedTxId\&quot;,     \&quot;height\&quot;: 123456,     \&quot;ticket\&quot;: {         \&quot;type\&quot;: \&quot;nft-royalty\&quot;,         \&quot;version\&quot;: 1,         \&quot;pastelID\&quot;: \&quot;oldPastelID456\&quot;,         \&quot;new_pastelID\&quot;: \&quot;newPastelID123\&quot;,         \&quot;nft_txid\&quot;: \&quot;907e5e4c6fc4d14660a22afe2bdf6d27a3c8762abf0a89355bb19b7d9e7dc440\&quot;,         \&quot;signature\&quot;: \&quot;signatureString\&quot;     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **RegisterRoyaltyTicketRequest** | [**RegisterRoyaltyTicketRequest**](../Models/RegisterRoyaltyTicketRequest.md)|  | |

### Return type

[**RegisterRoyaltyTicketResponse**](../Models/RegisterRoyaltyTicketResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="registerTransferTicketTicketsRegisterTransferPost"></a>
# **registerTransferTicketTicketsRegisterTransferPost**
> RegisterTransferTicketResponse registerTransferTicketTicketsRegisterTransferPost(RegisterTransferTicketRequest)

Register a transfer ticket

    Register a transfer ticket in the Pastel network.  ### Description - This endpoint registers a Transfer ticket, completing the transfer of an NFT from one owner to another in a secure manner.  ### Input Parameters - &#x60;offer_txid&#x60;: The transaction ID of the Offer ticket. - &#x60;accept_txid&#x60;: The transaction ID of the Accept ticket. - &#x60;pastel_id&#x60;: The Pastel ID of the new owner. Must match the Pastel ID used to sign the Accept ticket. - &#x60;passphrase&#x60;: Passphrase of the private key associated with the new owner&#39;s Pastel ID. - &#x60;address&#x60;: (Optional) The Pastel blockchain t-address to use for funding the registration.  ### Request JSON Format &#x60;&#x60;&#x60;json {     \&quot;offer_txid\&quot;: \&quot;offer_transaction_id\&quot;,     \&quot;accept_txid\&quot;: \&quot;accept_transaction_id\&quot;,     \&quot;pastel_id\&quot;: \&quot;new_owner_pastel_id\&quot;,     \&quot;passphrase\&quot;: \&quot;private_key_passphrase\&quot;,     \&quot;address\&quot;: \&quot;funding_t_address\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing details of the registered transfer ticket.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;ticket\&quot;: {         \&quot;type\&quot;: \&quot;transfer\&quot;,         \&quot;pastelID\&quot;: \&quot;new_owner_pastel_id\&quot;,         \&quot;offer_txid\&quot;: \&quot;offer_transaction_id\&quot;,         \&quot;accept_txid\&quot;: \&quot;accept_transaction_id\&quot;,         \&quot;item_txid\&quot;: \&quot;item_transaction_id\&quot;,         \&quot;registration_txid\&quot;: \&quot;registration_transaction_id\&quot;,         \&quot;signature\&quot;: \&quot;signature_value\&quot;     },     \&quot;height\&quot;: \&quot;block_height\&quot;,     \&quot;txid\&quot;: \&quot;transaction_id\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is used to securely transfer ownership of NFTs within the Pastel network.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **RegisterTransferTicketRequest** | [**RegisterTransferTicketRequest**](../Models/RegisterTransferTicketRequest.md)|  | |

### Return type

[**RegisterTransferTicketResponse**](../Models/RegisterTransferTicketResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="registerUsernameTicketsRegisterUsernamePost"></a>
# **registerUsernameTicketsRegisterUsernamePost**
> RegisterUsernameResponse registerUsernameTicketsRegisterUsernamePost(RegisterUsernameRequest)

Register a Username Change Request ticket

    Register a Username Change Request ticket with the specified username and Pastel ID.  ### Description - This endpoint registers a new username change request ticket in the Pastel network. - The Pastel ID must already exist and be stored in the node.  ### Input Parameters - &#x60;username&#x60;: The username to be associated with the specified Pastel ID. - &#x60;pastel_id&#x60;: The Pastel ID with which the username is to be associated. - &#x60;passphrase&#x60;: The passphrase to access the private key associated with the Pastel ID. - &#x60;address&#x60;: (Optional) The Pastel blockchain address to fund the registration.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;username\&quot;: \&quot;example_user\&quot;,     \&quot;pastel_id\&quot;: \&quot;jXYqZNPj21RVnwxnEJ654wEdzi7GZTZ5LAdiotBmPrF7pDMkpX1JegDMQZX55WZLkvy9fxNpZcbBJuE8QYUqBF\&quot;,     \&quot;passphrase\&quot;: \&quot;passphrase\&quot;,     \&quot;address\&quot;: \&quot;P_address\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing details of the username registration ticket, including the transaction ID.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;ticket\&quot;: {         \&quot;type\&quot;: \&quot;username\&quot;,         \&quot;pastelID\&quot;: \&quot;jXYqZNPj21RVnwxnEJ654wEdzi7GZTZ5LAdiotBmPrF7pDMkpX1JegDMQZX55WZLkvy9fxNpZcbBJuE8QYUqBF\&quot;,         \&quot;username\&quot;: \&quot;example_user\&quot;,         \&quot;fee\&quot;: \&quot;0.01\&quot;,         \&quot;signature\&quot;: \&quot;...\&quot;     },     \&quot;height\&quot;: \&quot;123456\&quot;,     \&quot;txid\&quot;: \&quot;abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is crucial for users who wish to change their username associated with their Pastel ID.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **RegisterUsernameRequest** | [**RegisterUsernameRequest**](../Models/RegisterUsernameRequest.md)|  | |

### Return type

[**RegisterUsernameResponse**](../Models/RegisterUsernameResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="resendWalletTransactionsResendwallettransactionsPost"></a>
# **resendWalletTransactionsResendwallettransactionsPost**
> ResendWalletTransactionsResponse resendWalletTransactionsResendwallettransactionsPost()

Re-broadcast unconfirmed wallet transactions

    Immediately re-broadcast unconfirmed wallet transactions to all peers.  ### Description - This endpoint is intended primarily for testing. It forces the immediate re-broadcast of unconfirmed transactions from the wallet to all peers. - The wallet code periodically re-broadcasts transactions automatically, so this method is typically unnecessary in production environments.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;POST /resendwallettransactions&#x60;  ### Response - Returns a JSON object containing an array of transaction IDs that were re-broadcast.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;transaction_ids\&quot;: [\&quot;txid1\&quot;, \&quot;txid2\&quot;, \&quot;txid3\&quot;] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Use this method with caution, as it is primarily for testing purposes and may affect network performance if used excessively.

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResendWalletTransactionsResponse**](../Models/ResendWalletTransactionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="retrieveChaindataChaindataRetrievePost"></a>
# **retrieveChaindataChaindataRetrievePost**
> ChaindataRetrieveResponse retrieveChaindataChaindataRetrievePost(ChaindataRetrieveRequest)

Retrieve data from the blockchain

    Retrieve data from the blockchain by transaction ID (&#x60;txid&#x60;).  ### Description - This endpoint retrieves data from the blockchain that was stored using the &#39;store&#39; command and associated with the provided &#x60;txid&#x60;.  ### Input Parameters - &#x60;txid&#x60;: The transaction ID of the data to be retrieved.  ### Example Request - &#x60;POST /chaindata/retrieve&#x60; with JSON payload &#x60;{\&quot;txid\&quot;: \&quot;example-txid\&quot;}&#x60;  ### Response - Returns a JSON object containing the retrieved data.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;data\&quot;: \&quot;retrieved data\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the &#x60;txid&#x60; is not provided or is invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ChaindataRetrieveRequest** | [**ChaindataRetrieveRequest**](../Models/ChaindataRetrieveRequest.md)|  | |

### Return type

[**ChaindataRetrieveResponse**](../Models/ChaindataRetrieveResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="scanForMissingTxsScanformissingtxsPost"></a>
# **scanForMissingTxsScanformissingtxsPost**
> ScanForMissingTxsResponse scanForMissingTxsScanformissingtxsPost(ScanForMissingTxsRequest)

Scan for missing transactions

    Scan the wallet for missing transactions starting from a specified block height.  ### Description - This endpoint scans the wallet for transactions that might be missing, starting from a given block height. It helps in ensuring the wallet&#39;s transaction history is complete and up-to-date.  ### Input Parameters - &#x60;starting_height&#x60;: (numeric, required) The block height from which to start scanning for missing transactions.  ### Example Request - &#x60;POST /scanformissingtxs&#x60; with payload &#x60;{\&quot;starting_height\&quot;: 100000}&#x60;  ### Response - Returns a JSON object containing a list of transaction IDs for transactions that are missing in the wallet.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;missing_txs\&quot;: [         \&quot;missing_transaction1_txid\&quot;,         \&quot;missing_transaction2_txid\&quot;         // ... more transaction IDs ...     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the &#x60;starting_height&#x60; is invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for wallet recovery and maintenance purposes.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ScanForMissingTxsRequest** | [**ScanForMissingTxsRequest**](../Models/ScanForMissingTxsRequest.md)|  | |

### Return type

[**ScanForMissingTxsResponse**](../Models/ScanForMissingTxsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="sendFromSendfromPost"></a>
# **sendFromSendfromPost**
> SendFromResponse sendFromSendfromPost(fromaccount, tozcashaddress, amount, minconf, comment, comment\_to)

Send amount from an account to a Pastel address

    Send an amount from an account to a specified Pastel address.                ### Description - This endpoint is a deprecated method (use sendtoaddress) for sending an amount from an account to a Pastel address. The amount is a real number and is rounded to the nearest 0.00000001.  ### Input Parameters - &#x60;fromaccount&#x60;: (string, required) Must be set to the empty string \&quot;\&quot; to represent the default account. Any other string will result in an error. - &#x60;tozcashaddress&#x60;: (string, required) The Pastel address to send funds to. - &#x60;amount&#x60;: (numeric, required) The amount in PSL. - &#x60;minconf&#x60;: (numeric, optional, default&#x3D;1) Only use funds with at least this many confirmations. - &#x60;comment&#x60;: (string, optional) A comment for the transaction, stored in your wallet. - &#x60;comment_to&#x60;: (string, optional) A comment to store the name of the person/organization to which you&#39;re sending the transaction, stored in your wallet.  ### Request JSON Format &#x60;&#x60;&#x60;json {     \&quot;fromaccount\&quot;: \&quot;\&quot;,     \&quot;tozcashaddress\&quot;: \&quot;PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n\&quot;,     \&quot;amount\&quot;: 0.01,     \&quot;minconf\&quot;: 1,     \&quot;comment\&quot;: \&quot;donation\&quot;,     \&quot;comment_to\&quot;: \&quot;seans outpost\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the transaction ID.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;transaction_id\&quot;: \&quot;transactionid1234567890\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Invalid request parameters. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - It&#39;s recommended to use &#x60;sendtoaddress&#x60; instead of this deprecated method.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fromaccount** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **tozcashaddress** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **amount** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **minconf** | [**Minconf_1**](../Models/.md)|  | [optional] [default to 1] |
| **comment** | [**Comment**](../Models/.md)|  | [optional] [default to null] |
| **comment\_to** | [**Comment_To**](../Models/.md)|  | [optional] [default to null] |

### Return type

[**SendFromResponse**](../Models/SendFromResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="sendManySendmanyPost"></a>
# **sendManySendmanyPost**
> SendManyResponse sendManySendmanyPost(SendManyRequest)

Send multiple transactions

    Send multiple times. Amounts are decimal numbers with at most 8 digits of precision.  ### Description - This endpoint sends multiple transactions to multiple addresses.  ### Input Parameters - &#x60;from_account&#x60;: MUST be set to the empty string \&quot;\&quot; to represent the default account. Any other string will result in an error. - &#x60;amounts&#x60;: A JSON object with addresses and amounts. - &#x60;min_conf&#x60;: Optional, minimum number of confirmations. Default is 1. - &#x60;comment&#x60;: Optional, a comment for the transaction. - &#x60;subtract_fee_from_amount&#x60;: Optional, a list of addresses from which the fee will be subtracted. - &#x60;change_address&#x60;: Optional, the destination address for the change. Can be \&quot;original\&quot;, \&quot;new\&quot;, or a specific Pastel t-address.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;from_account\&quot;: \&quot;\&quot;,     \&quot;amounts\&quot;: {         \&quot;PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n\&quot;: 0.01     },     \&quot;min_conf\&quot;: 1,     \&quot;comment\&quot;: \&quot;Test transaction\&quot;,     \&quot;subtract_fee_from_amount\&quot;: [\&quot;PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n\&quot;],     \&quot;change_address\&quot;: \&quot;original\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the transaction ID.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;transaction_id\&quot;: \&quot;transaction_id_here\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **SendManyRequest** | [**SendManyRequest**](../Models/SendManyRequest.md)|  | |

### Return type

[**SendManyResponse**](../Models/SendManyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="sendRawTransactionSendrawtransactionPost"></a>
# **sendRawTransactionSendrawtransactionPost**
> SendRawTransactionResponse sendRawTransactionSendrawtransactionPost(SendRawTransactionRequest)

Submit a raw transaction to the network

    Submit a raw transaction (serialized, hex-encoded) to the local node and network.  ### Description - This endpoint is used to submit a serialized, hex-encoded transaction to the network. - It can be used in combination with &#x60;createrawtransaction&#x60; and &#x60;signrawtransaction&#x60; calls.  ### Input Parameters - &#x60;hexstring&#x60; (string, required): The hex string of the raw transaction. - &#x60;allowhighfees&#x60; (boolean, optional, default&#x3D;false): Allow high fees.  ### Example Request - &#x60;POST /sendrawtransaction&#x60; with JSON body:  &#x60;&#x60;&#x60;json {     \&quot;hexstring\&quot;: \&quot;signedhex\&quot;,     \&quot;allowhighfees\&quot;: false } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the transaction hash.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;tx_hash\&quot;: \&quot;transactionhashinhex\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **SendRawTransactionRequest** | [**SendRawTransactionRequest**](../Models/SendRawTransactionRequest.md)|  | |

### Return type

[**SendRawTransactionResponse**](../Models/SendRawTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="sendToAddressSendtoaddressPost"></a>
# **sendToAddressSendtoaddressPost**
> SendToAddressResponse sendToAddressSendtoaddressPost(SendToAddressRequest)

Send an amount to a given address

    Send an amount to a given address. The amount is a real and is rounded to the nearest 0.00000001.  ### Description - Send Pastel to a specified address with optional comments and fee deduction options. - By default, the change is sent to the original address unless specified otherwise.  ### Input Parameters - &#x60;t_address&#x60; (string, required): The Pastel address to send to. - &#x60;amount&#x60; (numeric, required): The amount in Pastel to send. e.g., 0.1 - &#x60;comment&#x60; (string, optional): A comment for transaction record-keeping, not part of the transaction. - &#x60;comment_to&#x60; (string, optional): A comment about the recipient, for record-keeping. - &#x60;subtract_fee_from_amount&#x60; (boolean, optional, default&#x3D;false): If true, the fee is deducted from the amount being sent. - &#x60;change_address&#x60; (string, optional, default&#x3D;\&quot;original\&quot;): Address for sending the change. Can be \&quot;original\&quot;, \&quot;new\&quot;, or a specific Pastel t-address.  ### Example Request - &#x60;POST /sendtoaddress&#x60; with JSON body: &#x60;&#x60;&#x60;json {     \&quot;t_address\&quot;: \&quot;PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n\&quot;,     \&quot;amount\&quot;: 0.1,     \&quot;comment\&quot;: \&quot;donation\&quot;,     \&quot;comment_to\&quot;: \&quot;seans outpost\&quot;,     \&quot;subtract_fee_from_amount\&quot;: true,     \&quot;change_address\&quot;: \&quot;new\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns the transaction ID of the completed transaction.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;transaction_id\&quot;: \&quot;b6a19f8fb228edf47e93a2b3d3ad8b1b4f7d8eac4fc0f3c6d3e2c463d7b9fc6f\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **SendToAddressRequest** | [**SendToAddressRequest**](../Models/SendToAddressRequest.md)|  | |

### Return type

[**SendToAddressResponse**](../Models/SendToAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="setAccountSetaccountPost"></a>
# **setAccountSetaccountPost**
> SetAccountResponse setAccountSetaccountPost(SetAccountRequest)

Associate a Pastel address with an account

    DEPRECATED. Sets the account associated with the given address.  ### Description - This endpoint is used to associate a Pastel address with an account. - The &#x60;account&#x60; parameter must be set to an empty string \&quot;\&quot; to represent the default account. Passing any other string will result in an error.  ### Input Parameters - &#x60;zcashaddress&#x60; (string, required): The Pastel address to be associated with an account. - &#x60;account&#x60; (string, required): The account name. Must be an empty string for the default account.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;zcashaddress\&quot;: \&quot;PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n\&quot;,     \&quot;account\&quot;: \&quot;\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object indicating success or failure of the operation.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;success\&quot;: true,     \&quot;message\&quot;: \&quot;Account associated successfully\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **SetAccountRequest** | [**SetAccountRequest**](../Models/SetAccountRequest.md)|  | |

### Return type

[**SetAccountResponse**](../Models/SetAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="setBanSetbanPost"></a>
# **setBanSetbanPost**
> SetBanResponse setBanSetbanPost(SetBanRequest)

Add or Remove an IP/Subnet from the Ban List

    Add or remove an IP/Subnet from the banned list.  ### Description - This endpoint attempts to add or remove an IP/Subnet from the banned list of the node.  ### Input Parameters - &#x60;ip_subnet&#x60;: The IP/Subnet with an optional netmask (default is /32 &#x3D; single IP). - &#x60;command&#x60;: &#39;add&#39; to add to the list, &#39;remove&#39; to remove from the list. - &#x60;bantime&#x60;: (Optional) Time in seconds for how long the IP is banned. 0 or empty uses the default time of 24 hours. - &#x60;absolute&#x60;: (Optional) If true, &#x60;bantime&#x60; is an absolute timestamp since epoch (Jan 1 1970 GMT).  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;ip_subnet\&quot;: \&quot;192.168.0.6\&quot;,     \&quot;command\&quot;: \&quot;add\&quot;,     \&quot;bantime\&quot;: 86400,     \&quot;absolute\&quot;: false } &#x60;&#x60;&#x60;  ### Response - Returns a success message upon successful addition or removal.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;result\&quot;: \&quot;Success\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Use this endpoint with caution as it affects the node&#39;s network connections.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **SetBanRequest** | [**SetBanRequest**](../Models/SetBanRequest.md)|  | |

### Return type

[**SetBanResponse**](../Models/SetBanResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="setGenerateSetgeneratePost"></a>
# **setGenerateSetgeneratePost**
> SetGenerateResponse setGenerateSetgeneratePost(SetGenerateRequest)

Set generation on or off

    Set &#39;generate&#39; true or false to turn generation on or off.               Generation is limited to &#39;genproclimit&#39; processors, -1 is unlimited.               See the getgenerate call for the current setting.               ### Description              - This endpoint allows turning on or off the generation (mining) process in the Pastel network.               - It controls the number of processors to be used for generation.               ### Input Parameters              - &#x60;generate&#x60; (boolean, required): Set to true to turn on generation, off to turn off.              - &#x60;genproclimit&#x60; (numeric, optional): Set the processor limit for when generation is on. Can be -1 for unlimited.               ### Example Request              &#x60;&#x60;&#x60;json              {                  \&quot;generate\&quot;: true,                  \&quot;genproclimit\&quot;: 1              }              &#x60;&#x60;&#x60;               ### Response              - Returns a message indicating successful change of generation setting.               ### Example Response              &#x60;&#x60;&#x60;json              {                  \&quot;message\&quot;: \&quot;Generation setting updated successfully\&quot;              }              &#x60;&#x60;&#x60;               ### Possible Errors              - HTTP 400: Bad Request if the parameters are invalid.              - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **SetGenerateRequest** | [**SetGenerateRequest**](../Models/SetGenerateRequest.md)|  | |

### Return type

[**SetGenerateResponse**](../Models/SetGenerateResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="setTxFeeSettxfeePost"></a>
# **setTxFeeSettxfeePost**
> SetTxFeeResponse setTxFeeSettxfeePost(SetTxFeeRequest)

Set the transaction fee per kB

    Set the transaction fee per kilobyte for transactions.  ### Description - This endpoint allows setting the transaction fee per kilobyte that will be used for future transactions.  ### Input Parameters - &#x60;amount&#x60;: (numeric, required) The transaction fee in [currency]/kB rounded to the nearest 0.00000001.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;amount\&quot;: 0.00001 } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object indicating whether the transaction fee was successfully set.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;success\&quot;: true } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **SetTxFeeRequest** | [**SetTxFeeRequest**](../Models/SetTxFeeRequest.md)|  | |

### Return type

[**SetTxFeeResponse**](../Models/SetTxFeeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="signMessageSignmessagePost"></a>
# **signMessageSignmessagePost**
> SignMessageResponse signMessageSignmessagePost(SignMessageRequest)

Sign a message with the private key of a t-addr

    Sign a message using the private key of a transparent address (t-addr).  ### Description - This endpoint allows you to sign a message with the private key of a specified transparent address.  - It&#39;s commonly used for proving ownership of a specific address.  ### Input Parameters - &#x60;t_addr&#x60;: (string, required) The transparent address to use for the private key. - &#x60;message&#x60;: (string, required) The message to create a signature of.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;t_addr\&quot;: \&quot;PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n\&quot;,     \&quot;message\&quot;: \&quot;my message\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the base 64 encoded signature of the message.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;signature\&quot;: \&quot;H6sliPZjFfS36emU8XThY6UvZHxY...\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid or the address is not correct. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The address must be a valid t-addr and the wallet must be unlocked for this operation.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **SignMessageRequest** | [**SignMessageRequest**](../Models/SignMessageRequest.md)|  | |

### Return type

[**SignMessageResponse**](../Models/SignMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="signRawTransactionSignrawtransactionPost"></a>
# **signRawTransactionSignrawtransactionPost**
> SignRawTransactionResponse signRawTransactionSignrawtransactionPost(SignRawTransactionRequest)

Sign a raw transaction

    Sign inputs for a raw transaction (serialized, hex-encoded).  ### Description - This endpoint signs the inputs of a given raw transaction.  ### Input Parameters - &#x60;hexstring&#x60;: The transaction hex string. - &#x60;prevtxs&#x60;: An optional array of previous dependent transaction outputs. - &#x60;privatekeys&#x60;: An optional array of base58-encoded private keys for signing. - &#x60;sighashtype&#x60;: The signature hash type (default is \&quot;ALL\&quot;). - &#x60;branchid&#x60;: An optional consensus branch ID for signing.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;hexstring\&quot;: \&quot;01000000...\&quot;,     \&quot;prevtxs\&quot;: [{\&quot;txid\&quot;: \&quot;0123abcd...\&quot;, \&quot;vout\&quot;: 0, \&quot;scriptPubKey\&quot;: \&quot;76a914...\&quot;, \&quot;amount\&quot;: 0.1}],     \&quot;privatekeys\&quot;: [\&quot;5J1m2B...\&quot;, \&quot;5Hs2R...\&quot;],     \&quot;sighashtype\&quot;: \&quot;ALL\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns the signed transaction in hex format, along with a flag indicating if the transaction has a complete set of signatures.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;hex\&quot;: \&quot;01000000...\&quot;,     \&quot;complete\&quot;: true,     \&quot;errors\&quot;: [] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The endpoint is used for manually signing raw transactions before broadcasting them to the network.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **SignRawTransactionRequest** | [**SignRawTransactionRequest**](../Models/SignRawTransactionRequest.md)|  | |

### Return type

[**SignRawTransactionResponse**](../Models/SignRawTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="signWithPastelIdPastelidSignPost"></a>
# **signWithPastelIdPastelidSignPost**
> PastelIDSignResponse signWithPastelIdPastelidSignPost(PastelIDSignRequest)

Sign a text with Pastel ID

    Sign a text using the private key associated with a Pastel ID.  ### Description - Signs a provided text using the private key corresponding to the specified Pastel ID.  ### Input Parameters - &#x60;text&#x60;: The text to be signed. - &#x60;pastel_id&#x60;: The Pastel ID used for signing. - &#x60;passphrase&#x60;: The passphrase for the private key. - &#x60;algorithm&#x60;: (Optional) The signing algorithm, either &#39;ed448&#39; (default) or &#39;legroast&#39;.  ### Request JSON Format &#x60;&#x60;&#x60;json {     \&quot;text\&quot;: \&quot;Example text\&quot;,     \&quot;pastel_id\&quot;: \&quot;pastel_id_example\&quot;,     \&quot;passphrase\&quot;: \&quot;secure_passphrase\&quot;,     \&quot;algorithm\&quot;: \&quot;ed448\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the signature of the text.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;signature\&quot;: \&quot;generated_signature\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **PastelIDSignRequest** | [**PastelIDSignRequest**](../Models/PastelIDSignRequest.md)|  | |

### Return type

[**PastelIDSignResponse**](../Models/PastelIDSignResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="storageFeeStoragefeePost"></a>
# **storageFeeStoragefeePost**
> StorageFeeResponse storageFeeStoragefeePost(command, body)

Interact with Storage Fee and related actions

    Interact with various Storage Fee and related actions in the Pastel network.  ### Description - This endpoint allows interaction with various aspects of storage fees and related actions.  ### Input Parameters - &#x60;command&#x60;: The storage fee command to execute. - &#x60;params&#x60;: Parameters for the specified command.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;command\&quot;: \&quot;getstoragefee\&quot;,     \&quot;params\&quot;: {\&quot;is_local\&quot;: true, \&quot;height\&quot;: 1000} } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the result of the storage fee command.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;result\&quot;: {         \&quot;storage_fee\&quot;: \&quot;0.001\&quot;,         \&quot;height\&quot;: 1000     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **command** | **String**|  | [default to null] |
| **body** | **oas_any_type_not_mapped**|  | |

### Return type

[**StorageFeeResponse**](../Models/StorageFeeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="storagefeeSetfeeStoragefeeSetfeePost"></a>
# **storagefeeSetfeeStoragefeeSetfeePost**
> StorageFeeSetFeeResponse storagefeeSetfeeStoragefeeSetfeePost(StorageFeeSetFeeRequest)

Set a new fee for a specified fee type

    Set a new fee for various types of fees in the masternode system.  ### Description - This endpoint allows setting a new fee for storage, ticket, sense-compute, or sense-processing. - It requires an active masternode to execute.  ### Input Parameters - &#x60;fee_type&#x60;: The type of fee to set. Valid types are &#39;storage&#39;, &#39;ticket&#39;, &#39;sense-compute&#39;, and &#39;sense-processing&#39;. - &#x60;new_fee&#x60;: (Optional) The new fee amount to set. If not specified, the current fee for the specified type will be maintained.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;fee_type\&quot;: \&quot;storage\&quot;,     \&quot;new_fee\&quot;: 100 } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object indicating the success of the operation.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;success\&quot;: true } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid or the fee type is not recognized. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request. - HTTP 403: Forbidden if the request is not made by an active masternode.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **StorageFeeSetFeeRequest** | [**StorageFeeSetFeeRequest**](../Models/StorageFeeSetFeeRequest.md)|  | |

### Return type

[**StorageFeeSetFeeResponse**](../Models/StorageFeeSetFeeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="storeChaindataChaindataStorePost"></a>
# **storeChaindataChaindataStorePost**
> ChaindataStoreResponse storeChaindataChaindataStorePost(ChaindataStoreRequest)

Store data in the blockchain

    Store data in the blockchain. If successful, returns the transaction ID and raw transaction data.  ### Description - This endpoint stores provided data into the blockchain using a P2FMS transaction. - The maximum size of the data is 4KB.  ### Input Parameters - &#x60;data&#x60;: The data to be stored in the blockchain.  ### Example Request - &#x60;POST /chaindata/store&#x60; with JSON payload &#x60;{\&quot;data\&quot;: \&quot;&lt;your-data&gt;\&quot;}&#x60;  ### Response - Returns a JSON object containing the transaction ID (&#x60;txid&#x60;) and the raw transaction data (&#x60;rawtx&#x60;).  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;txid\&quot;: \&quot;example-txid\&quot;,     \&quot;rawtx\&quot;: \&quot;example-rawtx\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the data is not provided, is empty, or exceeds 4KB. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The data stored can later be retrieved using the &#39;retrieve&#39; command with the returned &#x60;txid&#x60;.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ChaindataStoreRequest** | [**ChaindataStoreRequest**](../Models/ChaindataStoreRequest.md)|  | |

### Return type

[**ChaindataStoreResponse**](../Models/ChaindataStoreResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="submitBlockSubmitblockPost"></a>
# **submitBlockSubmitblockPost**
> SubmitBlockResponse submitBlockSubmitblockPost(SubmitBlockRequest)

Submit a new block to the network

    Attempt to submit a new block to the network.  ### Description - This endpoint attempts to submit a new block to the blockchain.  - The &#39;jsonparametersobject&#39; parameter is currently ignored.  ### Input Parameters - &#x60;hexdata&#x60;: Hex-encoded block data to submit. - &#x60;jsonparametersobject&#x60;: Optional JSON object of parameters.  ### Request JSON Format &#x60;&#x60;&#x60;json {     \&quot;hexdata\&quot;: \&quot;blockdata\&quot;,     \&quot;jsonparametersobject\&quot;: {\&quot;workid\&quot;: \&quot;id\&quot;} } &#x60;&#x60;&#x60;  ### Response - Returns the result of the block submission.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;result\&quot;: \&quot;duplicate\&quot; // or \&quot;duplicate-invalid\&quot;, \&quot;duplicate-inconclusive\&quot;, \&quot;inconclusive\&quot;, \&quot;rejected\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if there are issues with the block data. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The block submission process follows the specification outlined in BIP 0022.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **SubmitBlockRequest** | [**SubmitBlockRequest**](../Models/SubmitBlockRequest.md)|  | |

### Return type

[**SubmitBlockResponse**](../Models/SubmitBlockResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="ticketsFindByLabelTicketsFindbylabelTicketTypeLabelGet"></a>
# **ticketsFindByLabelTicketsFindbylabelTicketTypeLabelGet**
> TicketsFindByLabelResponse ticketsFindByLabelTicketsFindbylabelTicketTypeLabelGet(ticket\_type, label)

Find tickets by label

    Find various types of Pastel tickets by label.  ### Description - This endpoint searches for different types of Pastel tickets (like NFT, collection, or action registration tickets) using a specific label.  ### Input Parameters - &#x60;ticket_type&#x60;: The type of ticket to search for (nft, action, collection). - &#x60;label&#x60;: The label used for ticket search.  ### Example Request - &#x60;GET /tickets/findbylabel/nft/someLabel&#x60;  ### Response - Returns a JSON object containing a list of tickets that match the given label.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;tickets\&quot;: [         {\&quot;ticket_data\&quot;: {\&quot;ticket_field1\&quot;: \&quot;value1\&quot;, \&quot;ticket_field2\&quot;: \&quot;value2\&quot;}},         {\&quot;ticket_data\&quot;: {\&quot;ticket_field1\&quot;: \&quot;value3\&quot;, \&quot;ticket_field2\&quot;: \&quot;value4\&quot;}}     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the ticket type is invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Use this endpoint to search for tickets by their labels across different ticket types.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ticket\_type** | **String**|  | [default to null] |
| **label** | **String**|  | [default to null] |

### Return type

[**TicketsFindByLabelResponse**](../Models/TicketsFindByLabelResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="ticketsFindTicketsFindGet"></a>
# **ticketsFindTicketsFindGet**
> Response_Tickets_Find_Tickets_Find_Get ticketsFindTicketsFindGet(ticket\_type, key)

Find Pastel tickets

    Find various types of Pastel tickets based on a given key.  ### Description - This endpoint searches for different types of Pastel tickets in the blockchain.  ### Input Parameters - &#x60;ticket_type&#x60;: Type of the ticket to find (e.g., &#39;id&#39;, &#39;nft&#39;, &#39;act&#39;, etc.). - &#x60;key&#x60;: The key to use for ticket search.  ### Example Request - &#x60;GET /tickets/find?ticket_type&#x3D;nft&amp;key&#x3D;exampleKey&#x60;  ### Response - Returns a JSON object or an array of objects containing the ticket data.  ### Example Response &#x60;&#x60;&#x60;json [     {         \&quot;ticket_id\&quot;: \&quot;exampleTicketId\&quot;,         \&quot;ticket_data\&quot;: {             \&quot;field1\&quot;: \&quot;value1\&quot;,             \&quot;field2\&quot;: \&quot;value2\&quot;             // ... other ticket data fields         }     }     // ... other tickets ] &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The structure and type of ticket returned depend on the ticket type being searched.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ticket\_type** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **key** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |

### Return type

[**Response_Tickets_Find_Tickets_Find_Get**](../Models/Response_Tickets_Find_Tickets_Find_Get.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="ticketsGetTicketsGetGet"></a>
# **ticketsGetTicketsGetGet**
> TicketsGetResponse ticketsGetTicketsGetGet(TicketsGetRequest)

Get a Pastel ticket by transaction ID

    Get any Pastel ticket by its transaction ID (txid).  ### Description - This endpoint retrieves a specific Pastel ticket based on its transaction ID. - It optionally decodes the ticket properties if &#39;decode_properties&#39; is set to true.  ### Input Parameters - &#x60;txid&#x60;: The transaction ID of the ticket. - &#x60;decode_properties&#x60;: (Optional) Boolean flag to decode ticket properties, default is false.  ### Example Request - &#x60;GET /tickets/get?txid&#x3D;bc1c5243284272dbb22c301a549d112e8bc9bc454b5ff50b1e5f7959d6b56726&amp;decode_properties&#x3D;true&#x60;  ### Response - Returns a JSON object containing the ticket information.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;ticket\&quot;: {         \&quot;property1\&quot;: \&quot;value1\&quot;,         \&quot;property2\&quot;: \&quot;value2\&quot;,         // Other ticket properties     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **TicketsGetRequest** | [**TicketsGetRequest**](../Models/TicketsGetRequest.md)|  | |

### Return type

[**TicketsGetResponse**](../Models/TicketsGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="ticketsRegisterAcceptTicketsRegisterAcceptPost"></a>
# **ticketsRegisterAcceptTicketsRegisterAcceptPost**
> TicketsRegisterAcceptResponse ticketsRegisterAcceptTicketsRegisterAcceptPost(TicketsRegisterAcceptRequest)

Register an accept ticket

    Register an accept ticket for a specific offer on the Pastel network.  ### Description - This endpoint is used to accept an offer for a ticket on the Pastel network. - It creates an accept ticket that indicates the acceptance of an offer.  ### Input Parameters - &#x60;offer_txid&#x60;: The transaction ID of the offer ticket to accept. - &#x60;price&#x60;: The accepted price in PSL. It should be equal to or more than the asked price in the offer ticket. - &#x60;pastel_id&#x60;: The Pastel ID of the new owner. - &#x60;passphrase&#x60;: The passphrase to the private key associated with the creator&#39;s Pastel ID. - &#x60;address&#x60;: (Optional) The Pastel blockchain t-address to use for funding the registration.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;offer_txid\&quot;: \&quot;example_txid\&quot;,     \&quot;price\&quot;: 100000,     \&quot;pastel_id\&quot;: \&quot;example_pastel_id\&quot;,     \&quot;passphrase\&quot;: \&quot;example_passphrase\&quot;,     \&quot;address\&quot;: \&quot;example_address\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the ticket details, block height, and transaction ID.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;ticket\&quot;: {         \&quot;type\&quot;: \&quot;accept\&quot;,         \&quot;pastelID\&quot;: \&quot;example_pastel_id\&quot;,         \&quot;offer_txid\&quot;: \&quot;example_txid\&quot;,         \&quot;price\&quot;: 100000,         \&quot;signature\&quot;: \&quot;example_signature\&quot;     },     \&quot;height\&quot;: \&quot;example_height\&quot;,     \&quot;txid\&quot;: \&quot;example_txid\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **TicketsRegisterAcceptRequest** | [**TicketsRegisterAcceptRequest**](../Models/TicketsRegisterAcceptRequest.md)|  | |

### Return type

[**TicketsRegisterAcceptResponse**](../Models/TicketsRegisterAcceptResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="ticketsRegisterCollectionTicketsRegistercollectionPost"></a>
# **ticketsRegisterCollectionTicketsRegistercollectionPost**
> RegisterCollectionTicketResponse ticketsRegisterCollectionTicketsRegistercollectionPost(RegisterCollectionTicketRequest)

Register a collection ticket

    Register a new collection ticket on the Pastel blockchain.  ### Description - This endpoint is used for registering a new collection ticket, representing a collection of NFTs on the Pastel blockchain. - The ticket includes collection details like name, creator, authorized contributors, and metadata.  ### Input Parameters - &#x60;collection_ticket&#x60;: Base64 encoded collection ticket. - &#x60;signatures&#x60;: Signatures and Pastel IDs of principal and verifying masternodes. - &#x60;pastelid&#x60;: The Pastel ID of the registering masternode (MN1). - &#x60;passphrase&#x60;: Passphrase for the private key associated with PastelID. - &#x60;label&#x60;: A label for the ticket. - &#x60;fee&#x60;: Storage fee for registering the ticket. - &#x60;address&#x60;: (Optional) Pastel blockchain address for funding the registration.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;collection_ticket\&quot;: \&quot;Base64EncodedTicket\&quot;,     \&quot;signatures\&quot;: {         \&quot;principal\&quot;: {\&quot;PastelID\&quot;: \&quot;Signature\&quot;},         \&quot;mn2\&quot;: {\&quot;PastelID\&quot;: \&quot;Signature\&quot;},         \&quot;mn3\&quot;: {\&quot;PastelID\&quot;: \&quot;Signature\&quot;}     },     \&quot;pastelid\&quot;: \&quot;jXYqZNPj21RVnwxnEJ654wEdzi7GZTZ5LAdiotBmPrF7pDMkpX1JegDMQZX55WZLkvy9fxNpZcbBJuE8QYUqBF\&quot;,     \&quot;passphrase\&quot;: \&quot;yourPassphrase\&quot;,     \&quot;label\&quot;: \&quot;MyCollection\&quot;,     \&quot;fee\&quot;: 100,     \&quot;address\&quot;: \&quot;OptionalAddress\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns details of the registered collection ticket including transaction ID, height, and ticket information.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;txid\&quot;: \&quot;TransactionId\&quot;,     \&quot;height\&quot;: 123456,     \&quot;ticket\&quot;: {         ... // Detailed ticket information     },     ... // Other fields } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **RegisterCollectionTicketRequest** | [**RegisterCollectionTicketRequest**](../Models/RegisterCollectionTicketRequest.md)|  | |

### Return type

[**RegisterCollectionTicketResponse**](../Models/RegisterCollectionTicketResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="ticketsRegisterDownTicketsRegisterDownPost"></a>
# **ticketsRegisterDownTicketsRegisterDownPost**
> TicketsRegisterDownResponse ticketsRegisterDownTicketsRegisterDownPost(txid, pastelid, passphrase, address)

Register a Take Down Request Ticket

    Register a take down request ticket in the Pastel Network.  ### Description - This endpoint registers a take down request ticket, which is a request to take down a piece of content. It returns the transaction ID if successful.  ### Input Parameters - &#x60;txid&#x60;: The transaction ID. - &#x60;pastelid&#x60;: The Pastel ID. Note: Pastel ID must be generated and stored inside the node. - &#x60;passphrase&#x60;: The passphrase to the private key associated with the Pastel ID. - &#x60;address&#x60;: (Optional) The Pastel blockchain t-address to use for funding the registration.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;txid\&quot;: \&quot;jXYqZNPj21RVnwxnEJ654wEdzi7GZTZ5LAdiotBmPrF7pDMkpX1JegDMQZX55WZLkvy9fxNpZcbBJuE8QYUqBF\&quot;,     \&quot;pastelid\&quot;: \&quot;your_pastel_id\&quot;,     \&quot;passphrase\&quot;: \&quot;your_passphrase\&quot;,     \&quot;address\&quot;: \&quot;optional_pastel_address\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object with the details of the registered take down request ticket.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;ticket\&quot;: {         \&quot;type\&quot;: \&quot;pastelid\&quot;,         \&quot;pastelID\&quot;: \&quot;your_pastel_id\&quot;,         \&quot;timeStamp\&quot;: \&quot;timestamp\&quot;,         \&quot;signature\&quot;: \&quot;signature\&quot;     },     \&quot;height\&quot;: \&quot;block_height\&quot;,     \&quot;txid\&quot;: \&quot;transaction_id\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are incorrect. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is used for registering take down requests in the Pastel Network.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **txid** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **pastelid** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **passphrase** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **address** | [**Address**](../Models/.md)|  | [optional] [default to null] |

### Return type

[**TicketsRegisterDownResponse**](../Models/TicketsRegisterDownResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="ticketsRegisterEthereumAddressTicketsRegisterEthereumaddressPost"></a>
# **ticketsRegisterEthereumAddressTicketsRegisterEthereumaddressPost**
> TicketsRegisterEthereumAddressResponse ticketsRegisterEthereumAddressTicketsRegisterEthereumaddressPost(TicketsRegisterEthereumAddressRequest)

Register Ethereum Address Change Request

    Register an Ethereum Address Change Request ticket.  ### Description - This endpoint registers a change of Ethereum address associated with a given Pastel ID.  ### Input Parameters - &#x60;ethereum_address&#x60;: The Ethereum address to be mapped with the Pastel ID. - &#x60;pastel_id&#x60;: The Pastel ID. - &#x60;passphrase&#x60;: The passphrase to the private key associated with the Pastel ID. - &#x60;address&#x60; (optional): The Pastel blockchain t-address for funding the registration.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;ethereum_address\&quot;: \&quot;0x863c30dd122a21f815e46ec510777fd3e3398c26\&quot;,     \&quot;pastel_id\&quot;: \&quot;jXYqZNPj21RVnwxnEJ654wEdzi7GZTZ5LAdiotBmPrF7pDMkpX1JegDMQZX55WZLkvy9fxNpZcbBJuE8QYUqBF\&quot;,     \&quot;passphrase\&quot;: \&quot;passphrase\&quot;,     \&quot;address\&quot;: \&quot;optional_t_address\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the details of the registered Ethereum address change request.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;ticket\&quot;: {         \&quot;type\&quot;: \&quot;ethereumAddress\&quot;,         \&quot;pastelID\&quot;: \&quot;jXYqZNPj...\&quot;,         \&quot;ethereumAddress\&quot;: \&quot;0x863c30d...\&quot;,         \&quot;fee\&quot;: \&quot;0.1\&quot;,         \&quot;signature\&quot;: \&quot;...\&quot;     },     \&quot;height\&quot;: \&quot;123456\&quot;,     \&quot;txid\&quot;: \&quot;xyz123abc...\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if input parameters are incorrect. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **TicketsRegisterEthereumAddressRequest** | [**TicketsRegisterEthereumAddressRequest**](../Models/TicketsRegisterEthereumAddressRequest.md)|  | |

### Return type

[**TicketsRegisterEthereumAddressResponse**](../Models/TicketsRegisterEthereumAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="ticketsRegisterIdTicketsRegisterIdPost"></a>
# **ticketsRegisterIdTicketsRegisterIdPost**
> TicketsRegisterIdResponse ticketsRegisterIdTicketsRegisterIdPost(TicketsRegisterIdRequest)

Register Pastel ID identity

    Register a Pastel ID identity on the Pastel blockchain.  ### Description - This endpoint is used to register a new Pastel ID identity. - The Pastel ID must be pre-generated and stored inside the node.  ### Input Parameters - &#x60;pastelid&#x60; (string, required): The Pastel ID. The Pastel ID must be generated and stored inside the node. - &#x60;passphrase&#x60; (string, required): The passphrase to the private key associated with the Pastel ID and stored inside the node. - &#x60;address&#x60; (string, required): The Pastel blockchain t-address to use for funding the transaction.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;pastelid\&quot;: \&quot;jXaShWhNtatHVPWRNPsvjoVHUYes2kA7T9EJVL9i9EKPdBNo5aTYp19niWemJb2EwgYYR68jymULPtmHdETf8M\&quot;,     \&quot;passphrase\&quot;: \&quot;passphrase\&quot;,     \&quot;address\&quot;: \&quot;tPmjPqWdUXD68JBTWYBTtqeCDwdFwwRjikg\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the transaction ID and other details of the registered Pastel ID.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;ticket\&quot;: {         \&quot;type\&quot;: \&quot;pastelid\&quot;,         \&quot;pastelID\&quot;: \&quot;jXaShWhN...\&quot;,         \&quot;address\&quot;: \&quot;tPmjPqWdUXD68...\&quot;,         \&quot;timeStamp\&quot;: \&quot;2021-04-25T15:30:00\&quot;,         \&quot;signature\&quot;: \&quot;HwMv...&#x3D;\&quot;     },     \&quot;height\&quot;: \&quot;100000\&quot;,     \&quot;txid\&quot;: \&quot;3a1b2c3d4e5f6789a0b1c2d3e4f5a678b9c0d1e2f3a4b5c6d7e8f9g0h1i2j3k4\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **TicketsRegisterIdRequest** | [**TicketsRegisterIdRequest**](../Models/TicketsRegisterIdRequest.md)|  | |

### Return type

[**TicketsRegisterIdResponse**](../Models/TicketsRegisterIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="ticketsRegisterMnidTicketsRegisterMnidPost"></a>
# **ticketsRegisterMnidTicketsRegisterMnidPost**
> TicketsRegisterMnidResponse ticketsRegisterMnidTicketsRegisterMnidPost(pastelid, passphrase, address)

Register Masternode PastelID

    Register the identity of the current Masternode into the blockchain.   ### Description - This endpoint registers the PastelID of the Masternode on the blockchain. It requires an active Masternode.  ### Input Parameters - &#x60;pastelid&#x60;: The PastelID to register. The PastelID must be generated and stored inside the node. - &#x60;passphrase&#x60;: The passphrase to the private key associated with the PastelID. - &#x60;address&#x60; (optional): The Pastel blockchain t-address to use for funding the registration.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;pastelid\&quot;: \&quot;jXaShWhNtatHVPWRNPsvjoVHUYes2kA7T9EJVL9i9EKPdBNo5aTYp19niWemJb2EwgYYR68jymULPtmHdETf8M\&quot;,     \&quot;passphrase\&quot;: \&quot;passphrase\&quot;,     \&quot;address\&quot;: \&quot;P_address\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the registration details of the Masternode PastelID.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;ticket\&quot;: {         \&quot;type\&quot;: \&quot;pastelid\&quot;,         \&quot;pastelID\&quot;: \&quot;jXaShWhNtatHVPWRNPsvjoVHUYes2kA7T9EJVL9i9EKPdBNo5aTYp19niWemJb2EwgYYR68jymULPtmHdETf8M\&quot;,         \&quot;address\&quot;: \&quot;P_address\&quot;,         \&quot;outpoint\&quot;: \&quot;\&quot;,         \&quot;timeStamp\&quot;: \&quot;\&quot;,         \&quot;signature\&quot;: \&quot;\&quot;     },     \&quot;height\&quot;: \&quot;12345\&quot;,     \&quot;txid\&quot;: \&quot;abcd1234\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Only active Masternodes can register their PastelID.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pastelid** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **passphrase** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **address** | [**Address**](../Models/.md)|  | [optional] [default to null] |

### Return type

[**TicketsRegisterMnidResponse**](../Models/TicketsRegisterMnidResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="ticketsRegisterOfferTicketsRegisterOfferPost"></a>
# **ticketsRegisterOfferTicketsRegisterOfferPost**
> TicketsRegisterOfferResponse ticketsRegisterOfferTicketsRegisterOfferPost(TicketsRegisterOfferRequest)

Register an offer ticket

    Register an offer ticket in the Pastel network.  ### Description - Registers an offer ticket on the Pastel network. This is used for offering an NFT for sale, either as the original creator or as the current owner if the NFT has been transferred.  ### Input Parameters - &#x60;txid&#x60;: The transaction ID of the ticket to offer. This is either the NFT Activation ticket (if the current owner is the original creator) or a Transfer ticket (if the current owner is not the original creator). - &#x60;price&#x60;: The offer price in PSL. - &#x60;pastel_id&#x60;: The Pastel ID of the current owner. This must be the same Pastel ID used to sign the ticket referred to by &#x60;txid&#x60;. - &#x60;passphrase&#x60;: The passphrase to the private key associated with the creator&#39;s Pastel ID. - &#x60;valid_after&#x60;: (Optional) The block height after which this offer ticket will become active. - &#x60;valid_before&#x60;: (Optional) The block height after which this offer ticket is no longer valid. - &#x60;copy_number&#x60;: (Optional) If present, will replace the original not yet accepted Offer ticket with this copy number. - &#x60;address&#x60;: (Optional) The Pastel blockchain address to use for funding the registration. - &#x60;intended_for&#x60;: (Optional) The Pastel ID of the intended recipient of the offer.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;txid\&quot;: \&quot;txid_value\&quot;,     \&quot;price\&quot;: 100000,     \&quot;pastel_id\&quot;: \&quot;pastel_id_value\&quot;,     \&quot;passphrase\&quot;: \&quot;passphrase_value\&quot;,     \&quot;valid_after\&quot;: 0,     \&quot;valid_before\&quot;: 0,     \&quot;copy_number\&quot;: 0,     \&quot;address\&quot;: \&quot;address_value\&quot;,     \&quot;intended_for\&quot;: \&quot;intended_for_value\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing details of the registered offer ticket.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;ticket\&quot;: {         \&quot;type\&quot;: \&quot;offer\&quot;,         \&quot;pastelID\&quot;: \&quot;pastel_id_value\&quot;,         \&quot;txid\&quot;: \&quot;txid_value\&quot;,         \&quot;copy_number\&quot;: \&quot;0\&quot;,         \&quot;asked_price\&quot;: \&quot;100000\&quot;,         \&quot;valid_after\&quot;: \&quot;0\&quot;,         \&quot;valid_before\&quot;: \&quot;0\&quot;,         \&quot;signature\&quot;: \&quot;signature_value\&quot;     },     \&quot;height\&quot;: \&quot;block_height_value\&quot;,     \&quot;txid\&quot;: \&quot;txid_value\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **TicketsRegisterOfferRequest** | [**TicketsRegisterOfferRequest**](../Models/TicketsRegisterOfferRequest.md)|  | |

### Return type

[**TicketsRegisterOfferResponse**](../Models/TicketsRegisterOfferResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="ticketsTicketsCommandGet"></a>
# **ticketsTicketsCommandGet**
> TicketsResponse ticketsTicketsCommandGet(command)

Execute Pastel Ticket Commands

    Execute various commands related to Pastel tickets.  ### Description - This endpoint allows for the execution of various commands related to Pastel tickets such as registering, activating, finding, listing, and getting tickets.  ### Input Parameters - &#x60;command&#x60;: The Pastel ticket command to execute. Available commands include register, activate, find, findbylabel, list, get, and tools.  ### Example Request - &#x60;GET /tickets/register&#x60;  ### Response - Returns the result of the executed command.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;result\&quot;: \&quot;Result of the executed command\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the command is not recognized. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The functionality of this endpoint depends on the specific command executed.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **command** | **String**|  | [default to null] |

### Return type

[**TicketsResponse**](../Models/TicketsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="ticketsToolsSearchthumbidsTicketsToolsSearchthumbidsPost"></a>
# **ticketsToolsSearchthumbidsTicketsToolsSearchthumbidsPost**
> TicketSearchThumbIdsResponse ticketsToolsSearchthumbidsTicketsToolsSearchthumbidsPost(TicketSearchThumbIdsRequest)

Search for NFT registration tickets and thumbnail hash

    Search for the NFT registration tickets and thumbnail_hash using filters defined by the search_json parameter (Base64-encoded).  ### Description - This endpoint allows searching for NFT registration tickets and associated thumbnail hashes based on various criteria. - The search criteria are provided as a Base64-encoded JSON string.  ### Input Parameters - &#x60;search_json_base64&#x60;: A Base64-encoded JSON string defining the search criteria. The JSON structure includes fields like &#39;creator&#39;, &#39;blocks&#39;, &#39;copies&#39;, &#39;rareness_score&#39;, &#39;nsfw_score&#39;, and &#39;fuzzy&#39; for fuzzy searches.  ### Example Request - &#x60;POST /tickets/tools/searchthumbids&#x60; with JSON body:   &#x60;&#x60;&#x60;json   {       \&quot;search_json_base64\&quot;: \&quot;eyJjcmVhdG9yIjogIm1pbmUiLCAiYmxvY2tzIjogWzIwMDAwLDMwMDAwXSwgImNvcGllcyI6IFswLDJdfQ&#x3D;&#x3D;\&quot;   }   &#x60;&#x60;&#x60;  ### Response - Returns a JSON array of objects with NFT registration ticket \&quot;txid\&quot; and thumbnail hash.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;tickets\&quot;: [         {\&quot;txid\&quot;: \&quot;txid_1\&quot;, \&quot;thumbnail_hash\&quot;: \&quot;thumbnail_hash_1\&quot;},         {\&quot;txid\&quot;: \&quot;txid_2\&quot;, \&quot;thumbnail_hash\&quot;: \&quot;thumbnail_hash_2\&quot;}     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid or if the Base64 decoding fails. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **TicketSearchThumbIdsRequest** | [**TicketSearchThumbIdsRequest**](../Models/TicketSearchThumbIdsRequest.md)|  | |

### Return type

[**TicketSearchThumbIdsResponse**](../Models/TicketSearchThumbIdsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="ticketsToolsTicketsToolsPost"></a>
# **ticketsToolsTicketsToolsPost**
> TicketsToolsResponse ticketsToolsTicketsToolsPost(TicketsToolsRequest)

Execute various ticket tools commands

    Execute a set of Pastel ticket tools commands.  ### Description - This endpoint provides a variety of tools related to Pastel tickets, enabling operations like printing trading chains, getting registration tickets by transfer txid, validating usernames and ethereum addresses, and more.  ### Input Parameters - &#x60;command&#x60; (str, required): The command to be executed. - &#x60;additional_params&#x60; (List[str], optional): Additional parameters required for specific commands.  ### Example Request - &#x60;POST /tickets/tools&#x60; with JSON body: &#x60;&#x60;&#x60;json {     \&quot;command\&quot;: \&quot;printtradingchain\&quot;,     \&quot;additional_params\&quot;: [\&quot;param1\&quot;, \&quot;param2\&quot;] } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the result of the executed command.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;result\&quot;: {         \&quot;key\&quot;: \&quot;value\&quot;     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The specific output and required additional parameters depend on the command executed.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **TicketsToolsRequest** | [**TicketsToolsRequest**](../Models/TicketsToolsRequest.md)|  | |

### Return type

[**TicketsToolsResponse**](../Models/TicketsToolsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="validateAddressValidateaddressPost"></a>
# **validateAddressValidateaddressPost**
> ValidateAddressResponse validateAddressValidateaddressPost(ValidateAddressRequest)

Validate a Pastel address

    Validate a given Pastel transparent address.  ### Description - This endpoint validates a specified Pastel transparent address and returns detailed information about it.  ### Input Parameters - &#x60;t_address&#x60;: The Pastel transparent address to validate.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;t_address\&quot;: \&quot;1PSSGeFHDnKNxiEyFrD1wcEaHr9hrQDDWc\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing various details about the address if it is valid. If the address is not valid, only the &#x60;isvalid&#x60; field is returned.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;isvalid\&quot;: true,     \&quot;address\&quot;: \&quot;1PSSGeFHDnKNxiEyFrD1wcEaHr9hrQDDWc\&quot;,     \&quot;scriptPubKey\&quot;: \&quot;76a914...\&quot;,     \&quot;ismine\&quot;: true,     \&quot;iswatchonly\&quot;: false,     \&quot;isscript\&quot;: false,     \&quot;pubkey\&quot;: \&quot;02...\&quot;,     \&quot;iscompressed\&quot;: true,     \&quot;account\&quot;: \&quot;\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Provides detailed information about a Pastel address, including ownership and script information.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ValidateAddressRequest** | [**ValidateAddressRequest**](../Models/ValidateAddressRequest.md)|  | |

### Return type

[**ValidateAddressResponse**](../Models/ValidateAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="validateOwnershipTicketsToolsValidateownershipPost"></a>
# **validateOwnershipTicketsToolsValidateownershipPost**
> ValidateOwnershipResponse validateOwnershipTicketsToolsValidateownershipPost(ValidateOwnershipRequest)

Validate item ownership by Pastel ID

    Validate item ownership by Pastel ID.  ### Description - This endpoint checks whether the given Pastel ID is the owner of a specified item. - It returns details of the item, including the type, ownership status, item transaction ID, and transfer ticket transaction ID.  ### Input Parameters - &#x60;item_txid&#x60; (string, required): The transaction ID of the original NFT registration. - &#x60;pastelid&#x60; (string, required): The registered Pastel ID supposed to own the item. - &#x60;passphrase&#x60; (string, required): The passphrase to the private key associated with the Pastel ID.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;item_txid\&quot;: \&quot;e4ee20e436d33f59cc313647bacff0c5b0df5b7b1c1fa13189ea7bc8b9df15a4\&quot;,     \&quot;pastelid\&quot;: \&quot;jXYqZNPj21RVnwxnEJ654wEdzi7GZTZ5LAdiotBmPrF7pDMkpX1JegDMQZX55WZLkvy9fxNpZcbBJuE8QYUqBF\&quot;,     \&quot;passphrase\&quot;: \&quot;passphrase\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object with the item type, ownership status, item transaction ID, and transfer ticket transaction ID.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;type\&quot;: \&quot;unknown\&quot;,     \&quot;owns\&quot;: false,     \&quot;txid\&quot;: \&quot;\&quot;,     \&quot;transfer\&quot;: \&quot;\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This method is critical for confirming ownership of NFTs and other registered items on the Pastel Network.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ValidateOwnershipRequest** | [**ValidateOwnershipRequest**](../Models/ValidateOwnershipRequest.md)|  | |

### Return type

[**ValidateOwnershipResponse**](../Models/ValidateOwnershipResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="verifyChainVerifychainGet"></a>
# **verifyChainVerifychainGet**
> VerifyChainResponse verifyChainVerifychainGet(VerifyChainRequest)

Verify the blockchain database

    Verifies the integrity of the blockchain database.  ### Description - This endpoint performs checks on the blockchain database to verify its integrity.  - It allows specification of the thoroughness of the verification and the number of blocks to check.  ### Input Parameters - &#x60;checklevel&#x60;: (Optional) An integer between 0 and 4, indicating the thoroughness of the block verification (default is 3). - &#x60;numblocks&#x60;: (Optional) The number of blocks to check. Default is 288, with 0 indicating all blocks.  ### Example Request - &#x60;GET /verifychain?checklevel&#x3D;3&amp;numblocks&#x3D;288&#x60;  ### Response - Returns a JSON object containing the result of the verification as a boolean value.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;verified\&quot;: true } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are out of the expected range. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This method is important for network administrators and developers for diagnostics and ensuring the integrity of the blockchain data.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **VerifyChainRequest** | [**VerifyChainRequest**](../Models/VerifyChainRequest.md)|  | |

### Return type

[**VerifyChainResponse**](../Models/VerifyChainResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="verifyMessageVerifymessagePost"></a>
# **verifyMessageVerifymessagePost**
> VerifyMessageResponse verifyMessageVerifymessagePost(VerifyMessageRequest)

Verify a signed message

    Verify a signed message using a Pastel transparent address, a signature, and the message itself.  ### Description - Verifies a message signature against a given Pastel transparent address.  ### Input Parameters - &#x60;t_address&#x60;: The Pastel transparent address used for the signature. - &#x60;signature&#x60;: The signature provided by the signer in base 64 encoding. - &#x60;message&#x60;: The message that was signed.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;t_address\&quot;: \&quot;Ptor9ydHJuGpNWFAX3ZTu3bXevEhCaDVrsY\&quot;,     \&quot;signature\&quot;: \&quot;signature_in_base64\&quot;,     \&quot;message\&quot;: \&quot;my message\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a boolean indicating if the signature is verified.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;is_verified\&quot;: true } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the inputs are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for validating the authenticity of messages signed with a Pastel address.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **VerifyMessageRequest** | [**VerifyMessageRequest**](../Models/VerifyMessageRequest.md)|  | |

### Return type

[**VerifyMessageResponse**](../Models/VerifyMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="walletPassphraseWalletpassphrasePost"></a>
# **walletPassphraseWalletpassphrasePost**
> WalletPassphraseResponse walletPassphraseWalletpassphrasePost(WalletPassphraseRequest)

Unlock the wallet

    Unlock the wallet with a passphrase for a given duration.  ### Description - Unlocks the wallet for the specified time period, allowing transactions related to private keys, such as sending Pastel.   ### Input Parameters - &#x60;passphrase&#x60;: The passphrase used to encrypt the wallet (string, required). - &#x60;timeout&#x60;: Duration in seconds to keep the wallet unlocked (integer, required).  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;passphrase\&quot;: \&quot;my pass phrase\&quot;,     \&quot;timeout\&quot;: 60 } &#x60;&#x60;&#x60;  ### Response - Confirmation message indicating successful unlocking of the wallet.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;result\&quot;: \&quot;Wallet unlocked successfully\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Incorrect passphrase provided. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request. - HTTP 403: Wallet is already unlocked.  ### Note - If the wallet is already unlocked, issuing this command will reset the unlock time.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **WalletPassphraseRequest** | [**WalletPassphraseRequest**](../Models/WalletPassphraseRequest.md)|  | |

### Return type

[**WalletPassphraseResponse**](../Models/WalletPassphraseResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="walletlockWalletlockPost"></a>
# **walletlockWalletlockPost**
> oas_any_type_not_mapped walletlockWalletlockPost()

Lock the wallet

    Lock the wallet by removing the encryption key from memory.  ### Description - This endpoint locks the wallet by removing the wallet encryption key from memory.  - After calling this method, you will need to call &#x60;walletpassphrase&#x60; again before being able to call any methods which require the wallet to be unlocked.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;POST /walletlock&#x60;  ### Response - Returns an empty response on successful execution.  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request or if the wallet is not encrypted. - HTTP 400: Bad Request if called with an unencrypted wallet.  ### Examples: - Set the passphrase for 2 minutes to perform a transaction:   - &#x60;walletpassphrase \&quot;my pass phrase\&quot; 120&#x60; - Perform a send (requires passphrase set):   - &#x60;sendtoaddress \&quot;PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n\&quot; 1.0&#x60; - Clear the passphrase since we are done before 2 minutes is up:   - &#x60;walletlock&#x60;  ### Note - This is primarily used for security purposes in managing wallet access.

### Parameters
This endpoint does not need any parameter.

### Return type

[**oas_any_type_not_mapped**](../Models/AnyType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="zExportKeyZExportkeyPost"></a>
# **zExportKeyZExportkeyPost**
> ZExportKeyResponse zExportKeyZExportkeyPost(ZExportKeyRequest)

Reveal the private key corresponding to a z-address

    Reveals the private key corresponding to the specified z-address.  ### Description - This endpoint is used to extract the private key associated with a given z-address. - The private key can then be used for various purposes, including wallet backup and migration.  ### Input Parameters - &#x60;zaddr&#x60;: A string representing the z-address for which the private key is required.  ### Example Request - &#x60;POST /z_exportkey&#x60;   &#x60;&#x60;&#x60;json   {       \&quot;zaddr\&quot;: \&quot;myzaddress\&quot;   }   &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the private key associated with the specified z-address.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;key\&quot;: \&quot;5Jxxxxx...\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the z-address is invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Use this endpoint cautiously as exposing private keys can lead to security risks.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ZExportKeyRequest** | [**ZExportKeyRequest**](../Models/ZExportKeyRequest.md)|  | |

### Return type

[**ZExportKeyResponse**](../Models/ZExportKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="zExportViewingKeyZExportviewingkeyGet"></a>
# **zExportViewingKeyZExportviewingkeyGet**
> ZExportViewingKeyResponse zExportViewingKeyZExportviewingkeyGet(zaddr)

Export the viewing key for a Z-address

    Export the viewing key for a specified Z-address (zaddr).  ### Description - This endpoint reveals the viewing key corresponding to a given Z-address.  - The key can then be used with the &#x60;z_importviewingkey&#x60; method.  ### Input Parameters - &#x60;zaddr&#x60;: A string representing the Z-address for which the viewing key is requested.  ### Example Request - &#x60;GET /z_exportviewingkey?zaddr&#x3D;myaddress&#x60;  ### Response - Returns a JSON object containing the viewing key for the specified Z-address.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;viewing_key\&quot;: \&quot;Zivk...\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the Z-address is invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The returned viewing key allows viewing the transaction details associated with the Z-address.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **zaddr** | **String**|  | [default to null] |

### Return type

[**ZExportViewingKeyResponse**](../Models/ZExportViewingKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="zExportWalletZExportwalletPost"></a>
# **zExportWalletZExportwalletPost**
> ExportWalletResponse zExportWalletZExportwalletPost(filename)

Export wallet keys

    Export all wallet keys, for taddr and zaddr, in a human-readable format.  ### Description - Exports all wallet keys, including both transparent (taddr) and shielded (zaddr) addresses, to a specified file. Overwriting an existing file is not permitted.  ### Input Parameters - &#x60;filename&#x60;: A string representing the filename to which the wallet keys will be exported. The file will be saved in the folder set by the &#x60;pasteld -exportdir&#x60; option.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;filename\&quot;: \&quot;my_wallet_export\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the full path of the destination file where the wallet keys are exported.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;path\&quot;: \&quot;/path/to/exported/file/my_wallet_export\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request. - HTTP 400: Bad Request if the filename parameter is not provided or if the file already exists.  ### Note - Use this endpoint to backup wallet keys securely.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **filename** | **String**|  | [default to null] |

### Return type

[**ExportWalletResponse**](../Models/ExportWalletResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="zGetBalanceZGetbalanceAddressGet"></a>
# **zGetBalanceZGetbalanceAddressGet**
> ZGetBalanceResponse zGetBalanceZGetbalanceAddressGet(address, minconf)

Get the balance of an address

    Get the balance of a transparent or private address in the Pastel blockchain.  ### Description - This endpoint returns the balance of a given t-address or z-address belonging to the node&#39;s wallet.  - CAUTION: If the wallet has only an incoming viewing key for this address, spends cannot be detected, and the returned balance may be larger than the actual balance.  ### Input Parameters - &#x60;address&#x60;: The address for which the balance is requested. It can be a transparent (t-address) or private (z-address). - &#x60;minconf&#x60; (optional): Only include transactions confirmed at least this many times. Default is 1.  ### Example Request - &#x60;GET /z_getbalance/myaddress&#x60; - &#x60;GET /z_getbalance/myaddress?minconf&#x3D;5&#x60;  ### Response - Returns a JSON object containing the balance of the specified address.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;balance\&quot;: 1234.56 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the address is invalid or does not belong to the node. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Balance is returned in )\&quot; + CURRENCY_UNIT + R\&quot;(. Primarily used to check the amount received by an address.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **address** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **minconf** | [**Minconf_1**](../Models/.md)|  | [optional] [default to 1] |

### Return type

[**ZGetBalanceResponse**](../Models/ZGetBalanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="zGetNewAddressZGetnewaddressGet"></a>
# **zGetNewAddressZGetnewaddressGet**
> ZGetNewAddressResponse zGetNewAddressZGetnewaddressGet(address\_type)

Generate a new shielded address

    Generate a new shielded address for receiving payments.   ### Description - This endpoint returns a new shielded (Zcash) Sapling address for receiving payments.  ### Input Parameters - &#x60;type&#x60;: (Optional) The type of address to generate. Currently, only &#39;Sapling&#39; type is supported.  ### Example Request - &#x60;GET /z_getnewaddress?type&#x3D;Sapling&#x60;  ### Response - Returns a JSON object containing the new shielded Zcash address.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;zcash_address\&quot;: \&quot;zs1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request. - HTTP 400: Bad Request if an invalid address type is specified.  ### Note - Used for creating new addresses to receive shielded transactions.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **address\_type** | [**Address_Type**](../Models/.md)|  | [optional] [default to null] |

### Return type

[**ZGetNewAddressResponse**](../Models/ZGetNewAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="zGetNotesCountZGetnotescountGet"></a>
# **zGetNotesCountZGetnotescountGet**
> ZGetNotesCountResponse zGetNotesCountZGetnotescountGet(minconf)

Get the count of sapling notes in the wallet

    Get the count of sapling notes in the wallet.  ### Description - This endpoint returns the number of sapling notes available in the wallet. - It includes notes in transactions confirmed at least a specified number of times.  ### Input Parameters - &#x60;minconf&#x60;: (Optional, numeric) Only include notes in transactions confirmed at least this many times. Default is 1.  ### Example Request - &#x60;GET /z_getnotescount?minconf&#x3D;1&#x60;  ### Response - Returns a JSON object containing the count of sapling notes in the wallet.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;sapling\&quot;: 5 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for assessing the number of sapling notes held in the wallet.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **minconf** | [**oas_any_type_not_mapped**](../Models/.md)|  | [optional] [default to 1] |

### Return type

[**ZGetNotesCountResponse**](../Models/ZGetNotesCountResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="zGetOperationStatusZGetoperationstatusGet"></a>
# **zGetOperationStatusZGetoperationstatusGet**
> GetOperationStatusResponse zGetOperationStatusZGetoperationstatusGet(Operation\_Ids\_1)

Get the status of asynchronous operations

    Get the status and any associated results or errors for asynchronous operations.  ### Description - This endpoint returns the status and any results or error data for asynchronous operations, such as those initiated by the &#x60;z_sendmany&#x60; or &#x60;z_shieldcoinbase&#x60; methods. - Operations will remain in memory even after completion.  ### Input Parameters - &#x60;operation_ids&#x60;: (Optional) A list of operation IDs to query. If not provided, information about all operations known to the node is returned.  ### Example Request - &#x60;GET /z_getoperationstatus?operation_ids&#x3D;[\&quot;opid-1a2b3c\&quot;, \&quot;opid-4d5e6f\&quot;]&#x60;  ### Response - Returns a JSON array of objects, each representing the status of an operation.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;operations\&quot;: [         {             \&quot;id\&quot;: \&quot;opid-1a2b3c\&quot;,             \&quot;status\&quot;: \&quot;success\&quot;,             \&quot;creation_time\&quot;: 1617754083,             \&quot;method\&quot;: \&quot;z_sendmany\&quot;,             \&quot;params\&quot;: { ... },             \&quot;result\&quot;: { ... },             \&quot;error\&quot;: null,             \&quot;execution_secs\&quot;: 2.345,             \&quot;method_finished\&quot;: true         },         {             \&quot;id\&quot;: \&quot;opid-4d5e6f\&quot;,             \&quot;status\&quot;: \&quot;executing\&quot;,             \&quot;creation_time\&quot;: 1617754090,             \&quot;method\&quot;: \&quot;z_shieldcoinbase\&quot;,             \&quot;params\&quot;: { ... },             \&quot;result\&quot;: null,             \&quot;error\&quot;: null,             \&quot;execution_secs\&quot;: null,             \&quot;method_finished\&quot;: false         }     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the provided operation IDs are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is useful for tracking the progress and outcome of operations that do not provide immediate results.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **Operation\_Ids\_1** | [**Operation_Ids_1**](../Models/Operation_Ids_1.md)|  | [optional] |

### Return type

[**GetOperationStatusResponse**](../Models/GetOperationStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="zGetTotalBalanceZGettotalbalanceGet"></a>
# **zGetTotalBalanceZGettotalbalanceGet**
> ZGetTotalBalanceResponse zGetTotalBalanceZGettotalbalanceGet(ZGetTotalBalanceRequest)

Get the total balance of both transparent and private funds

    Get the total value of funds stored in the node&#39;s wallet.  ### Description - This endpoint returns the total balance of both transparent and private funds in the node&#39;s wallet. - The balance is calculated based on the specified minimum number of confirmations and can include watchonly addresses.  ### Input Parameters - &#x60;minconf&#x60; (int, optional, default&#x3D;1): Only include transactions confirmed at least this many times. - &#x60;includeWatchonly&#x60; (bool, optional, default&#x3D;false): Include balance in watchonly addresses.  ### Example Request - &#x60;GET /z_gettotalbalance?minconf&#x3D;5&amp;includeWatchonly&#x3D;true&#x60;  ### Response - Returns a JSON object containing the total balance of transparent and private funds.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;transparent\&quot;: 100.0,     \&quot;private\&quot;: 50.0,     \&quot;total\&quot;: 150.0 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Balance calculations with watchonly addresses require the corresponding viewing keys.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ZGetTotalBalanceRequest** | [**ZGetTotalBalanceRequest**](../Models/ZGetTotalBalanceRequest.md)|  | |

### Return type

[**ZGetTotalBalanceResponse**](../Models/ZGetTotalBalanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="zGetoperationresultZGetoperationresultGet"></a>
# **zGetoperationresultZGetoperationresultGet**
> ZGetOperationResultResponse zGetoperationresultZGetoperationresultGet(Operation\_Ids)

Retrieve the result and status of Zcash operations

    Retrieve the result and status of an operation which has finished, and then remove the operation from memory.  ### Description - This endpoint retrieves the results of one or more operations identified by their operation IDs. - It&#39;s primarily used to get the outcome of previously initiated Zcash shielded operations. - The operation is removed from memory after the result is retrieved.  ### Input Parameters - &#x60;operation_ids&#x60;: (Optional) A list of operation ids to query. If not provided, the endpoint examines all operations known to the node.  ### Example Request - &#x60;GET /z_getoperationresult?operation_ids&#x3D;[\&quot;opid-1234\&quot;, \&quot;opid-5678\&quot;]&#x60;  ### Response - Returns a JSON array containing the results of the queried operations.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;operation_results\&quot;: [         {             \&quot;id\&quot;: \&quot;opid-1234\&quot;,             \&quot;status\&quot;: \&quot;success\&quot;,             \&quot;creation_time\&quot;: 1622547600,             \&quot;result\&quot;: {                 \&quot;txid\&quot;: \&quot;2f5b0e...\&quot;             },             \&quot;error\&quot;: null,             \&quot;method\&quot;: \&quot;z_sendmany\&quot;,             \&quot;params\&quot;: {                 \&quot;fromaddress\&quot;: \&quot;tm...\&quot;,                 \&quot;amounts\&quot;: [                     {                         \&quot;amount\&quot;: 0.1,                         \&quot;address\&quot;: \&quot;tm...\&quot;                     }                 ]             }         }     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The endpoint is specific to Zcash-based operations and is not applicable to standard Bitcoin transactions.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **Operation\_Ids** | [**Operation_Ids**](../Models/Operation_Ids.md)|  | [optional] |

### Return type

[**ZGetOperationResultResponse**](../Models/ZGetOperationResultResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="zImportKeyZImportkeyGet"></a>
# **zImportKeyZImportkeyGet**
> ZImportKeyResponse zImportKeyZImportkeyGet(zkey, rescan, start\_height)

Import a Z key into the wallet

    Imports a Z key (as returned by z_exportkey) to your wallet.  ### Description - Adds a Z key to your wallet and optionally rescans the wallet for transactions.  ### Input Parameters - &#x60;zkey&#x60;: The Z key to be imported (required). - &#x60;rescan&#x60;: Option to rescan the wallet for transactions - can be \&quot;yes\&quot;, \&quot;no\&quot;, or \&quot;whenkeyisnew\&quot; (optional, default&#x3D;\&quot;whenkeyisnew\&quot;). - &#x60;start_height&#x60;: Block height to start rescan from (optional, default&#x3D;0).  ### Example Request - &#x60;GET /z_importkey?zkey&#x3D;mykey&amp;rescan&#x3D;yes&amp;start_height&#x3D;30000&#x60;  ### Response - Returns a JSON object containing the type and address corresponding to the imported spending key.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;type\&quot;: \&quot;sapling\&quot;,     \&quot;address\&quot;: \&quot;ps1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Importing a key can take minutes to complete if rescan is true. The call will block until the rescan is complete.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **zkey** | **String**|  | [default to null] |
| **rescan** | **String**|  | [optional] [default to null] |
| **start\_height** | **Integer**|  | [optional] [default to null] |

### Return type

[**ZImportKeyResponse**](../Models/ZImportKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="zImportViewingKeyZImportviewingkeyPost"></a>
# **zImportViewingKeyZImportviewingkeyPost**
> ZImportViewingKeyResponse zImportViewingKeyZImportviewingkeyPost(ZImportViewingKeyRequest)

Import a viewing key into the wallet

    Import a viewing key into your wallet.  ### Description - This endpoint adds a viewing key (as returned by z_exportviewingkey) to your wallet. It allows you to track transactions associated with the viewing key&#39;s address.  ### Input Parameters - &#x60;vkey&#x60;: The viewing key to be imported. - &#x60;rescan&#x60;: Rescan option for the wallet transactions. Can be \&quot;yes\&quot;, \&quot;no\&quot;, or \&quot;whenkeyisnew\&quot;. - &#x60;start_height&#x60;: The block height from which to start the rescan.  ### Example Request - &#x60;POST /z_importviewingkey&#x60; with JSON body: &#x60;&#x60;&#x60;json {     \&quot;vkey\&quot;: \&quot;your_viewing_key\&quot;,     \&quot;rescan\&quot;: \&quot;yes\&quot;,     \&quot;start_height\&quot;: 30000 } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the type and address corresponding to the imported viewing key.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;type\&quot;: \&quot;sapling\&quot;,     \&quot;address\&quot;: \&quot;pastel_address\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request. - Specific errors for invalid viewing key or if the key already exists in the wallet.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ZImportViewingKeyRequest** | [**ZImportViewingKeyRequest**](../Models/ZImportViewingKeyRequest.md)|  | |

### Return type

[**ZImportViewingKeyResponse**](../Models/ZImportViewingKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="zImportWalletZImportwalletPost"></a>
# **zImportWalletZImportwalletPost**
> ZImportWalletResponse zImportWalletZImportwalletPost(filename)

Import keys from a wallet export file

    Imports taddr and zaddr keys from a wallet export file. This is typically used after using &#x60;z_exportwallet&#x60;.  ### Description - Allows for the importation of taddr and zaddr keys from a previously exported wallet file.  ### Input Parameters - &#x60;filename&#x60;: The path to the wallet file that needs to be imported.  ### Example Request - &#x60;POST /z_importwallet&#x60; with payload: &#x60;&#x60;&#x60;json {     \&quot;filename\&quot;: \&quot;path/to/exportdir/nameofbackup\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object indicating the success or failure of the import operation.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;success\&quot;: true,     \&quot;message\&quot;: \&quot;Wallet imported successfully\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the filename parameter is missing or invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Ensure the path to the wallet file is correct and accessible.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **filename** | **String**|  | [default to null] |

### Return type

[**ZImportWalletResponse**](../Models/ZImportWalletResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="zListOperationIdsZListoperationidsGet"></a>
# **zListOperationIdsZListoperationidsGet**
> ZListOperationIdsResponse zListOperationIdsZListoperationidsGet(status)

List Operation IDs

    List all operation IDs currently known to the wallet.  ### Description - This endpoint retrieves a list of operation IDs that are known to the wallet.    It can optionally filter these IDs based on the operation&#39;s state.  ### Input Parameters - &#x60;status&#x60;: (Optional) A string to filter the operation IDs by their state, e.g., \&quot;success\&quot;.  ### Example Request - &#x60;GET /z_listoperationids?status&#x3D;success&#x60;  ### Response - Returns a JSON array containing the operation IDs.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;operation_ids\&quot;: [\&quot;opid-1\&quot;, \&quot;opid-2\&quot;, \&quot;opid-3\&quot;] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for tracking and managing asynchronous operations performed by the wallet.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **status** | [**Status**](../Models/.md)|  | [optional] [default to null] |

### Return type

[**ZListOperationIdsResponse**](../Models/ZListOperationIdsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="zListReceivedByAddressZListreceivedbyaddressGet"></a>
# **zListReceivedByAddressZListreceivedbyaddressGet**
> ZListReceivedByAddressResponse zListReceivedByAddressZListreceivedbyaddressGet(ZListReceivedByAddressRequest)

List amounts received by a z-address

    List amounts received by a z-address belonging to the node&#39;s wallet.  ### Description - This endpoint returns a list of amounts received by a specified z-address.  - It includes various details about each received note, such as the transaction ID, amount, confirmations, and more.  ### Input Parameters - &#x60;address&#x60; (string): The z-address to query. - &#x60;minconf&#x60; (numeric, optional, default&#x3D;1): Minimum number of confirmations for a transaction to be included.  ### Example Request - &#x60;GET /z_listreceivedbyaddress?address&#x3D;&lt;z-address&gt;&amp;minconf&#x3D;1&#x60;  ### Response - Returns a JSON object containing a list of received notes, each with detailed information.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;notes\&quot;: [         {             \&quot;txid\&quot;: \&quot;example-txid\&quot;,             \&quot;amount\&quot;: 1.23,             \&quot;amountPat\&quot;: 123,             \&quot;memo\&quot;: \&quot;hex-string\&quot;,             \&quot;confirmations\&quot;: 10,             \&quot;blockheight\&quot;: 100000,             \&quot;blockindex\&quot;: 1,             \&quot;blocktime\&quot;: 1609459200,             \&quot;change\&quot;: false         }     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ZListReceivedByAddressRequest** | [**ZListReceivedByAddressRequest**](../Models/ZListReceivedByAddressRequest.md)|  | |

### Return type

[**ZListReceivedByAddressResponse**](../Models/ZListReceivedByAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="zListunspentZListunspentGet"></a>
# **zListunspentZListunspentGet**
> ZListUnspentResponse zListunspentZListunspentGet(minconf, maxconf, includeWatchonly, Addresses\_1)

List unspent shielded notes

    List unspent shielded notes with a specified range of confirmations and optionally filter for specific addresses.  ### Description - Returns an array of unspent shielded notes with a specified range of confirmations. Optionally filters to only include notes sent to specified addresses.  ### Input Parameters - &#x60;minconf&#x60;: Minimum number of confirmations to filter (default&#x3D;1). - &#x60;maxconf&#x60;: Maximum number of confirmations to filter (default&#x3D;9999999). - &#x60;includeWatchonly&#x60;: Whether to include watchonly addresses (default&#x3D;false). - &#x60;addresses&#x60;: Array of Sapling zaddrs to filter on (optional).  ### Example Request - &#x60;GET /z_listunspent?minconf&#x3D;1&amp;maxconf&#x3D;9999999&amp;includeWatchonly&#x3D;false&amp;addresses&#x3D;[\&quot;zaddr1\&quot;, \&quot;zaddr2\&quot;]&#x60;  ### Response - Returns a JSON array of objects, each representing an unspent shielded note.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;unspent_notes\&quot;: [         {             \&quot;txid\&quot;: \&quot;txid\&quot;,             \&quot;outindex\&quot;: 0,             \&quot;confirmations\&quot;: 10,             \&quot;spendable\&quot;: true,             \&quot;address\&quot;: \&quot;address\&quot;,             \&quot;amount\&quot;: 123.45,             \&quot;memo\&quot;: \&quot;hex_memo\&quot;,             \&quot;change\&quot;: false         },         ...     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Used for wallet balance management and transaction preparation.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **minconf** | [**Minconf_1**](../Models/.md)|  | [optional] [default to 1] |
| **maxconf** | [**Maxconf**](../Models/.md)|  | [optional] [default to 9999999] |
| **includeWatchonly** | [**Includewatchonly_1**](../Models/.md)|  | [optional] [default to false] |
| **Addresses\_1** | [**Addresses_1**](../Models/Addresses_1.md)|  | [optional] |

### Return type

[**ZListUnspentResponse**](../Models/ZListUnspentResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="zMergetoaddressZMergetoaddressPost"></a>
# **zMergetoaddressZMergetoaddressPost**
> MergeToAddressResponse zMergetoaddressZMergetoaddressPost(MergeToAddressRequest)

Merge multiple UTXOs and notes into a single UTXO or note

    Merge multiple UTXOs and notes into a single UTXO or note.  ### Description - This endpoint merges multiple UTXOs and notes into a single UTXO or note. Coinbase UTXOs are ignored; use &#x60;z_shieldcoinbase&#x60; to combine those into a single note. - It&#39;s an asynchronous operation, and UTXOs selected for merging will be locked. If there is an error, they are unlocked. - The number of UTXOs and notes selected for merging can be limited by the caller.  ### Input Parameters - &#x60;fromaddresses&#x60;: List of addresses. Special strings \&quot;ANY_TADDR\&quot; and \&quot;ANY_SAPLING\&quot; can be used. - &#x60;toaddress&#x60;: The address to send the funds to. - &#x60;fee&#x60;: Optional fee amount to attach to this transaction. - &#x60;transparent_limit&#x60;: Optional limit on the number of UTXOs to merge. - &#x60;shielded_limit&#x60;: Optional limit on the number of notes to merge. - &#x60;memo&#x60;: Optional memo, encoded as hex, applicable only for zaddr.  ### Example Request &#x60;&#x60;&#x60;json {   \&quot;fromaddresses\&quot;: [\&quot;ANY_SAPLING\&quot;, \&quot;t1XYZ\&quot;],   \&quot;toaddress\&quot;: \&quot;t1ABC\&quot;,   \&quot;fee\&quot;: 0.001,   \&quot;transparent_limit\&quot;: 50,   \&quot;shielded_limit\&quot;: 200,   \&quot;memo\&quot;: \&quot;48656c6c6f\&quot; } &#x60;&#x60;&#x60;  ### Response - Detailed information about the merge operation, including the number of UTXOs and notes merged, remaining ones, and the operation ID.  ### Possible Errors - HTTP 400: Bad Request for invalid parameters. - HTTP 500: Internal Server Error for processing issues.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **MergeToAddressRequest** | [**MergeToAddressRequest**](../Models/MergeToAddressRequest.md)|  | |

### Return type

[**MergeToAddressResponse**](../Models/MergeToAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="zSendManyZSendmanyPost"></a>
# **zSendManyZSendmanyPost**
> SendManyResponse zSendManyZSendmanyPost(SendManyRequest)

Send multiple times to multiple recipients

    Send multiple times to multiple recipients. This endpoint allows for sending transactions to multiple addresses.  ### Description - Allows for sending specified amounts to multiple taddr or zaddr addresses from a single fromaddress.  ### Input Parameters - &#x60;SendManyRequest&#x60;: A JSON object containing the sending address, a list of recipient addresses with amounts and optional memos, minimum confirmations, and an optional fee.  ### Request JSON Format &#x60;&#x60;&#x60;json {     \&quot;fromaddress\&quot;: \&quot;t1XYZ...\&quot;,     \&quot;amounts\&quot;: [         {\&quot;address\&quot;: \&quot;t1ABC...\&quot;, \&quot;amount\&quot;: 0.1, \&quot;memo\&quot;: \&quot;Optional memo\&quot;},         {\&quot;address\&quot;: \&quot;t1DEF...\&quot;, \&quot;amount\&quot;: 0.2}     ],     \&quot;minconf\&quot;: 1,     \&quot;fee\&quot;: 0.0001 } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the operation ID of the send operation.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;operationid\&quot;: \&quot;opid-1234567890abcdef\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Used for creating complex transactions involving multiple recipients.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **SendManyRequest** | [**SendManyRequest**](../Models/SendManyRequest.md)|  | |

### Return type

[**SendManyResponse**](../Models/SendManyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="zShieldcoinbaseZShieldcoinbasePost"></a>
# **zShieldcoinbaseZShieldcoinbasePost**
> ZShieldCoinbaseResponse zShieldcoinbaseZShieldcoinbasePost(ZShieldCoinbaseRequest)

Shield transparent coinbase funds to a shielded zaddr

    Shield transparent coinbase funds by sending them to a shielded z-address.                              This is an asynchronous operation, and UTXOs selected for shielding will be locked.  ### Description - Shields coinbase UTXOs from a transparent address (taddr) to a shielded address (zaddr), locking the UTXOs involved in the process.  ### Input Parameters - &#x60;fromaddress&#x60;: The source transparent address or \&quot;*\&quot; for all taddrs belonging to the wallet. - &#x60;toaddress&#x60;: The destination shielded address. - &#x60;fee&#x60;: (Optional) The fee amount to attach to this transaction. - &#x60;limit&#x60;: (Optional) The maximum number of UTXOs to shield. Set to 0 to shield as many as will fit in the transaction.  ### Request JSON Format &#x60;&#x60;&#x60;json {     \&quot;fromaddress\&quot;: \&quot;t1exampleaddress...\&quot;,     \&quot;toaddress\&quot;: \&quot;zs1exampleaddress...\&quot;,     \&quot;fee\&quot;: 0.0001,     \&quot;limit\&quot;: 50 } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing details about the shielding process including the operation id.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;remainingUTXOs\&quot;: 100,     \&quot;remainingValue\&quot;: 2.5,     \&quot;shieldingUTXOs\&quot;: 50,     \&quot;shieldingValue\&quot;: 1.5,     \&quot;opid\&quot;: \&quot;opid-example-1234\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ZShieldCoinbaseRequest** | [**ZShieldCoinbaseRequest**](../Models/ZShieldCoinbaseRequest.md)|  | |

### Return type

[**ZShieldCoinbaseResponse**](../Models/ZShieldCoinbaseResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="zValidateAddressZValidateaddressGet"></a>
# **zValidateAddressZValidateaddressGet**
> ZValidateAddressResponse zValidateAddressZValidateaddressGet(ZAddressQuery)

Validate a Z address

    Validate the given Z address and return information about it.  ### Description - This endpoint validates a Z address and returns various details about it, including its validity, type, and ownership.  ### Input Parameters - &#x60;zaddr&#x60;: The Z address to validate.  ### Example Request - &#x60;GET /z_validateaddress?zaddr&#x3D;PzWcy67ygestjagHaFZxjWxmawMeShmQWNPE8FNJp23pQS2twecwps5223ajUtN7iihxR4MmLDFQ19heHkBx5AKaDooS6aQ&#x60;  ### Response - Returns a JSON object with information about the Z address.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;isvalid\&quot;: true,     \&quot;address\&quot;: \&quot;PzWcy67y...\&quot;,     \&quot;type\&quot;: \&quot;sapling\&quot;,     \&quot;ismine\&quot;: false,     ... } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the address format is incorrect. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is used to verify the details and ownership of a Z address.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ZAddressQuery** | [**ZAddressQuery**](../Models/ZAddressQuery.md)|  | |

### Return type

[**ZValidateAddressResponse**](../Models/ZValidateAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="zViewTransactionZViewtransactionTxidGet"></a>
# **zViewTransactionZViewtransactionTxidGet**
> ZViewTransactionResponse zViewTransactionZViewtransactionTxidGet(txid)

Get detailed shielded information about in-wallet transaction

    Retrieve detailed information about a shielded transaction in the wallet.  ### Description - Returns detailed information about a specific in-wallet transaction, including spends and outputs related to shielded addresses.  ### Input Parameters - &#x60;txid&#x60;: The transaction id (string, required).  ### Example Request - &#x60;GET /z_viewtransaction/1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d&#x60;  ### Response - Returns detailed information about the transaction, including spends and outputs.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;txid\&quot;: \&quot;1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d\&quot;,     \&quot;spends\&quot;: [...],     \&quot;outputs\&quot;: [...] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request. - HTTP 404: Transaction not found or not part of the wallet.  ### Note - This endpoint is used to get detailed information about shielded transactions, particularly for auditing and verification purposes.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **txid** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |

### Return type

[**ZViewTransactionResponse**](../Models/ZViewTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="zcBenchmarkZcbenchmarkPost"></a>
# **zcBenchmarkZcbenchmarkPost**
> ZCBenchmarkResponse zcBenchmarkZcbenchmarkPost(ZCBenchmarkRequest)

Runs a benchmark of the selected type

    Runs a benchmark of the selected type &#x60;samplecount&#x60; times, returning the running times of each sample.  ### Description - This endpoint runs a specified benchmark multiple times and returns the running time for each iteration.  - It&#39;s useful for performance testing various operations on the Pastel blockchain.  ### Input Parameters - &#x60;benchmarktype&#x60;: The type of benchmark to run. - &#x60;samplecount&#x60;: The number of times to run the benchmark. - &#x60;extra_param&#x60;: Optional additional parameter, depending on the benchmark type.  ### Example Request &#x60;&#x60;&#x60;json {   \&quot;benchmarktype\&quot;: \&quot;solveequihash\&quot;,   \&quot;samplecount\&quot;: 5,   \&quot;extra_param\&quot;: 2 } &#x60;&#x60;&#x60;  ### Response - Returns a list of objects, each containing the &#x60;runningtime&#x60; for a benchmark sample.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;results\&quot;: [         {\&quot;runningtime\&quot;: 0.12},         {\&quot;runningtime\&quot;: 0.11},         {\&quot;runningtime\&quot;: 0.13},         {\&quot;runningtime\&quot;: 0.12},         {\&quot;runningtime\&quot;: 0.12}     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ZCBenchmarkRequest** | [**ZCBenchmarkRequest**](../Models/ZCBenchmarkRequest.md)|  | |

### Return type

[**ZCBenchmarkResponse**](../Models/ZCBenchmarkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

