# Documentation for Pastel-RPC-REST-Wrapper

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *http://localhost*

| Class | Method | HTTP request | Description |
|------------ | ------------- | ------------- | -------------|
| *BlockchainMethodsApi* | [**estimateFeeEstimatefeeGet**](Apis/BlockchainMethodsApi.md#estimatefeeestimatefeeget) | **GET** /estimatefee | Estimate the transaction fee per kilobyte |
*BlockchainMethodsApi* | [**fixMissingTransactionsFixmissingtxsStartingHeightGet**](Apis/BlockchainMethodsApi.md#fixmissingtransactionsfixmissingtxsstartingheightget) | **GET** /fixmissingtxs/{starting_height} | Fix Missing Transactions |
*BlockchainMethodsApi* | [**getAccountGetaccountZcashaddressGet**](Apis/BlockchainMethodsApi.md#getaccountgetaccountzcashaddressget) | **GET** /getaccount/{zcashaddress} | Get the account associated with a Pastel address |
*BlockchainMethodsApi* | [**getBalanceGetbalanceGet**](Apis/BlockchainMethodsApi.md#getbalancegetbalanceget) | **GET** /getbalance | Get the server's total available balance |
*BlockchainMethodsApi* | [**getBestBlockHashGetbestblockhashGet**](Apis/BlockchainMethodsApi.md#getbestblockhashgetbestblockhashget) | **GET** /getbestblockhash | Get the hash of the best block |
*BlockchainMethodsApi* | [**getBlockCountGetblockcountGet**](Apis/BlockchainMethodsApi.md#getblockcountgetblockcountget) | **GET** /getblockcount | Get the current block count |
*BlockchainMethodsApi* | [**getBlockDeltasGetblockdeltasBlockHashGet**](Apis/BlockchainMethodsApi.md#getblockdeltasgetblockdeltasblockhashget) | **GET** /getblockdeltas/{block_hash} | Get block deltas |
*BlockchainMethodsApi* | [**getBlockGetblockGet**](Apis/BlockchainMethodsApi.md#getblockgetblockget) | **GET** /getblock | Get block data |
*BlockchainMethodsApi* | [**getBlockHashGetblockhashGet**](Apis/BlockchainMethodsApi.md#getblockhashgetblockhashget) | **GET** /getblockhash | Get the hash of a block at a specific index |
*BlockchainMethodsApi* | [**getBlockHeaderGetblockheaderBlockHashGet**](Apis/BlockchainMethodsApi.md#getblockheadergetblockheaderblockhashget) | **GET** /getblockheader/{block_hash} | Get information about a block header |
*BlockchainMethodsApi* | [**getBlockchainInfoGetblockchaininfoGet**](Apis/BlockchainMethodsApi.md#getblockchaininfogetblockchaininfoget) | **GET** /getblockchaininfo | Get blockchain information |
*BlockchainMethodsApi* | [**getChainTipsGetchaintipsGet**](Apis/BlockchainMethodsApi.md#getchaintipsgetchaintipsget) | **GET** /getchaintips | Get information about all known chain tips |
*BlockchainMethodsApi* | [**getNextBlockSubsidyGetnextblocksubsidyGet**](Apis/BlockchainMethodsApi.md#getnextblocksubsidygetnextblocksubsidyget) | **GET** /getnextblocksubsidy | Get subsidy rewards for the next block |
*BlockchainMethodsApi* | [**getRawMempoolGetrawmempoolGet**](Apis/BlockchainMethodsApi.md#getrawmempoolgetrawmempoolget) | **GET** /getrawmempool | Get all transaction IDs in memory pool |
*BlockchainMethodsApi* | [**getReceivedByAddressGetreceivedbyaddressGet**](Apis/BlockchainMethodsApi.md#getreceivedbyaddressgetreceivedbyaddressget) | **GET** /getreceivedbyaddress | Get the total amount received by a Pastel address |
*BlockchainMethodsApi* | [**getTransactionGettransactionTxidGet**](Apis/BlockchainMethodsApi.md#gettransactiongettransactiontxidget) | **GET** /gettransaction/{txid} | Get detailed information about a transaction |
*BlockchainMethodsApi* | [**getTxOutGettxoutGet**](Apis/BlockchainMethodsApi.md#gettxoutgettxoutget) | **GET** /gettxout | Get details about an unspent transaction output |
*BlockchainMethodsApi* | [**getTxOutSetInfoGettxoutsetinfoGet**](Apis/BlockchainMethodsApi.md#gettxoutsetinfogettxoutsetinfoget) | **GET** /gettxoutsetinfo | Get statistics about the unspent transaction output set |
*BlockchainMethodsApi* | [**getTxfeeGettxfeeTxidGet**](Apis/BlockchainMethodsApi.md#gettxfeegettxfeetxidget) | **GET** /gettxfee/{txid} | Get transaction fee by txid |
*BlockchainMethodsApi* | [**invalidateBlockInvalidateblockPost**](Apis/BlockchainMethodsApi.md#invalidateblockinvalidateblockpost) | **POST** /invalidateblock | Mark a block as permanently invalid |
*BlockchainMethodsApi* | [**listAddressGroupingsListaddressgroupingsGet**](Apis/BlockchainMethodsApi.md#listaddressgroupingslistaddressgroupingsget) | **GET** /listaddressgroupings | List groups of addresses with common ownership |
*BlockchainMethodsApi* | [**listLockUnspentListlockunspentGet**](Apis/BlockchainMethodsApi.md#listlockunspentlistlockunspentget) | **GET** /listlockunspent | List Temporarily Unspendable Outputs |
*BlockchainMethodsApi* | [**listShieldedAddressesZListaddressesGet**](Apis/BlockchainMethodsApi.md#listshieldedaddresseszlistaddressesget) | **GET** /z_listaddresses | List Shielded Addresses |
*BlockchainMethodsApi* | [**listSinceBlockListsinceblockPost**](Apis/BlockchainMethodsApi.md#listsinceblocklistsinceblockpost) | **POST** /listsinceblock | List transactions since a specific block |
*BlockchainMethodsApi* | [**listUnspentListunspentGet**](Apis/BlockchainMethodsApi.md#listunspentlistunspentget) | **GET** /listunspent | List Unspent Transaction Outputs |
*BlockchainMethodsApi* | [**reconsiderBlockReconsiderblockPost**](Apis/BlockchainMethodsApi.md#reconsiderblockreconsiderblockpost) | **POST** /reconsiderblock | Reconsider a previously invalidated block |
*BlockchainMethodsApi* | [**submitBlockSubmitblockPost**](Apis/BlockchainMethodsApi.md#submitblocksubmitblockpost) | **POST** /submitblock | Submit a new block to the network |
*BlockchainMethodsApi* | [**verifyChainVerifychainGet**](Apis/BlockchainMethodsApi.md#verifychainverifychainget) | **GET** /verifychain | Verify the blockchain database |
*BlockchainMethodsApi* | [**zGetBalanceZGetbalanceAddressGet**](Apis/BlockchainMethodsApi.md#zgetbalancezgetbalanceaddressget) | **GET** /z_getbalance/{address} | Get the balance of an address |
*BlockchainMethodsApi* | [**zGetoperationresultZGetoperationresultGet**](Apis/BlockchainMethodsApi.md#zgetoperationresultzgetoperationresultget) | **GET** /z_getoperationresult | Retrieve the result and status of Zcash operations |
*BlockchainMethodsApi* | [**zListOperationIdsZListoperationidsGet**](Apis/BlockchainMethodsApi.md#zlistoperationidszlistoperationidsget) | **GET** /z_listoperationids | List Operation IDs |
*BlockchainMethodsApi* | [**zListunspentZListunspentGet**](Apis/BlockchainMethodsApi.md#zlistunspentzlistunspentget) | **GET** /z_listunspent | List unspent shielded notes |
*BlockchainMethodsApi* | [**zShieldcoinbaseZShieldcoinbasePost**](Apis/BlockchainMethodsApi.md#zshieldcoinbasezshieldcoinbasepost) | **POST** /z_shieldcoinbase | Shield transparent coinbase funds to a shielded zaddr |
*BlockchainMethodsApi* | [**zViewTransactionZViewtransactionTxidGet**](Apis/BlockchainMethodsApi.md#zviewtransactionzviewtransactiontxidget) | **GET** /z_viewtransaction/{txid} | Get detailed shielded information about in-wallet transaction |
| *ControlMethodsApi* | [**changeWalletPassphraseWalletpassphrasechangePost**](Apis/ControlMethodsApi.md#changewalletpassphrasewalletpassphrasechangepost) | **POST** /walletpassphrasechange | Change the wallet passphrase |
*ControlMethodsApi* | [**disconnectNodeDisconnectnodePost**](Apis/ControlMethodsApi.md#disconnectnodedisconnectnodepost) | **POST** /disconnectnode | Disconnect from a specified node |
*ControlMethodsApi* | [**encryptWalletEncryptwalletPost**](Apis/ControlMethodsApi.md#encryptwalletencryptwalletpost) | **POST** /encryptwallet | Encrypt the wallet with a passphrase |
*ControlMethodsApi* | [**getDeprecationInfoGetdeprecationinfoGet**](Apis/ControlMethodsApi.md#getdeprecationinfogetdeprecationinfoget) | **GET** /getdeprecationinfo | Get deprecation information of the current version |
*ControlMethodsApi* | [**getInfoGetinfoGet**](Apis/ControlMethodsApi.md#getinfogetinfoget) | **GET** /getinfo | Get various state info |
*ControlMethodsApi* | [**keypoolRefillKeypoolrefillPost**](Apis/ControlMethodsApi.md#keypoolrefillkeypoolrefillpost) | **POST** /keypoolrefill | Refill the keypool |
*ControlMethodsApi* | [**lockUnspentLockunspentPost**](Apis/ControlMethodsApi.md#lockunspentlockunspentpost) | **POST** /lockunspent | Lock or unlock unspent transaction outputs |
*ControlMethodsApi* | [**moveMovePost**](Apis/ControlMethodsApi.md#movemovepost) | **POST** /move | Move amount from one account to another |
*ControlMethodsApi* | [**setAccountSetaccountPost**](Apis/ControlMethodsApi.md#setaccountsetaccountpost) | **POST** /setaccount | Associate a Pastel address with an account |
*ControlMethodsApi* | [**setBanSetbanPost**](Apis/ControlMethodsApi.md#setbansetbanpost) | **POST** /setban | Add or Remove an IP/Subnet from the Ban List |
*ControlMethodsApi* | [**storageFeeStoragefeePost**](Apis/ControlMethodsApi.md#storagefeestoragefeepost) | **POST** /storagefee | Interact with Storage Fee and related actions |
*ControlMethodsApi* | [**storagefeeSetfeeStoragefeeSetfeePost**](Apis/ControlMethodsApi.md#storagefeesetfeestoragefeesetfeepost) | **POST** /storagefee/setfee | Set a new fee for a specified fee type |
*ControlMethodsApi* | [**walletPassphraseWalletpassphrasePost**](Apis/ControlMethodsApi.md#walletpassphrasewalletpassphrasepost) | **POST** /walletpassphrase | Unlock the wallet |
*ControlMethodsApi* | [**walletlockWalletlockPost**](Apis/ControlMethodsApi.md#walletlockwalletlockpost) | **POST** /walletlock | Lock the wallet |
| *MainApi* | [**addMultisigAddressAddmultisigaddressPost**](Apis/MainApi.md#addmultisigaddressaddmultisigaddresspost) | **POST** /addmultisigaddress | Add a multisignature address |
*MainApi* | [**addNodeAddnodePost**](Apis/MainApi.md#addnodeaddnodepost) | **POST** /addnode | Add, remove, or try a connection to a node |
*MainApi* | [**backupWalletBackupwalletPost**](Apis/MainApi.md#backupwalletbackupwalletpost) | **POST** /backupwallet | Backup the wallet to a destination |
*MainApi* | [**changeWalletPassphraseWalletpassphrasechangePost**](Apis/MainApi.md#changewalletpassphrasewalletpassphrasechangepost) | **POST** /walletpassphrasechange | Change the wallet passphrase |
*MainApi* | [**createMultisigCreatemultisigPost**](Apis/MainApi.md#createmultisigcreatemultisigpost) | **POST** /createmultisig | Create a multisig address |
*MainApi* | [**createRawTransactionCreaterawtransactionPost**](Apis/MainApi.md#createrawtransactioncreaterawtransactionpost) | **POST** /createrawtransaction | Create a raw transaction |
*MainApi* | [**decodeRawTransactionDecoderawtransactionPost**](Apis/MainApi.md#decoderawtransactiondecoderawtransactionpost) | **POST** /decoderawtransaction | Decode a raw transaction |
*MainApi* | [**decodeScriptDecodescriptPost**](Apis/MainApi.md#decodescriptdecodescriptpost) | **POST** /decodescript | Decode a hex-encoded script |
*MainApi* | [**disconnectNodeDisconnectnodePost**](Apis/MainApi.md#disconnectnodedisconnectnodepost) | **POST** /disconnectnode | Disconnect from a specified node |
*MainApi* | [**dumpPrivKeyDumpprivkeyGet**](Apis/MainApi.md#dumpprivkeydumpprivkeyget) | **GET** /dumpprivkey | Reveal the private key for a given address |
*MainApi* | [**dumpWalletDumpwalletPost**](Apis/MainApi.md#dumpwalletdumpwalletpost) | **POST** /dumpwallet | Dump wallet keys |
*MainApi* | [**encryptWalletEncryptwalletPost**](Apis/MainApi.md#encryptwalletencryptwalletpost) | **POST** /encryptwallet | Encrypt the wallet with a passphrase |
*MainApi* | [**estimateFeeEstimatefeeGet**](Apis/MainApi.md#estimatefeeestimatefeeget) | **GET** /estimatefee | Estimate the transaction fee per kilobyte |
*MainApi* | [**estimateNftStorageFeeTicketsToolsEstimatenftstoragefeeGet**](Apis/MainApi.md#estimatenftstoragefeeticketstoolsestimatenftstoragefeeget) | **GET** /tickets/tools/estimatenftstoragefee | Estimate storage fee for NFT registration |
*MainApi* | [**estimatePriorityEstimatepriorityGet**](Apis/MainApi.md#estimatepriorityestimatepriorityget) | **GET** /estimatepriority | Estimate the transaction priority for zero-fee confirmation |
*MainApi* | [**executeMasternodeCommandMasternodeCommandPost**](Apis/MainApi.md#executemasternodecommandmasternodecommandpost) | **POST** /masternode/command | Execute masternode related actions |
*MainApi* | [**fixMissingTransactionsFixmissingtxsStartingHeightGet**](Apis/MainApi.md#fixmissingtransactionsfixmissingtxsstartingheightget) | **GET** /fixmissingtxs/{starting_height} | Fix Missing Transactions |
*MainApi* | [**fundRawTransactionFundrawtransactionPost**](Apis/MainApi.md#fundrawtransactionfundrawtransactionpost) | **POST** /fundrawtransaction | Add inputs to a transaction |
*MainApi* | [**generateBlocksGeneratePost**](Apis/MainApi.md#generateblocksgeneratepost) | **POST** /generate | Mine blocks immediately |
*MainApi* | [**generatePastelIdNewkeyPastelidNewkeyPost**](Apis/MainApi.md#generatepastelidnewkeypastelidnewkeypost) | **POST** /pastelid/newkey | Generate new Pastel ID and keys |
*MainApi* | [**generateReportGenerateReportReportNameGet**](Apis/MainApi.md#generatereportgeneratereportreportnameget) | **GET** /generate-report/{report_name} | Generate various reports |
*MainApi* | [**getAccountAddressGetaccountaddressGet**](Apis/MainApi.md#getaccountaddressgetaccountaddressget) | **GET** /getaccountaddress | Get the current Pastel address for receiving payments |
*MainApi* | [**getAccountGetaccountZcashaddressGet**](Apis/MainApi.md#getaccountgetaccountzcashaddressget) | **GET** /getaccount/{zcashaddress} | Get the account associated with a Pastel address |
*MainApi* | [**getActionFeesStoragefeeGetactionfeesGet**](Apis/MainApi.md#getactionfeesstoragefeegetactionfeesget) | **GET** /storagefee/getactionfees | Get action fees based on data size |
*MainApi* | [**getAddedNodeInfoGetaddednodeinfoGet**](Apis/MainApi.md#getaddednodeinfogetaddednodeinfoget) | **GET** /getaddednodeinfo | Get information about added nodes |
*MainApi* | [**getAddressMempoolGetaddressmempoolGet**](Apis/MainApi.md#getaddressmempoolgetaddressmempoolget) | **GET** /getaddressmempool | Get all mempool deltas for an address |
*MainApi* | [**getAddressesByAccountGetaddressesbyaccountGet**](Apis/MainApi.md#getaddressesbyaccountgetaddressesbyaccountget) | **GET** /getaddressesbyaccount | Get addresses by account |
*MainApi* | [**getBalanceGetbalanceGet**](Apis/MainApi.md#getbalancegetbalanceget) | **GET** /getbalance | Get the server's total available balance |
*MainApi* | [**getBestBlockHashGetbestblockhashGet**](Apis/MainApi.md#getbestblockhashgetbestblockhashget) | **GET** /getbestblockhash | Get the hash of the best block |
*MainApi* | [**getBlockCountGetblockcountGet**](Apis/MainApi.md#getblockcountgetblockcountget) | **GET** /getblockcount | Get the current block count |
*MainApi* | [**getBlockDeltasGetblockdeltasBlockHashGet**](Apis/MainApi.md#getblockdeltasgetblockdeltasblockhashget) | **GET** /getblockdeltas/{block_hash} | Get block deltas |
*MainApi* | [**getBlockGetblockGet**](Apis/MainApi.md#getblockgetblockget) | **GET** /getblock | Get block data |
*MainApi* | [**getBlockHashGetblockhashGet**](Apis/MainApi.md#getblockhashgetblockhashget) | **GET** /getblockhash | Get the hash of a block at a specific index |
*MainApi* | [**getBlockHeaderGetblockheaderBlockHashGet**](Apis/MainApi.md#getblockheadergetblockheaderblockhashget) | **GET** /getblockheader/{block_hash} | Get information about a block header |
*MainApi* | [**getBlockSubsidyGetblocksubsidyGet**](Apis/MainApi.md#getblocksubsidygetblocksubsidyget) | **GET** /getblocksubsidy | Get block subsidy reward information |
*MainApi* | [**getBlockTemplateGetblocktemplatePost**](Apis/MainApi.md#getblocktemplategetblocktemplatepost) | **POST** /getblocktemplate | Get data needed to construct a block to work on |
*MainApi* | [**getBlockchainInfoGetblockchaininfoGet**](Apis/MainApi.md#getblockchaininfogetblockchaininfoget) | **GET** /getblockchaininfo | Get blockchain information |
*MainApi* | [**getChainTipsGetchaintipsGet**](Apis/MainApi.md#getchaintipsgetchaintipsget) | **GET** /getchaintips | Get information about all known chain tips |
*MainApi* | [**getConnectionCountGetconnectioncountGet**](Apis/MainApi.md#getconnectioncountgetconnectioncountget) | **GET** /getconnectioncount | Get the number of connections to other nodes |
*MainApi* | [**getDeprecationInfoGetdeprecationinfoGet**](Apis/MainApi.md#getdeprecationinfogetdeprecationinfoget) | **GET** /getdeprecationinfo | Get deprecation information of the current version |
*MainApi* | [**getDifficultyGetdifficultyGet**](Apis/MainApi.md#getdifficultygetdifficultyget) | **GET** /getdifficulty | Get the current proof-of-work difficulty |
*MainApi* | [**getFeeScheduleGetfeescheduleGet**](Apis/MainApi.md#getfeeschedulegetfeescheduleget) | **GET** /getfeeschedule | Get the current fee schedule |
*MainApi* | [**getGenerateGetgenerateGet**](Apis/MainApi.md#getgenerategetgenerateget) | **GET** /getgenerate | Check if the server is set to generate coins |
*MainApi* | [**getInfoGetinfoGet**](Apis/MainApi.md#getinfogetinfoget) | **GET** /getinfo | Get various state info |
*MainApi* | [**getLocalSolpsGetlocalsolpsGet**](Apis/MainApi.md#getlocalsolpsgetlocalsolpsget) | **GET** /getlocalsolps | Get average local solutions per second |
*MainApi* | [**getMemoryInfoGetmemoryinfoGet**](Apis/MainApi.md#getmemoryinfogetmemoryinfoget) | **GET** /getmemoryinfo | Get memory usage information |
*MainApi* | [**getMempoolInfoGetmempoolinfoGet**](Apis/MainApi.md#getmempoolinfogetmempoolinfoget) | **GET** /getmempoolinfo | Get active state of the TX memory pool |
*MainApi* | [**getMiningInfoGetmininginfoGet**](Apis/MainApi.md#getmininginfogetmininginfoget) | **GET** /getmininginfo | Get mining-related information |
*MainApi* | [**getNetTotalsGetnettotalsGet**](Apis/MainApi.md#getnettotalsgetnettotalsget) | **GET** /getnettotals | Get network traffic information |
*MainApi* | [**getNetworkInfoGetnetworkinfoGet**](Apis/MainApi.md#getnetworkinfogetnetworkinfoget) | **GET** /getnetworkinfo | Get various state info regarding P2P networking |
*MainApi* | [**getNetworkSolpsGetnetworksolpsGet**](Apis/MainApi.md#getnetworksolpsgetnetworksolpsget) | **GET** /getnetworksolps | Get estimated network solutions per second |
*MainApi* | [**getNetworksInfoGetnetworksinfoGet**](Apis/MainApi.md#getnetworksinfogetnetworksinfoget) | **GET** /getnetworksinfo | Get information about all the networks |
*MainApi* | [**getNewAddressGetnewaddressGet**](Apis/MainApi.md#getnewaddressgetnewaddressget) | **GET** /getnewaddress | Generate a new Pastel address |
*MainApi* | [**getNextBlockSubsidyGetnextblocksubsidyGet**](Apis/MainApi.md#getnextblocksubsidygetnextblocksubsidyget) | **GET** /getnextblocksubsidy | Get subsidy rewards for the next block |
*MainApi* | [**getPeerInfoGetpeerinfoGet**](Apis/MainApi.md#getpeerinfogetpeerinfoget) | **GET** /getpeerinfo | Get data about each connected network node |
*MainApi* | [**getRawChangeAddressGetrawchangeaddressGet**](Apis/MainApi.md#getrawchangeaddressgetrawchangeaddressget) | **GET** /getrawchangeaddress | Get a new Pastel address for receiving change |
*MainApi* | [**getRawMempoolGetrawmempoolGet**](Apis/MainApi.md#getrawmempoolgetrawmempoolget) | **GET** /getrawmempool | Get all transaction IDs in memory pool |
*MainApi* | [**getRawTransactionGetrawtransactionPost**](Apis/MainApi.md#getrawtransactiongetrawtransactionpost) | **POST** /getrawtransaction | Get the raw transaction data |
*MainApi* | [**getReceivedByAccountGetreceivedbyaccountGet**](Apis/MainApi.md#getreceivedbyaccountgetreceivedbyaccountget) | **GET** /getreceivedbyaccount | Get the total amount received by an account |
*MainApi* | [**getReceivedByAddressGetreceivedbyaddressGet**](Apis/MainApi.md#getreceivedbyaddressgetreceivedbyaddressget) | **GET** /getreceivedbyaddress | Get the total amount received by a Pastel address |
*MainApi* | [**getStorageFeeGetFeeStoragefeeGetfeeGet**](Apis/MainApi.md#getstoragefeegetfeestoragefeegetfeeget) | **GET** /storagefee/getfee | Get the storage fee |
*MainApi* | [**getStorageFeesStoragefeeGetfeesGet**](Apis/MainApi.md#getstoragefeesstoragefeegetfeesget) | **GET** /storagefee/getfees | Get the current storage fees |
*MainApi* | [**getTotalStorageFeeTicketsToolsGettotalstoragefeePost**](Apis/MainApi.md#gettotalstoragefeeticketstoolsgettotalstoragefeepost) | **POST** /tickets/tools/gettotalstoragefee | Calculate Total Storage Fee for NFT Registration |
*MainApi* | [**getTransactionGettransactionTxidGet**](Apis/MainApi.md#gettransactiongettransactiontxidget) | **GET** /gettransaction/{txid} | Get detailed information about a transaction |
*MainApi* | [**getTxOutGettxoutGet**](Apis/MainApi.md#gettxoutgettxoutget) | **GET** /gettxout | Get details about an unspent transaction output |
*MainApi* | [**getTxOutProofGettxoutproofGet**](Apis/MainApi.md#gettxoutproofgettxoutproofget) | **GET** /gettxoutproof | Get proof of transaction inclusion in a block |
*MainApi* | [**getTxOutSetInfoGettxoutsetinfoGet**](Apis/MainApi.md#gettxoutsetinfogettxoutsetinfoget) | **GET** /gettxoutsetinfo | Get statistics about the unspent transaction output set |
*MainApi* | [**getTxfeeGettxfeeTxidGet**](Apis/MainApi.md#gettxfeegettxfeetxidget) | **GET** /gettxfee/{txid} | Get transaction fee by txid |
*MainApi* | [**getWalletInfoGetwalletinfoGet**](Apis/MainApi.md#getwalletinfogetwalletinfoget) | **GET** /getwalletinfo | Get wallet state information |
*MainApi* | [**governanceActionGovernancePost**](Apis/MainApi.md#governanceactiongovernancepost) | **POST** /governance | Cast a vote or list governance tickets |
*MainApi* | [**importAddressImportaddressPost**](Apis/MainApi.md#importaddressimportaddresspost) | **POST** /importaddress | Import an address |
*MainApi* | [**importPrivKeyImportprivkeyPost**](Apis/MainApi.md#importprivkeyimportprivkeypost) | **POST** /importprivkey | Import a private key |
*MainApi* | [**importWalletImportwalletPost**](Apis/MainApi.md#importwalletimportwalletpost) | **POST** /importwallet | Import a wallet from a dump file |
*MainApi* | [**initializeMasternodeMasternodeInitPost**](Apis/MainApi.md#initializemasternodemasternodeinitpost) | **POST** /masternode/init | Initialize masternode |
*MainApi* | [**invalidateBlockInvalidateblockPost**](Apis/MainApi.md#invalidateblockinvalidateblockpost) | **POST** /invalidateblock | Mark a block as permanently invalid |
*MainApi* | [**keypoolRefillKeypoolrefillPost**](Apis/MainApi.md#keypoolrefillkeypoolrefillpost) | **POST** /keypoolrefill | Refill the keypool |
*MainApi* | [**listAccountsListaccountsGet**](Apis/MainApi.md#listaccountslistaccountsget) | **GET** /listaccounts | List account balances |
*MainApi* | [**listAddressAmountsListaddressamountsGet**](Apis/MainApi.md#listaddressamountslistaddressamountsget) | **GET** /listaddressamounts | List balance on each address |
*MainApi* | [**listAddressGroupingsListaddressgroupingsGet**](Apis/MainApi.md#listaddressgroupingslistaddressgroupingsget) | **GET** /listaddressgroupings | List groups of addresses with common ownership |
*MainApi* | [**listBannedListbannedGet**](Apis/MainApi.md#listbannedlistbannedget) | **GET** /listbanned | List all banned IPs/Subnets |
*MainApi* | [**listLockUnspentListlockunspentGet**](Apis/MainApi.md#listlockunspentlistlockunspentget) | **GET** /listlockunspent | List Temporarily Unspendable Outputs |
*MainApi* | [**listMasternodeOutputsMasternodeOutputsGet**](Apis/MainApi.md#listmasternodeoutputsmasternodeoutputsget) | **GET** /masternode/outputs | List masternode outputs |
*MainApi* | [**listReceivedByAddressListreceivedbyaddressGet**](Apis/MainApi.md#listreceivedbyaddresslistreceivedbyaddressget) | **GET** /listreceivedbyaddress | List balances by receiving address |
*MainApi* | [**listShieldedAddressesZListaddressesGet**](Apis/MainApi.md#listshieldedaddresseszlistaddressesget) | **GET** /z_listaddresses | List Shielded Addresses |
*MainApi* | [**listSinceBlockListsinceblockPost**](Apis/MainApi.md#listsinceblocklistsinceblockpost) | **POST** /listsinceblock | List transactions since a specific block |
*MainApi* | [**listTicketsTicketsListGet**](Apis/MainApi.md#listticketsticketslistget) | **GET** /tickets/list | List tickets of a specific type |
*MainApi* | [**listTransactionsListtransactionsGet**](Apis/MainApi.md#listtransactionslisttransactionsget) | **GET** /listtransactions | List recent transactions |
*MainApi* | [**listUnspentListunspentGet**](Apis/MainApi.md#listunspentlistunspentget) | **GET** /listunspent | List Unspent Transaction Outputs |
*MainApi* | [**lockUnspentLockunspentPost**](Apis/MainApi.md#lockunspentlockunspentpost) | **POST** /lockunspent | Lock or unlock unspent transaction outputs |
*MainApi* | [**masternodeBroadcastMasternodebroadcastPost**](Apis/MainApi.md#masternodebroadcastmasternodebroadcastpost) | **POST** /masternodebroadcast | Create and relay masternode broadcast messages |
*MainApi* | [**masternodeClearCacheMasternodeClearCachePost**](Apis/MainApi.md#masternodeclearcachemasternodeclearcachepost) | **POST** /masternode/clear-cache | Clear Masternode Cache Items |
*MainApi* | [**masternodeMakeConfMasternodeMakeConfPost**](Apis/MainApi.md#masternodemakeconfmasternodemakeconfpost) | **POST** /masternode/make_conf | Create Masternode Configuration |
*MainApi* | [**masternodeMessageMasternodeMessagePost**](Apis/MainApi.md#masternodemessagemasternodemessagepost) | **POST** /masternode/message | Interact with Masternode messages |
*MainApi* | [**masternodePoseBanScoreMasternodePoseBanScorePost**](Apis/MainApi.md#masternodeposebanscoremasternodeposebanscorepost) | **POST** /masternode_pose_ban_score | Manage MasterNode PoSe Ban Score |
*MainApi* | [**masternodelistMasternodelistGet**](Apis/MainApi.md#masternodelistmasternodelistget) | **GET** /masternodelist | Get a list of masternodes in different modes |
*MainApi* | [**moveMovePost**](Apis/MainApi.md#movemovepost) | **POST** /move | Move amount from one account to another |
*MainApi* | [**pastelidNewkeyPastelidNewkeyPost**](Apis/MainApi.md#pastelidnewkeypastelidnewkeypost) | **POST** /pastelid_newkey | Generate new Pastel ID and associated keys |
*MainApi* | [**pastelidPasswdPastelidPasswdPost**](Apis/MainApi.md#pastelidpasswdpastelidpasswdpost) | **POST** /pastelid/passwd | Change passphrase for PastelID secure container |
*MainApi* | [**pastelidSignFilePastelidSignfilePost**](Apis/MainApi.md#pastelidsignfilepastelidsignfilepost) | **POST** /pastelid/signfile | Sign a file with a Pastel ID |
*MainApi* | [**pastelidVerifyFilePastelidVerifyFilePost**](Apis/MainApi.md#pastelidverifyfilepastelidverifyfilepost) | **POST** /pastelid/verify-file | Verify a file's signature with a Pastel ID |
*MainApi* | [**pastelidVerifyPastelidVerifyPost**](Apis/MainApi.md#pastelidverifypastelidverifypost) | **POST** /pastelid/verify | Verify a signature with PastelID |
*MainApi* | [**pingPingGet**](Apis/MainApi.md#pingpingget) | **GET** /ping | Send a ping to all nodes |
*MainApi* | [**prioritiseTransactionPrioritisetransactionPost**](Apis/MainApi.md#prioritisetransactionprioritisetransactionpost) | **POST** /prioritisetransaction | Prioritise a transaction for mining |
*MainApi* | [**reconsiderBlockReconsiderblockPost**](Apis/MainApi.md#reconsiderblockreconsiderblockpost) | **POST** /reconsiderblock | Reconsider a previously invalidated block |
*MainApi* | [**refreshMiningMnidInfoRefreshminingmnidinfoGet**](Apis/MainApi.md#refreshminingmnidinforefreshminingmnidinfoget) | **GET** /refreshminingmnidinfo | Refresh mining MNID information |
*MainApi* | [**registerActionTicketTicketsRegisterActionPost**](Apis/MainApi.md#registeractionticketticketsregisteractionpost) | **POST** /tickets/register_action | Register new Action ticket |
*MainApi* | [**registerNftTicketTicketsRegisterNftPost**](Apis/MainApi.md#registernftticketticketsregisternftpost) | **POST** /tickets/register/nft | Register a new NFT ticket |
*MainApi* | [**registerRoyaltyTicketTicketsRegisterRoyaltyPost**](Apis/MainApi.md#registerroyaltyticketticketsregisterroyaltypost) | **POST** /tickets/register_royalty | Register new change payee of the NFT royalty ticket |
*MainApi* | [**registerTransferTicketTicketsRegisterTransferPost**](Apis/MainApi.md#registertransferticketticketsregistertransferpost) | **POST** /tickets/register/transfer | Register a transfer ticket |
*MainApi* | [**registerUsernameTicketsRegisterUsernamePost**](Apis/MainApi.md#registerusernameticketsregisterusernamepost) | **POST** /tickets/register/username | Register a Username Change Request ticket |
*MainApi* | [**resendWalletTransactionsResendwallettransactionsPost**](Apis/MainApi.md#resendwallettransactionsresendwallettransactionspost) | **POST** /resendwallettransactions | Re-broadcast unconfirmed wallet transactions |
*MainApi* | [**retrieveChaindataChaindataRetrievePost**](Apis/MainApi.md#retrievechaindatachaindataretrievepost) | **POST** /chaindata/retrieve | Retrieve data from the blockchain |
*MainApi* | [**scanForMissingTxsScanformissingtxsPost**](Apis/MainApi.md#scanformissingtxsscanformissingtxspost) | **POST** /scanformissingtxs | Scan for missing transactions |
*MainApi* | [**sendFromSendfromPost**](Apis/MainApi.md#sendfromsendfrompost) | **POST** /sendfrom | Send amount from an account to a Pastel address |
*MainApi* | [**sendManySendmanyPost**](Apis/MainApi.md#sendmanysendmanypost) | **POST** /sendmany | Send multiple transactions |
*MainApi* | [**sendRawTransactionSendrawtransactionPost**](Apis/MainApi.md#sendrawtransactionsendrawtransactionpost) | **POST** /sendrawtransaction | Submit a raw transaction to the network |
*MainApi* | [**sendToAddressSendtoaddressPost**](Apis/MainApi.md#sendtoaddresssendtoaddresspost) | **POST** /sendtoaddress | Send an amount to a given address |
*MainApi* | [**setAccountSetaccountPost**](Apis/MainApi.md#setaccountsetaccountpost) | **POST** /setaccount | Associate a Pastel address with an account |
*MainApi* | [**setBanSetbanPost**](Apis/MainApi.md#setbansetbanpost) | **POST** /setban | Add or Remove an IP/Subnet from the Ban List |
*MainApi* | [**setGenerateSetgeneratePost**](Apis/MainApi.md#setgeneratesetgeneratepost) | **POST** /setgenerate | Set generation on or off |
*MainApi* | [**setTxFeeSettxfeePost**](Apis/MainApi.md#settxfeesettxfeepost) | **POST** /settxfee | Set the transaction fee per kB |
*MainApi* | [**signMessageSignmessagePost**](Apis/MainApi.md#signmessagesignmessagepost) | **POST** /signmessage | Sign a message with the private key of a t-addr |
*MainApi* | [**signRawTransactionSignrawtransactionPost**](Apis/MainApi.md#signrawtransactionsignrawtransactionpost) | **POST** /signrawtransaction | Sign a raw transaction |
*MainApi* | [**signWithPastelIdPastelidSignPost**](Apis/MainApi.md#signwithpastelidpastelidsignpost) | **POST** /pastelid/sign | Sign a text with Pastel ID |
*MainApi* | [**storageFeeStoragefeePost**](Apis/MainApi.md#storagefeestoragefeepost) | **POST** /storagefee | Interact with Storage Fee and related actions |
*MainApi* | [**storagefeeSetfeeStoragefeeSetfeePost**](Apis/MainApi.md#storagefeesetfeestoragefeesetfeepost) | **POST** /storagefee/setfee | Set a new fee for a specified fee type |
*MainApi* | [**storeChaindataChaindataStorePost**](Apis/MainApi.md#storechaindatachaindatastorepost) | **POST** /chaindata/store | Store data in the blockchain |
*MainApi* | [**submitBlockSubmitblockPost**](Apis/MainApi.md#submitblocksubmitblockpost) | **POST** /submitblock | Submit a new block to the network |
*MainApi* | [**ticketsFindByLabelTicketsFindbylabelTicketTypeLabelGet**](Apis/MainApi.md#ticketsfindbylabelticketsfindbylabeltickettypelabelget) | **GET** /tickets/findbylabel/{ticket_type}/{label} | Find tickets by label |
*MainApi* | [**ticketsFindTicketsFindGet**](Apis/MainApi.md#ticketsfindticketsfindget) | **GET** /tickets/find | Find Pastel tickets |
*MainApi* | [**ticketsGetTicketsGetGet**](Apis/MainApi.md#ticketsgetticketsgetget) | **GET** /tickets/get | Get a Pastel ticket by transaction ID |
*MainApi* | [**ticketsRegisterAcceptTicketsRegisterAcceptPost**](Apis/MainApi.md#ticketsregisteracceptticketsregisteracceptpost) | **POST** /tickets/register/accept | Register an accept ticket |
*MainApi* | [**ticketsRegisterCollectionTicketsRegistercollectionPost**](Apis/MainApi.md#ticketsregistercollectionticketsregistercollectionpost) | **POST** /tickets/registercollection | Register a collection ticket |
*MainApi* | [**ticketsRegisterDownTicketsRegisterDownPost**](Apis/MainApi.md#ticketsregisterdownticketsregisterdownpost) | **POST** /tickets/register/down | Register a Take Down Request Ticket |
*MainApi* | [**ticketsRegisterEthereumAddressTicketsRegisterEthereumaddressPost**](Apis/MainApi.md#ticketsregisterethereumaddressticketsregisterethereumaddresspost) | **POST** /tickets/register/ethereumaddress | Register Ethereum Address Change Request |
*MainApi* | [**ticketsRegisterIdTicketsRegisterIdPost**](Apis/MainApi.md#ticketsregisteridticketsregisteridpost) | **POST** /tickets/register_id | Register Pastel ID identity |
*MainApi* | [**ticketsRegisterMnidTicketsRegisterMnidPost**](Apis/MainApi.md#ticketsregistermnidticketsregistermnidpost) | **POST** /tickets/register/mnid | Register Masternode PastelID |
*MainApi* | [**ticketsRegisterOfferTicketsRegisterOfferPost**](Apis/MainApi.md#ticketsregisterofferticketsregisterofferpost) | **POST** /tickets/register/offer | Register an offer ticket |
*MainApi* | [**ticketsTicketsCommandGet**](Apis/MainApi.md#ticketsticketscommandget) | **GET** /tickets/{command} | Execute Pastel Ticket Commands |
*MainApi* | [**ticketsToolsSearchthumbidsTicketsToolsSearchthumbidsPost**](Apis/MainApi.md#ticketstoolssearchthumbidsticketstoolssearchthumbidspost) | **POST** /tickets/tools/searchthumbids | Search for NFT registration tickets and thumbnail hash |
*MainApi* | [**ticketsToolsTicketsToolsPost**](Apis/MainApi.md#ticketstoolsticketstoolspost) | **POST** /tickets/tools | Execute various ticket tools commands |
*MainApi* | [**validateAddressValidateaddressPost**](Apis/MainApi.md#validateaddressvalidateaddresspost) | **POST** /validateaddress | Validate a Pastel address |
*MainApi* | [**validateOwnershipTicketsToolsValidateownershipPost**](Apis/MainApi.md#validateownershipticketstoolsvalidateownershippost) | **POST** /tickets/tools/validateownership | Validate item ownership by Pastel ID |
*MainApi* | [**verifyChainVerifychainGet**](Apis/MainApi.md#verifychainverifychainget) | **GET** /verifychain | Verify the blockchain database |
*MainApi* | [**verifyMessageVerifymessagePost**](Apis/MainApi.md#verifymessageverifymessagepost) | **POST** /verifymessage | Verify a signed message |
*MainApi* | [**walletPassphraseWalletpassphrasePost**](Apis/MainApi.md#walletpassphrasewalletpassphrasepost) | **POST** /walletpassphrase | Unlock the wallet |
*MainApi* | [**walletlockWalletlockPost**](Apis/MainApi.md#walletlockwalletlockpost) | **POST** /walletlock | Lock the wallet |
*MainApi* | [**zExportKeyZExportkeyPost**](Apis/MainApi.md#zexportkeyzexportkeypost) | **POST** /z_exportkey | Reveal the private key corresponding to a z-address |
*MainApi* | [**zExportViewingKeyZExportviewingkeyGet**](Apis/MainApi.md#zexportviewingkeyzexportviewingkeyget) | **GET** /z_exportviewingkey | Export the viewing key for a Z-address |
*MainApi* | [**zExportWalletZExportwalletPost**](Apis/MainApi.md#zexportwalletzexportwalletpost) | **POST** /z_exportwallet | Export wallet keys |
*MainApi* | [**zGetBalanceZGetbalanceAddressGet**](Apis/MainApi.md#zgetbalancezgetbalanceaddressget) | **GET** /z_getbalance/{address} | Get the balance of an address |
*MainApi* | [**zGetNewAddressZGetnewaddressGet**](Apis/MainApi.md#zgetnewaddresszgetnewaddressget) | **GET** /z_getnewaddress | Generate a new shielded address |
*MainApi* | [**zGetNotesCountZGetnotescountGet**](Apis/MainApi.md#zgetnotescountzgetnotescountget) | **GET** /z_getnotescount | Get the count of sapling notes in the wallet |
*MainApi* | [**zGetOperationStatusZGetoperationstatusGet**](Apis/MainApi.md#zgetoperationstatuszgetoperationstatusget) | **GET** /z_getoperationstatus | Get the status of asynchronous operations |
*MainApi* | [**zGetTotalBalanceZGettotalbalanceGet**](Apis/MainApi.md#zgettotalbalancezgettotalbalanceget) | **GET** /z_gettotalbalance | Get the total balance of both transparent and private funds |
*MainApi* | [**zGetoperationresultZGetoperationresultGet**](Apis/MainApi.md#zgetoperationresultzgetoperationresultget) | **GET** /z_getoperationresult | Retrieve the result and status of Zcash operations |
*MainApi* | [**zImportKeyZImportkeyGet**](Apis/MainApi.md#zimportkeyzimportkeyget) | **GET** /z_importkey | Import a Z key into the wallet |
*MainApi* | [**zImportViewingKeyZImportviewingkeyPost**](Apis/MainApi.md#zimportviewingkeyzimportviewingkeypost) | **POST** /z_importviewingkey | Import a viewing key into the wallet |
*MainApi* | [**zImportWalletZImportwalletPost**](Apis/MainApi.md#zimportwalletzimportwalletpost) | **POST** /z_importwallet | Import keys from a wallet export file |
*MainApi* | [**zListOperationIdsZListoperationidsGet**](Apis/MainApi.md#zlistoperationidszlistoperationidsget) | **GET** /z_listoperationids | List Operation IDs |
*MainApi* | [**zListReceivedByAddressZListreceivedbyaddressGet**](Apis/MainApi.md#zlistreceivedbyaddresszlistreceivedbyaddressget) | **GET** /z_listreceivedbyaddress | List amounts received by a z-address |
*MainApi* | [**zListunspentZListunspentGet**](Apis/MainApi.md#zlistunspentzlistunspentget) | **GET** /z_listunspent | List unspent shielded notes |
*MainApi* | [**zMergetoaddressZMergetoaddressPost**](Apis/MainApi.md#zmergetoaddresszmergetoaddresspost) | **POST** /z_mergetoaddress | Merge multiple UTXOs and notes into a single UTXO or note |
*MainApi* | [**zSendManyZSendmanyPost**](Apis/MainApi.md#zsendmanyzsendmanypost) | **POST** /z_sendmany | Send multiple times to multiple recipients |
*MainApi* | [**zShieldcoinbaseZShieldcoinbasePost**](Apis/MainApi.md#zshieldcoinbasezshieldcoinbasepost) | **POST** /z_shieldcoinbase | Shield transparent coinbase funds to a shielded zaddr |
*MainApi* | [**zValidateAddressZValidateaddressGet**](Apis/MainApi.md#zvalidateaddresszvalidateaddressget) | **GET** /z_validateaddress | Validate a Z address |
*MainApi* | [**zViewTransactionZViewtransactionTxidGet**](Apis/MainApi.md#zviewtransactionzviewtransactiontxidget) | **GET** /z_viewtransaction/{txid} | Get detailed shielded information about in-wallet transaction |
*MainApi* | [**zcBenchmarkZcbenchmarkPost**](Apis/MainApi.md#zcbenchmarkzcbenchmarkpost) | **POST** /zcbenchmark | Runs a benchmark of the selected type |
| *MiningMethodsApi* | [**generateBlocksGeneratePost**](Apis/MiningMethodsApi.md#generateblocksgeneratepost) | **POST** /generate | Mine blocks immediately |
*MiningMethodsApi* | [**getBlockSubsidyGetblocksubsidyGet**](Apis/MiningMethodsApi.md#getblocksubsidygetblocksubsidyget) | **GET** /getblocksubsidy | Get block subsidy reward information |
*MiningMethodsApi* | [**getBlockTemplateGetblocktemplatePost**](Apis/MiningMethodsApi.md#getblocktemplategetblocktemplatepost) | **POST** /getblocktemplate | Get data needed to construct a block to work on |
*MiningMethodsApi* | [**getDifficultyGetdifficultyGet**](Apis/MiningMethodsApi.md#getdifficultygetdifficultyget) | **GET** /getdifficulty | Get the current proof-of-work difficulty |
*MiningMethodsApi* | [**getGenerateGetgenerateGet**](Apis/MiningMethodsApi.md#getgenerategetgenerateget) | **GET** /getgenerate | Check if the server is set to generate coins |
*MiningMethodsApi* | [**getLocalSolpsGetlocalsolpsGet**](Apis/MiningMethodsApi.md#getlocalsolpsgetlocalsolpsget) | **GET** /getlocalsolps | Get average local solutions per second |
*MiningMethodsApi* | [**getMiningInfoGetmininginfoGet**](Apis/MiningMethodsApi.md#getmininginfogetmininginfoget) | **GET** /getmininginfo | Get mining-related information |
*MiningMethodsApi* | [**getNetworkSolpsGetnetworksolpsGet**](Apis/MiningMethodsApi.md#getnetworksolpsgetnetworksolpsget) | **GET** /getnetworksolps | Get estimated network solutions per second |
*MiningMethodsApi* | [**prioritiseTransactionPrioritisetransactionPost**](Apis/MiningMethodsApi.md#prioritisetransactionprioritisetransactionpost) | **POST** /prioritisetransaction | Prioritise a transaction for mining |
*MiningMethodsApi* | [**refreshMiningMnidInfoRefreshminingmnidinfoGet**](Apis/MiningMethodsApi.md#refreshminingmnidinforefreshminingmnidinfoget) | **GET** /refreshminingmnidinfo | Refresh mining MNID information |
*MiningMethodsApi* | [**setGenerateSetgeneratePost**](Apis/MiningMethodsApi.md#setgeneratesetgeneratepost) | **POST** /setgenerate | Set generation on or off |
| *NetworkMethodsApi* | [**addNodeAddnodePost**](Apis/NetworkMethodsApi.md#addnodeaddnodepost) | **POST** /addnode | Add, remove, or try a connection to a node |
*NetworkMethodsApi* | [**getAddedNodeInfoGetaddednodeinfoGet**](Apis/NetworkMethodsApi.md#getaddednodeinfogetaddednodeinfoget) | **GET** /getaddednodeinfo | Get information about added nodes |
*NetworkMethodsApi* | [**getConnectionCountGetconnectioncountGet**](Apis/NetworkMethodsApi.md#getconnectioncountgetconnectioncountget) | **GET** /getconnectioncount | Get the number of connections to other nodes |
*NetworkMethodsApi* | [**getNetTotalsGetnettotalsGet**](Apis/NetworkMethodsApi.md#getnettotalsgetnettotalsget) | **GET** /getnettotals | Get network traffic information |
*NetworkMethodsApi* | [**getNetworkInfoGetnetworkinfoGet**](Apis/NetworkMethodsApi.md#getnetworkinfogetnetworkinfoget) | **GET** /getnetworkinfo | Get various state info regarding P2P networking |
*NetworkMethodsApi* | [**getNetworksInfoGetnetworksinfoGet**](Apis/NetworkMethodsApi.md#getnetworksinfogetnetworksinfoget) | **GET** /getnetworksinfo | Get information about all the networks |
*NetworkMethodsApi* | [**getPeerInfoGetpeerinfoGet**](Apis/NetworkMethodsApi.md#getpeerinfogetpeerinfoget) | **GET** /getpeerinfo | Get data about each connected network node |
*NetworkMethodsApi* | [**listBannedListbannedGet**](Apis/NetworkMethodsApi.md#listbannedlistbannedget) | **GET** /listbanned | List all banned IPs/Subnets |
| *RawTransactionMethodsApi* | [**createRawTransactionCreaterawtransactionPost**](Apis/RawTransactionMethodsApi.md#createrawtransactioncreaterawtransactionpost) | **POST** /createrawtransaction | Create a raw transaction |
*RawTransactionMethodsApi* | [**decodeRawTransactionDecoderawtransactionPost**](Apis/RawTransactionMethodsApi.md#decoderawtransactiondecoderawtransactionpost) | **POST** /decoderawtransaction | Decode a raw transaction |
*RawTransactionMethodsApi* | [**fundRawTransactionFundrawtransactionPost**](Apis/RawTransactionMethodsApi.md#fundrawtransactionfundrawtransactionpost) | **POST** /fundrawtransaction | Add inputs to a transaction |
*RawTransactionMethodsApi* | [**getRawChangeAddressGetrawchangeaddressGet**](Apis/RawTransactionMethodsApi.md#getrawchangeaddressgetrawchangeaddressget) | **GET** /getrawchangeaddress | Get a new Pastel address for receiving change |
*RawTransactionMethodsApi* | [**getRawTransactionGetrawtransactionPost**](Apis/RawTransactionMethodsApi.md#getrawtransactiongetrawtransactionpost) | **POST** /getrawtransaction | Get the raw transaction data |
*RawTransactionMethodsApi* | [**getTxOutProofGettxoutproofGet**](Apis/RawTransactionMethodsApi.md#gettxoutproofgettxoutproofget) | **GET** /gettxoutproof | Get proof of transaction inclusion in a block |
*RawTransactionMethodsApi* | [**sendFromSendfromPost**](Apis/RawTransactionMethodsApi.md#sendfromsendfrompost) | **POST** /sendfrom | Send amount from an account to a Pastel address |
*RawTransactionMethodsApi* | [**sendManySendmanyPost**](Apis/RawTransactionMethodsApi.md#sendmanysendmanypost) | **POST** /sendmany | Send multiple transactions |
*RawTransactionMethodsApi* | [**sendRawTransactionSendrawtransactionPost**](Apis/RawTransactionMethodsApi.md#sendrawtransactionsendrawtransactionpost) | **POST** /sendrawtransaction | Submit a raw transaction to the network |
*RawTransactionMethodsApi* | [**signRawTransactionSignrawtransactionPost**](Apis/RawTransactionMethodsApi.md#signrawtransactionsignrawtransactionpost) | **POST** /signrawtransaction | Sign a raw transaction |
*RawTransactionMethodsApi* | [**zMergetoaddressZMergetoaddressPost**](Apis/RawTransactionMethodsApi.md#zmergetoaddresszmergetoaddresspost) | **POST** /z_mergetoaddress | Merge multiple UTXOs and notes into a single UTXO or note |
*RawTransactionMethodsApi* | [**zSendManyZSendmanyPost**](Apis/RawTransactionMethodsApi.md#zsendmanyzsendmanypost) | **POST** /z_sendmany | Send multiple times to multiple recipients |
| *SupernodeMethodsApi* | [**executeMasternodeCommandMasternodeCommandPost**](Apis/SupernodeMethodsApi.md#executemasternodecommandmasternodecommandpost) | **POST** /masternode/command | Execute masternode related actions |
*SupernodeMethodsApi* | [**initializeMasternodeMasternodeInitPost**](Apis/SupernodeMethodsApi.md#initializemasternodemasternodeinitpost) | **POST** /masternode/init | Initialize masternode |
*SupernodeMethodsApi* | [**listMasternodeOutputsMasternodeOutputsGet**](Apis/SupernodeMethodsApi.md#listmasternodeoutputsmasternodeoutputsget) | **GET** /masternode/outputs | List masternode outputs |
*SupernodeMethodsApi* | [**masternodeBroadcastMasternodebroadcastPost**](Apis/SupernodeMethodsApi.md#masternodebroadcastmasternodebroadcastpost) | **POST** /masternodebroadcast | Create and relay masternode broadcast messages |
*SupernodeMethodsApi* | [**masternodeClearCacheMasternodeClearCachePost**](Apis/SupernodeMethodsApi.md#masternodeclearcachemasternodeclearcachepost) | **POST** /masternode/clear-cache | Clear Masternode Cache Items |
*SupernodeMethodsApi* | [**masternodeMakeConfMasternodeMakeConfPost**](Apis/SupernodeMethodsApi.md#masternodemakeconfmasternodemakeconfpost) | **POST** /masternode/make_conf | Create Masternode Configuration |
*SupernodeMethodsApi* | [**masternodeMessageMasternodeMessagePost**](Apis/SupernodeMethodsApi.md#masternodemessagemasternodemessagepost) | **POST** /masternode/message | Interact with Masternode messages |
*SupernodeMethodsApi* | [**masternodePoseBanScoreMasternodePoseBanScorePost**](Apis/SupernodeMethodsApi.md#masternodeposebanscoremasternodeposebanscorepost) | **POST** /masternode_pose_ban_score | Manage MasterNode PoSe Ban Score |
*SupernodeMethodsApi* | [**masternodelistMasternodelistGet**](Apis/SupernodeMethodsApi.md#masternodelistmasternodelistget) | **GET** /masternodelist | Get a list of masternodes in different modes |
| *TicketMethodsApi* | [**estimateNftStorageFeeTicketsToolsEstimatenftstoragefeeGet**](Apis/TicketMethodsApi.md#estimatenftstoragefeeticketstoolsestimatenftstoragefeeget) | **GET** /tickets/tools/estimatenftstoragefee | Estimate storage fee for NFT registration |
*TicketMethodsApi* | [**getTotalStorageFeeTicketsToolsGettotalstoragefeePost**](Apis/TicketMethodsApi.md#gettotalstoragefeeticketstoolsgettotalstoragefeepost) | **POST** /tickets/tools/gettotalstoragefee | Calculate Total Storage Fee for NFT Registration |
*TicketMethodsApi* | [**listTicketsTicketsListGet**](Apis/TicketMethodsApi.md#listticketsticketslistget) | **GET** /tickets/list | List tickets of a specific type |
*TicketMethodsApi* | [**registerActionTicketTicketsRegisterActionPost**](Apis/TicketMethodsApi.md#registeractionticketticketsregisteractionpost) | **POST** /tickets/register_action | Register new Action ticket |
*TicketMethodsApi* | [**registerNftTicketTicketsRegisterNftPost**](Apis/TicketMethodsApi.md#registernftticketticketsregisternftpost) | **POST** /tickets/register/nft | Register a new NFT ticket |
*TicketMethodsApi* | [**registerRoyaltyTicketTicketsRegisterRoyaltyPost**](Apis/TicketMethodsApi.md#registerroyaltyticketticketsregisterroyaltypost) | **POST** /tickets/register_royalty | Register new change payee of the NFT royalty ticket |
*TicketMethodsApi* | [**registerTransferTicketTicketsRegisterTransferPost**](Apis/TicketMethodsApi.md#registertransferticketticketsregistertransferpost) | **POST** /tickets/register/transfer | Register a transfer ticket |
*TicketMethodsApi* | [**registerUsernameTicketsRegisterUsernamePost**](Apis/TicketMethodsApi.md#registerusernameticketsregisterusernamepost) | **POST** /tickets/register/username | Register a Username Change Request ticket |
*TicketMethodsApi* | [**ticketsFindByLabelTicketsFindbylabelTicketTypeLabelGet**](Apis/TicketMethodsApi.md#ticketsfindbylabelticketsfindbylabeltickettypelabelget) | **GET** /tickets/findbylabel/{ticket_type}/{label} | Find tickets by label |
*TicketMethodsApi* | [**ticketsFindTicketsFindGet**](Apis/TicketMethodsApi.md#ticketsfindticketsfindget) | **GET** /tickets/find | Find Pastel tickets |
*TicketMethodsApi* | [**ticketsGetTicketsGetGet**](Apis/TicketMethodsApi.md#ticketsgetticketsgetget) | **GET** /tickets/get | Get a Pastel ticket by transaction ID |
*TicketMethodsApi* | [**ticketsRegisterAcceptTicketsRegisterAcceptPost**](Apis/TicketMethodsApi.md#ticketsregisteracceptticketsregisteracceptpost) | **POST** /tickets/register/accept | Register an accept ticket |
*TicketMethodsApi* | [**ticketsRegisterCollectionTicketsRegistercollectionPost**](Apis/TicketMethodsApi.md#ticketsregistercollectionticketsregistercollectionpost) | **POST** /tickets/registercollection | Register a collection ticket |
*TicketMethodsApi* | [**ticketsRegisterDownTicketsRegisterDownPost**](Apis/TicketMethodsApi.md#ticketsregisterdownticketsregisterdownpost) | **POST** /tickets/register/down | Register a Take Down Request Ticket |
*TicketMethodsApi* | [**ticketsRegisterEthereumAddressTicketsRegisterEthereumaddressPost**](Apis/TicketMethodsApi.md#ticketsregisterethereumaddressticketsregisterethereumaddresspost) | **POST** /tickets/register/ethereumaddress | Register Ethereum Address Change Request |
*TicketMethodsApi* | [**ticketsRegisterIdTicketsRegisterIdPost**](Apis/TicketMethodsApi.md#ticketsregisteridticketsregisteridpost) | **POST** /tickets/register_id | Register Pastel ID identity |
*TicketMethodsApi* | [**ticketsRegisterMnidTicketsRegisterMnidPost**](Apis/TicketMethodsApi.md#ticketsregistermnidticketsregistermnidpost) | **POST** /tickets/register/mnid | Register Masternode PastelID |
*TicketMethodsApi* | [**ticketsRegisterOfferTicketsRegisterOfferPost**](Apis/TicketMethodsApi.md#ticketsregisterofferticketsregisterofferpost) | **POST** /tickets/register/offer | Register an offer ticket |
*TicketMethodsApi* | [**ticketsTicketsCommandGet**](Apis/TicketMethodsApi.md#ticketsticketscommandget) | **GET** /tickets/{command} | Execute Pastel Ticket Commands |
*TicketMethodsApi* | [**ticketsToolsSearchthumbidsTicketsToolsSearchthumbidsPost**](Apis/TicketMethodsApi.md#ticketstoolssearchthumbidsticketstoolssearchthumbidspost) | **POST** /tickets/tools/searchthumbids | Search for NFT registration tickets and thumbnail hash |
*TicketMethodsApi* | [**ticketsToolsTicketsToolsPost**](Apis/TicketMethodsApi.md#ticketstoolsticketstoolspost) | **POST** /tickets/tools | Execute various ticket tools commands |
*TicketMethodsApi* | [**validateOwnershipTicketsToolsValidateownershipPost**](Apis/TicketMethodsApi.md#validateownershipticketstoolsvalidateownershippost) | **POST** /tickets/tools/validateownership | Validate item ownership by Pastel ID |
| *UtilityMethodsApi* | [**addMultisigAddressAddmultisigaddressPost**](Apis/UtilityMethodsApi.md#addmultisigaddressaddmultisigaddresspost) | **POST** /addmultisigaddress | Add a multisignature address |
*UtilityMethodsApi* | [**backupWalletBackupwalletPost**](Apis/UtilityMethodsApi.md#backupwalletbackupwalletpost) | **POST** /backupwallet | Backup the wallet to a destination |
*UtilityMethodsApi* | [**createMultisigCreatemultisigPost**](Apis/UtilityMethodsApi.md#createmultisigcreatemultisigpost) | **POST** /createmultisig | Create a multisig address |
*UtilityMethodsApi* | [**decodeScriptDecodescriptPost**](Apis/UtilityMethodsApi.md#decodescriptdecodescriptpost) | **POST** /decodescript | Decode a hex-encoded script |
*UtilityMethodsApi* | [**estimatePriorityEstimatepriorityGet**](Apis/UtilityMethodsApi.md#estimatepriorityestimatepriorityget) | **GET** /estimatepriority | Estimate the transaction priority for zero-fee confirmation |
*UtilityMethodsApi* | [**generatePastelIdNewkeyPastelidNewkeyPost**](Apis/UtilityMethodsApi.md#generatepastelidnewkeypastelidnewkeypost) | **POST** /pastelid/newkey | Generate new Pastel ID and keys |
*UtilityMethodsApi* | [**generateReportGenerateReportReportNameGet**](Apis/UtilityMethodsApi.md#generatereportgeneratereportreportnameget) | **GET** /generate-report/{report_name} | Generate various reports |
*UtilityMethodsApi* | [**getActionFeesStoragefeeGetactionfeesGet**](Apis/UtilityMethodsApi.md#getactionfeesstoragefeegetactionfeesget) | **GET** /storagefee/getactionfees | Get action fees based on data size |
*UtilityMethodsApi* | [**getAddressMempoolGetaddressmempoolGet**](Apis/UtilityMethodsApi.md#getaddressmempoolgetaddressmempoolget) | **GET** /getaddressmempool | Get all mempool deltas for an address |
*UtilityMethodsApi* | [**getFeeScheduleGetfeescheduleGet**](Apis/UtilityMethodsApi.md#getfeeschedulegetfeescheduleget) | **GET** /getfeeschedule | Get the current fee schedule |
*UtilityMethodsApi* | [**getMemoryInfoGetmemoryinfoGet**](Apis/UtilityMethodsApi.md#getmemoryinfogetmemoryinfoget) | **GET** /getmemoryinfo | Get memory usage information |
*UtilityMethodsApi* | [**getMempoolInfoGetmempoolinfoGet**](Apis/UtilityMethodsApi.md#getmempoolinfogetmempoolinfoget) | **GET** /getmempoolinfo | Get active state of the TX memory pool |
*UtilityMethodsApi* | [**getNewAddressGetnewaddressGet**](Apis/UtilityMethodsApi.md#getnewaddressgetnewaddressget) | **GET** /getnewaddress | Generate a new Pastel address |
*UtilityMethodsApi* | [**getStorageFeeGetFeeStoragefeeGetfeeGet**](Apis/UtilityMethodsApi.md#getstoragefeegetfeestoragefeegetfeeget) | **GET** /storagefee/getfee | Get the storage fee |
*UtilityMethodsApi* | [**getStorageFeesStoragefeeGetfeesGet**](Apis/UtilityMethodsApi.md#getstoragefeesstoragefeegetfeesget) | **GET** /storagefee/getfees | Get the current storage fees |
*UtilityMethodsApi* | [**getWalletInfoGetwalletinfoGet**](Apis/UtilityMethodsApi.md#getwalletinfogetwalletinfoget) | **GET** /getwalletinfo | Get wallet state information |
*UtilityMethodsApi* | [**governanceActionGovernancePost**](Apis/UtilityMethodsApi.md#governanceactiongovernancepost) | **POST** /governance | Cast a vote or list governance tickets |
*UtilityMethodsApi* | [**pastelidNewkeyPastelidNewkeyPost**](Apis/UtilityMethodsApi.md#pastelidnewkeypastelidnewkeypost) | **POST** /pastelid_newkey | Generate new Pastel ID and associated keys |
*UtilityMethodsApi* | [**pastelidPasswdPastelidPasswdPost**](Apis/UtilityMethodsApi.md#pastelidpasswdpastelidpasswdpost) | **POST** /pastelid/passwd | Change passphrase for PastelID secure container |
*UtilityMethodsApi* | [**pastelidSignFilePastelidSignfilePost**](Apis/UtilityMethodsApi.md#pastelidsignfilepastelidsignfilepost) | **POST** /pastelid/signfile | Sign a file with a Pastel ID |
*UtilityMethodsApi* | [**pastelidVerifyFilePastelidVerifyFilePost**](Apis/UtilityMethodsApi.md#pastelidverifyfilepastelidverifyfilepost) | **POST** /pastelid/verify-file | Verify a file's signature with a Pastel ID |
*UtilityMethodsApi* | [**pastelidVerifyPastelidVerifyPost**](Apis/UtilityMethodsApi.md#pastelidverifypastelidverifypost) | **POST** /pastelid/verify | Verify a signature with PastelID |
*UtilityMethodsApi* | [**pingPingGet**](Apis/UtilityMethodsApi.md#pingpingget) | **GET** /ping | Send a ping to all nodes |
*UtilityMethodsApi* | [**resendWalletTransactionsResendwallettransactionsPost**](Apis/UtilityMethodsApi.md#resendwallettransactionsresendwallettransactionspost) | **POST** /resendwallettransactions | Re-broadcast unconfirmed wallet transactions |
*UtilityMethodsApi* | [**retrieveChaindataChaindataRetrievePost**](Apis/UtilityMethodsApi.md#retrievechaindatachaindataretrievepost) | **POST** /chaindata/retrieve | Retrieve data from the blockchain |
*UtilityMethodsApi* | [**scanForMissingTxsScanformissingtxsPost**](Apis/UtilityMethodsApi.md#scanformissingtxsscanformissingtxspost) | **POST** /scanformissingtxs | Scan for missing transactions |
*UtilityMethodsApi* | [**sendToAddressSendtoaddressPost**](Apis/UtilityMethodsApi.md#sendtoaddresssendtoaddresspost) | **POST** /sendtoaddress | Send an amount to a given address |
*UtilityMethodsApi* | [**setTxFeeSettxfeePost**](Apis/UtilityMethodsApi.md#settxfeesettxfeepost) | **POST** /settxfee | Set the transaction fee per kB |
*UtilityMethodsApi* | [**signMessageSignmessagePost**](Apis/UtilityMethodsApi.md#signmessagesignmessagepost) | **POST** /signmessage | Sign a message with the private key of a t-addr |
*UtilityMethodsApi* | [**signWithPastelIdPastelidSignPost**](Apis/UtilityMethodsApi.md#signwithpastelidpastelidsignpost) | **POST** /pastelid/sign | Sign a text with Pastel ID |
*UtilityMethodsApi* | [**storeChaindataChaindataStorePost**](Apis/UtilityMethodsApi.md#storechaindatachaindatastorepost) | **POST** /chaindata/store | Store data in the blockchain |
*UtilityMethodsApi* | [**validateAddressValidateaddressPost**](Apis/UtilityMethodsApi.md#validateaddressvalidateaddresspost) | **POST** /validateaddress | Validate a Pastel address |
*UtilityMethodsApi* | [**verifyMessageVerifymessagePost**](Apis/UtilityMethodsApi.md#verifymessageverifymessagepost) | **POST** /verifymessage | Verify a signed message |
*UtilityMethodsApi* | [**zGetNotesCountZGetnotescountGet**](Apis/UtilityMethodsApi.md#zgetnotescountzgetnotescountget) | **GET** /z_getnotescount | Get the count of sapling notes in the wallet |
*UtilityMethodsApi* | [**zGetOperationStatusZGetoperationstatusGet**](Apis/UtilityMethodsApi.md#zgetoperationstatuszgetoperationstatusget) | **GET** /z_getoperationstatus | Get the status of asynchronous operations |
*UtilityMethodsApi* | [**zListReceivedByAddressZListreceivedbyaddressGet**](Apis/UtilityMethodsApi.md#zlistreceivedbyaddresszlistreceivedbyaddressget) | **GET** /z_listreceivedbyaddress | List amounts received by a z-address |
*UtilityMethodsApi* | [**zValidateAddressZValidateaddressGet**](Apis/UtilityMethodsApi.md#zvalidateaddresszvalidateaddressget) | **GET** /z_validateaddress | Validate a Z address |
*UtilityMethodsApi* | [**zcBenchmarkZcbenchmarkPost**](Apis/UtilityMethodsApi.md#zcbenchmarkzcbenchmarkpost) | **POST** /zcbenchmark | Runs a benchmark of the selected type |
| *WalletMethodsApi* | [**dumpPrivKeyDumpprivkeyGet**](Apis/WalletMethodsApi.md#dumpprivkeydumpprivkeyget) | **GET** /dumpprivkey | Reveal the private key for a given address |
*WalletMethodsApi* | [**dumpWalletDumpwalletPost**](Apis/WalletMethodsApi.md#dumpwalletdumpwalletpost) | **POST** /dumpwallet | Dump wallet keys |
*WalletMethodsApi* | [**getAccountAddressGetaccountaddressGet**](Apis/WalletMethodsApi.md#getaccountaddressgetaccountaddressget) | **GET** /getaccountaddress | Get the current Pastel address for receiving payments |
*WalletMethodsApi* | [**getAddressesByAccountGetaddressesbyaccountGet**](Apis/WalletMethodsApi.md#getaddressesbyaccountgetaddressesbyaccountget) | **GET** /getaddressesbyaccount | Get addresses by account |
*WalletMethodsApi* | [**getReceivedByAccountGetreceivedbyaccountGet**](Apis/WalletMethodsApi.md#getreceivedbyaccountgetreceivedbyaccountget) | **GET** /getreceivedbyaccount | Get the total amount received by an account |
*WalletMethodsApi* | [**importAddressImportaddressPost**](Apis/WalletMethodsApi.md#importaddressimportaddresspost) | **POST** /importaddress | Import an address |
*WalletMethodsApi* | [**importPrivKeyImportprivkeyPost**](Apis/WalletMethodsApi.md#importprivkeyimportprivkeypost) | **POST** /importprivkey | Import a private key |
*WalletMethodsApi* | [**importWalletImportwalletPost**](Apis/WalletMethodsApi.md#importwalletimportwalletpost) | **POST** /importwallet | Import a wallet from a dump file |
*WalletMethodsApi* | [**listAccountsListaccountsGet**](Apis/WalletMethodsApi.md#listaccountslistaccountsget) | **GET** /listaccounts | List account balances |
*WalletMethodsApi* | [**listAddressAmountsListaddressamountsGet**](Apis/WalletMethodsApi.md#listaddressamountslistaddressamountsget) | **GET** /listaddressamounts | List balance on each address |
*WalletMethodsApi* | [**listReceivedByAddressListreceivedbyaddressGet**](Apis/WalletMethodsApi.md#listreceivedbyaddresslistreceivedbyaddressget) | **GET** /listreceivedbyaddress | List balances by receiving address |
*WalletMethodsApi* | [**listTransactionsListtransactionsGet**](Apis/WalletMethodsApi.md#listtransactionslisttransactionsget) | **GET** /listtransactions | List recent transactions |
*WalletMethodsApi* | [**zExportKeyZExportkeyPost**](Apis/WalletMethodsApi.md#zexportkeyzexportkeypost) | **POST** /z_exportkey | Reveal the private key corresponding to a z-address |
*WalletMethodsApi* | [**zExportViewingKeyZExportviewingkeyGet**](Apis/WalletMethodsApi.md#zexportviewingkeyzexportviewingkeyget) | **GET** /z_exportviewingkey | Export the viewing key for a Z-address |
*WalletMethodsApi* | [**zExportWalletZExportwalletPost**](Apis/WalletMethodsApi.md#zexportwalletzexportwalletpost) | **POST** /z_exportwallet | Export wallet keys |
*WalletMethodsApi* | [**zGetNewAddressZGetnewaddressGet**](Apis/WalletMethodsApi.md#zgetnewaddresszgetnewaddressget) | **GET** /z_getnewaddress | Generate a new shielded address |
*WalletMethodsApi* | [**zGetTotalBalanceZGettotalbalanceGet**](Apis/WalletMethodsApi.md#zgettotalbalancezgettotalbalanceget) | **GET** /z_gettotalbalance | Get the total balance of both transparent and private funds |
*WalletMethodsApi* | [**zImportKeyZImportkeyGet**](Apis/WalletMethodsApi.md#zimportkeyzimportkeyget) | **GET** /z_importkey | Import a Z key into the wallet |
*WalletMethodsApi* | [**zImportViewingKeyZImportviewingkeyPost**](Apis/WalletMethodsApi.md#zimportviewingkeyzimportviewingkeypost) | **POST** /z_importviewingkey | Import a viewing key into the wallet |
*WalletMethodsApi* | [**zImportWalletZImportwalletPost**](Apis/WalletMethodsApi.md#zimportwalletzimportwalletpost) | **POST** /z_importwallet | Import keys from a wallet export file |


<a name="documentation-for-models"></a>
## Documentation for Models

 - [Absolute](./Models/Absolute.md)
 - [Account](./Models/Account.md)
 - [Account_1](./Models/Account_1.md)
 - [Account_2](./Models/Account_2.md)
 - [ActionTicketRequest](./Models/ActionTicketRequest.md)
 - [ActionTicketResponse](./Models/ActionTicketResponse.md)
 - [AddMultisigAddressRequest](./Models/AddMultisigAddressRequest.md)
 - [AddMultisigAddressResponse](./Models/AddMultisigAddressResponse.md)
 - [AddNodeRequest](./Models/AddNodeRequest.md)
 - [AddNodeResponse](./Models/AddNodeResponse.md)
 - [AddedNodeInfo](./Models/AddedNodeInfo.md)
 - [Additional_Args](./Models/Additional_Args.md)
 - [Additional_Param](./Models/Additional_Param.md)
 - [Additional_Params](./Models/Additional_Params.md)
 - [Address](./Models/Address.md)
 - [AddressGrouping](./Models/AddressGrouping.md)
 - [AddressGroupingsResponse](./Models/AddressGroupingsResponse.md)
 - [AddressReceivedInfo](./Models/AddressReceivedInfo.md)
 - [Address_Type](./Models/Address_Type.md)
 - [Addresses](./Models/Addresses.md)
 - [Addresses_1](./Models/Addresses_1.md)
 - [Addrlocal](./Models/Addrlocal.md)
 - [Algorithm](./Models/Algorithm.md)
 - [Algorithm_1](./Models/Algorithm_1.md)
 - [Allowhighfees](./Models/Allowhighfees.md)
 - [BackupWalletRequest](./Models/BackupWalletRequest.md)
 - [BackupWalletResponse](./Models/BackupWalletResponse.md)
 - [Balance](./Models/Balance.md)
 - [BannedAddress](./Models/BannedAddress.md)
 - [Banscore](./Models/Banscore.md)
 - [Bantime](./Models/Bantime.md)
 - [BlockResponseVerbosity0](./Models/BlockResponseVerbosity0.md)
 - [BlockResponseVerbosity1](./Models/BlockResponseVerbosity1.md)
 - [BlockResponseVerbosity2](./Models/BlockResponseVerbosity2.md)
 - [Block_Hash](./Models/Block_Hash.md)
 - [BlockchainInfoResponse](./Models/BlockchainInfoResponse.md)
 - [Blockhash](./Models/Blockhash.md)
 - [Blockhash_1](./Models/Blockhash_1.md)
 - [Blockhash_2](./Models/Blockhash_2.md)
 - [Blockindex](./Models/Blockindex.md)
 - [Blockindex_1](./Models/Blockindex_1.md)
 - [Blocks](./Models/Blocks.md)
 - [Blocktime](./Models/Blocktime.md)
 - [Blocktime_1](./Models/Blocktime_1.md)
 - [Blocktime_2](./Models/Blocktime_2.md)
 - [ChainTip](./Models/ChainTip.md)
 - [ChaindataRetrieveRequest](./Models/ChaindataRetrieveRequest.md)
 - [ChaindataRetrieveResponse](./Models/ChaindataRetrieveResponse.md)
 - [ChaindataStoreRequest](./Models/ChaindataStoreRequest.md)
 - [ChaindataStoreResponse](./Models/ChaindataStoreResponse.md)
 - [Change](./Models/Change.md)
 - [Change_Address](./Models/Change_Address.md)
 - [Checklevel](./Models/Checklevel.md)
 - [CoinbaseTxn](./Models/CoinbaseTxn.md)
 - [CollectionTicket](./Models/CollectionTicket.md)
 - [Comment](./Models/Comment.md)
 - [Comment_To](./Models/Comment_To.md)
 - [Confirmations](./Models/Confirmations.md)
 - [Confirmations_1](./Models/Confirmations_1.md)
 - [Consensus](./Models/Consensus.md)
 - [Consensus_Branch_ID](./Models/Consensus_Branch_ID.md)
 - [Copy_Number](./Models/Copy_Number.md)
 - [Count](./Models/Count.md)
 - [CreateMultisigRequest](./Models/CreateMultisigRequest.md)
 - [CreateMultisigResponse](./Models/CreateMultisigResponse.md)
 - [CreateRawTransactionRequest](./Models/CreateRawTransactionRequest.md)
 - [CreateRawTransactionResponse](./Models/CreateRawTransactionResponse.md)
 - [DecodeRawTransactionRequest](./Models/DecodeRawTransactionRequest.md)
 - [DecodeRawTransactionResponse](./Models/DecodeRawTransactionResponse.md)
 - [DecodeScriptRequest](./Models/DecodeScriptRequest.md)
 - [DecodeScriptResponse](./Models/DecodeScriptResponse.md)
 - [Decode_Properties](./Models/Decode_Properties.md)
 - [DeltaDetail](./Models/DeltaDetail.md)
 - [Detail](./Models/Detail.md)
 - [DisconnectNodeRequest](./Models/DisconnectNodeRequest.md)
 - [DisconnectNodeResponse](./Models/DisconnectNodeResponse.md)
 - [Diversifiedtransmissionkey](./Models/Diversifiedtransmissionkey.md)
 - [Diversifier](./Models/Diversifier.md)
 - [DumpPrivKeyRequest](./Models/DumpPrivKeyRequest.md)
 - [DumpPrivKeyResponse](./Models/DumpPrivKeyResponse.md)
 - [DumpWalletResponse](./Models/DumpWalletResponse.md)
 - [EncryptWalletResponse](./Models/EncryptWalletResponse.md)
 - [Error](./Models/Error.md)
 - [ErrorObject](./Models/ErrorObject.md)
 - [Error_Message](./Models/Error_Message.md)
 - [Errormessage](./Models/Errormessage.md)
 - [Errors](./Models/Errors.md)
 - [EstimateFeeResponse](./Models/EstimateFeeResponse.md)
 - [EstimateNftStorageFeeResponse](./Models/EstimateNftStorageFeeResponse.md)
 - [Execution_Secs](./Models/Execution_Secs.md)
 - [Expiryheight](./Models/Expiryheight.md)
 - [Expiryheight_1](./Models/Expiryheight_1.md)
 - [ExportWalletResponse](./Models/ExportWalletResponse.md)
 - [Extra_Param](./Models/Extra_Param.md)
 - [Fast](./Models/Fast.md)
 - [Fee](./Models/Fee.md)
 - [Fee_1](./Models/Fee_1.md)
 - [Filter](./Models/Filter.md)
 - [Finalsaplingroot](./Models/Finalsaplingroot.md)
 - [FixMissingTransactionsResponse](./Models/FixMissingTransactionsResponse.md)
 - [From_Index](./Models/From_Index.md)
 - [FundRawTransactionRequest](./Models/FundRawTransactionRequest.md)
 - [FundRawTransactionResponse](./Models/FundRawTransactionResponse.md)
 - [GenerateBlocksRequest](./Models/GenerateBlocksRequest.md)
 - [GenerateBlocksResponse](./Models/GenerateBlocksResponse.md)
 - [GenerateReportResponse](./Models/GenerateReportResponse.md)
 - [Genproclimit](./Models/Genproclimit.md)
 - [GetAccountAddressResponse](./Models/GetAccountAddressResponse.md)
 - [GetAccountResponse](./Models/GetAccountResponse.md)
 - [GetActionFeesResponse](./Models/GetActionFeesResponse.md)
 - [GetAddedNodeInfoResponse](./Models/GetAddedNodeInfoResponse.md)
 - [GetAddressMempoolResponse](./Models/GetAddressMempoolResponse.md)
 - [GetBalanceResponse](./Models/GetBalanceResponse.md)
 - [GetBestBlockHashResponse](./Models/GetBestBlockHashResponse.md)
 - [GetBlockCountResponse](./Models/GetBlockCountResponse.md)
 - [GetBlockDeltasResponse](./Models/GetBlockDeltasResponse.md)
 - [GetBlockHashRequest](./Models/GetBlockHashRequest.md)
 - [GetBlockHashResponse](./Models/GetBlockHashResponse.md)
 - [GetBlockResponse](./Models/GetBlockResponse.md)
 - [GetBlockSubsidyResponse](./Models/GetBlockSubsidyResponse.md)
 - [GetBlockTemplateRequest](./Models/GetBlockTemplateRequest.md)
 - [GetBlockTemplateResponse](./Models/GetBlockTemplateResponse.md)
 - [GetBlockTemplateResponse_coinbasetxn](./Models/GetBlockTemplateResponse_coinbasetxn.md)
 - [GetChainTipsResponse](./Models/GetChainTipsResponse.md)
 - [GetConnectionCountResponse](./Models/GetConnectionCountResponse.md)
 - [GetDeprecationInfoResponse](./Models/GetDeprecationInfoResponse.md)
 - [GetDifficultyResponse](./Models/GetDifficultyResponse.md)
 - [GetFeeScheduleResponse](./Models/GetFeeScheduleResponse.md)
 - [GetFeesResponse](./Models/GetFeesResponse.md)
 - [GetGenerateResponse](./Models/GetGenerateResponse.md)
 - [GetInfoResponse](./Models/GetInfoResponse.md)
 - [GetLocalSolpsResponse](./Models/GetLocalSolpsResponse.md)
 - [GetMemoryInfoResponse](./Models/GetMemoryInfoResponse.md)
 - [GetMempoolInfoResponse](./Models/GetMempoolInfoResponse.md)
 - [GetMiningInfoResponse](./Models/GetMiningInfoResponse.md)
 - [GetNetTotalsResponse](./Models/GetNetTotalsResponse.md)
 - [GetNetworkInfoResponse](./Models/GetNetworkInfoResponse.md)
 - [GetNetworkSolpsRequest](./Models/GetNetworkSolpsRequest.md)
 - [GetNetworkSolpsResponse](./Models/GetNetworkSolpsResponse.md)
 - [GetNetworksInfoResponse](./Models/GetNetworksInfoResponse.md)
 - [GetNewAddressResponse](./Models/GetNewAddressResponse.md)
 - [GetNextBlockSubsidyResponse](./Models/GetNextBlockSubsidyResponse.md)
 - [GetOperationStatusResponse](./Models/GetOperationStatusResponse.md)
 - [GetPeerInfoResponse](./Models/GetPeerInfoResponse.md)
 - [GetRawTransactionRequest](./Models/GetRawTransactionRequest.md)
 - [GetReceivedByAccountRequest](./Models/GetReceivedByAccountRequest.md)
 - [GetReceivedByAccountResponse](./Models/GetReceivedByAccountResponse.md)
 - [GetReceivedByAddressResponse](./Models/GetReceivedByAddressResponse.md)
 - [GetTotalStorageFeeRequest](./Models/GetTotalStorageFeeRequest.md)
 - [GetTotalStorageFeeResponse](./Models/GetTotalStorageFeeResponse.md)
 - [GetTransactionResponse](./Models/GetTransactionResponse.md)
 - [GetTxOutProofResponse](./Models/GetTxOutProofResponse.md)
 - [GetTxOutResponse](./Models/GetTxOutResponse.md)
 - [GetTxOutSetInfoResponse](./Models/GetTxOutSetInfoResponse.md)
 - [GetTxfeeResponse](./Models/GetTxfeeResponse.md)
 - [Governance](./Models/Governance.md)
 - [GovernanceTicketResponse](./Models/GovernanceTicketResponse.md)
 - [HTTPValidationError](./Models/HTTPValidationError.md)
 - [Height](./Models/Height.md)
 - [Height_1](./Models/Height_1.md)
 - [Hex](./Models/Hex.md)
 - [ImportAddressRequest](./Models/ImportAddressRequest.md)
 - [ImportAddressResponse](./Models/ImportAddressResponse.md)
 - [ImportPrivKeyResponse](./Models/ImportPrivKeyResponse.md)
 - [ImportWalletResponse](./Models/ImportWalletResponse.md)
 - [In_Active_Chain](./Models/In_Active_Chain.md)
 - [Include_Empty](./Models/Include_Empty.md)
 - [Include_Watch_Only](./Models/Include_Watch_Only.md)
 - [Include_Watchonly](./Models/Include_Watchonly.md)
 - [Includemempool](./Models/Includemempool.md)
 - [Includewatchonly](./Models/Includewatchonly.md)
 - [Includewatchonly_1](./Models/Includewatchonly_1.md)
 - [Index](./Models/Index.md)
 - [Inflight](./Models/Inflight.md)
 - [InputDetail](./Models/InputDetail.md)
 - [Intended_For](./Models/Intended_For.md)
 - [InvalidateBlockResponse](./Models/InvalidateBlockResponse.md)
 - [Involveswatchonly](./Models/Involveswatchonly.md)
 - [Is_Local](./Models/Is_Local.md)
 - [Iscompressed](./Models/Iscompressed.md)
 - [Ismine](./Models/Ismine.md)
 - [Ismine_Filter](./Models/Ismine_Filter.md)
 - [Isscript](./Models/Isscript.md)
 - [Iswatchonly](./Models/Iswatchonly.md)
 - [Jsindex](./Models/Jsindex.md)
 - [Jsonparametersobject](./Models/Jsonparametersobject.md)
 - [Jsonrequestobject](./Models/Jsonrequestobject.md)
 - [Jsoutindex](./Models/Jsoutindex.md)
 - [Jsoutputprev](./Models/Jsoutputprev.md)
 - [Jsprev](./Models/Jsprev.md)
 - [KeypoolRefillRequest](./Models/KeypoolRefillRequest.md)
 - [Keypoololdest](./Models/Keypoololdest.md)
 - [Keypoolsize](./Models/Keypoolsize.md)
 - [Label](./Models/Label.md)
 - [Limit](./Models/Limit.md)
 - [ListAccountsResponse](./Models/ListAccountsResponse.md)
 - [ListAccountsResponseItem](./Models/ListAccountsResponseItem.md)
 - [ListAddressAmountsResponse](./Models/ListAddressAmountsResponse.md)
 - [ListBannedResponse](./Models/ListBannedResponse.md)
 - [ListLockUnspentResponse](./Models/ListLockUnspentResponse.md)
 - [ListLockUnspentResponseItem](./Models/ListLockUnspentResponseItem.md)
 - [ListShieldedAddressesResponse](./Models/ListShieldedAddressesResponse.md)
 - [ListSinceBlockRequest](./Models/ListSinceBlockRequest.md)
 - [ListSinceBlockResponse](./Models/ListSinceBlockResponse.md)
 - [ListTransactionsRequest](./Models/ListTransactionsRequest.md)
 - [ListTransactionsResponse](./Models/ListTransactionsResponse.md)
 - [ListUnspentResponse](./Models/ListUnspentResponse.md)
 - [LocalAddressInfo](./Models/LocalAddressInfo.md)
 - [LockUnspentRequest](./Models/LockUnspentRequest.md)
 - [LockUnspentResponse](./Models/LockUnspentResponse.md)
 - [Locktime](./Models/Locktime.md)
 - [MasterNodePoseBanScoreRequest](./Models/MasterNodePoseBanScoreRequest.md)
 - [MasterNodePoseBanScoreResponse](./Models/MasterNodePoseBanScoreResponse.md)
 - [MasternodeBroadcastRequest](./Models/MasternodeBroadcastRequest.md)
 - [MasternodeBroadcastResponse](./Models/MasternodeBroadcastResponse.md)
 - [MasternodeClearCacheResponse](./Models/MasternodeClearCacheResponse.md)
 - [MasternodeCommandRequest](./Models/MasternodeCommandRequest.md)
 - [MasternodeConfig](./Models/MasternodeConfig.md)
 - [MasternodeCountResponse](./Models/MasternodeCountResponse.md)
 - [MasternodeCurrentInfo](./Models/MasternodeCurrentInfo.md)
 - [MasternodeGenKeyResponse](./Models/MasternodeGenKeyResponse.md)
 - [MasternodeInfo](./Models/MasternodeInfo.md)
 - [MasternodeInitRequest](./Models/MasternodeInitRequest.md)
 - [MasternodeInitResponse](./Models/MasternodeInitResponse.md)
 - [MasternodeListResponse](./Models/MasternodeListResponse.md)
 - [MasternodeMakeConfRequest](./Models/MasternodeMakeConfRequest.md)
 - [MasternodeMakeConfResponse](./Models/MasternodeMakeConfResponse.md)
 - [MasternodeMessageRequest](./Models/MasternodeMessageRequest.md)
 - [MasternodeMessageResponse](./Models/MasternodeMessageResponse.md)
 - [MasternodeOutputsResponse](./Models/MasternodeOutputsResponse.md)
 - [MasternodePoSeBanScoreResponse](./Models/MasternodePoSeBanScoreResponse.md)
 - [MasternodeStatus](./Models/MasternodeStatus.md)
 - [MasternodeStatusResponse](./Models/MasternodeStatusResponse.md)
 - [MasternodeTopInfo](./Models/MasternodeTopInfo.md)
 - [MasternodeTopResponse](./Models/MasternodeTopResponse.md)
 - [MasternodeWinnerInfo](./Models/MasternodeWinnerInfo.md)
 - [MasternodeWinnersResponse](./Models/MasternodeWinnersResponse.md)
 - [Maxconf](./Models/Maxconf.md)
 - [Memo](./Models/Memo.md)
 - [MemoryInfo](./Models/MemoryInfo.md)
 - [Memostr](./Models/Memostr.md)
 - [MempoolDelta](./Models/MempoolDelta.md)
 - [MergeToAddressRequest](./Models/MergeToAddressRequest.md)
 - [MergeToAddressResponse](./Models/MergeToAddressResponse.md)
 - [Message](./Models/Message.md)
 - [Message_Id](./Models/Message_Id.md)
 - [Messages](./Models/Messages.md)
 - [Min_Conf](./Models/Min_Conf.md)
 - [Min_Height](./Models/Min_Height.md)
 - [Minconf](./Models/Minconf.md)
 - [Minconf_1](./Models/Minconf_1.md)
 - [MoveRequest](./Models/MoveRequest.md)
 - [MoveResponse](./Models/MoveResponse.md)
 - [New_Fee](./Models/New_Fee.md)
 - [Newsize](./Models/Newsize.md)
 - [Nextblockhash](./Models/Nextblockhash.md)
 - [NodeAddressInfo](./Models/NodeAddressInfo.md)
 - [Numblocks](./Models/Numblocks.md)
 - [OperationStatusInfo](./Models/OperationStatusInfo.md)
 - [Operation_Ids](./Models/Operation_Ids.md)
 - [Operation_Ids_1](./Models/Operation_Ids_1.md)
 - [Otheraccount](./Models/Otheraccount.md)
 - [Outindex](./Models/Outindex.md)
 - [Outputprev](./Models/Outputprev.md)
 - [Parameters](./Models/Parameters.md)
 - [PastelIDNewKeyRequest](./Models/PastelIDNewKeyRequest.md)
 - [PastelIDNewKeyResponse](./Models/PastelIDNewKeyResponse.md)
 - [PastelIDPasswdRequest](./Models/PastelIDPasswdRequest.md)
 - [PastelIDPasswdResponse](./Models/PastelIDPasswdResponse.md)
 - [PastelIDSignFileRequest](./Models/PastelIDSignFileRequest.md)
 - [PastelIDSignFileResponse](./Models/PastelIDSignFileResponse.md)
 - [PastelIDSignRequest](./Models/PastelIDSignRequest.md)
 - [PastelIDSignResponse](./Models/PastelIDSignResponse.md)
 - [PastelIDVerifyFileResponse](./Models/PastelIDVerifyFileResponse.md)
 - [PastelIDVerifyRequest](./Models/PastelIDVerifyRequest.md)
 - [PastelIDVerifyResponse](./Models/PastelIDVerifyResponse.md)
 - [Pastel_Id](./Models/Pastel_Id.md)
 - [Pastelid](./Models/Pastelid.md)
 - [Payingkey](./Models/Payingkey.md)
 - [Paytxfee](./Models/Paytxfee.md)
 - [PeerInfo](./Models/PeerInfo.md)
 - [PingResponse](./Models/PingResponse.md)
 - [Pingwait](./Models/Pingwait.md)
 - [Pose_Ban_Height](./Models/Pose_Ban_Height.md)
 - [PrevTx](./Models/PrevTx.md)
 - [Previous_Transactions](./Models/Previous_Transactions.md)
 - [Previousblockhash](./Models/Previousblockhash.md)
 - [Prevmerklerootsignature](./Models/Prevmerklerootsignature.md)
 - [Prevout](./Models/Prevout.md)
 - [Prevtxid](./Models/Prevtxid.md)
 - [PrioritiseTransactionRequest](./Models/PrioritiseTransactionRequest.md)
 - [PrioritiseTransactionResponse](./Models/PrioritiseTransactionResponse.md)
 - [Private_Keys](./Models/Private_Keys.md)
 - [Proxy](./Models/Proxy.md)
 - [Pruned](./Models/Pruned.md)
 - [Pruneheight](./Models/Pruneheight.md)
 - [Pub_Key](./Models/Pub_Key.md)
 - [Pubkey](./Models/Pubkey.md)
 - [ReceivedNoteInfo](./Models/ReceivedNoteInfo.md)
 - [ReconsiderBlockRequest](./Models/ReconsiderBlockRequest.md)
 - [ReconsiderBlockResponse](./Models/ReconsiderBlockResponse.md)
 - [Redeemscript](./Models/Redeemscript.md)
 - [RefreshMiningMnidInfoResponse](./Models/RefreshMiningMnidInfoResponse.md)
 - [RegisterCollectionTicketRequest](./Models/RegisterCollectionTicketRequest.md)
 - [RegisterCollectionTicketResponse](./Models/RegisterCollectionTicketResponse.md)
 - [RegisterNFTTicketRequest](./Models/RegisterNFTTicketRequest.md)
 - [RegisterNFTTicketResponse](./Models/RegisterNFTTicketResponse.md)
 - [RegisterRoyaltyTicketRequest](./Models/RegisterRoyaltyTicketRequest.md)
 - [RegisterRoyaltyTicketResponse](./Models/RegisterRoyaltyTicketResponse.md)
 - [RegisterTransferTicketRequest](./Models/RegisterTransferTicketRequest.md)
 - [RegisterTransferTicketResponse](./Models/RegisterTransferTicketResponse.md)
 - [RegisterUsernameRequest](./Models/RegisterUsernameRequest.md)
 - [RegisterUsernameResponse](./Models/RegisterUsernameResponse.md)
 - [Reqsigs](./Models/Reqsigs.md)
 - [Required](./Models/Required.md)
 - [Rescan](./Models/Rescan.md)
 - [Rescan_1](./Models/Rescan_1.md)
 - [ResendWalletTransactionsResponse](./Models/ResendWalletTransactionsResponse.md)
 - [Response](./Models/Response.md)
 - [Response_Execute_Masternode_Command_Masternode_Command_Post](./Models/Response_Execute_Masternode_Command_Masternode_Command_Post.md)
 - [Response_Governance_Action_Governance_Post](./Models/Response_Governance_Action_Governance_Post.md)
 - [Response_Tickets_Find_Tickets_Find_Get](./Models/Response_Tickets_Find_Tickets_Find_Get.md)
 - [Result](./Models/Result.md)
 - [Result_1](./Models/Result_1.md)
 - [ScanForMissingTxsRequest](./Models/ScanForMissingTxsRequest.md)
 - [ScanForMissingTxsResponse](./Models/ScanForMissingTxsResponse.md)
 - [ScriptPubKey](./Models/ScriptPubKey.md)
 - [ScriptSig](./Models/ScriptSig.md)
 - [Scriptpubkey](./Models/Scriptpubkey.md)
 - [Seedfp](./Models/Seedfp.md)
 - [SendFromResponse](./Models/SendFromResponse.md)
 - [SendManyRequest](./Models/SendManyRequest.md)
 - [SendManyResponse](./Models/SendManyResponse.md)
 - [SendRawTransactionRequest](./Models/SendRawTransactionRequest.md)
 - [SendRawTransactionResponse](./Models/SendRawTransactionResponse.md)
 - [SendToAddressRequest](./Models/SendToAddressRequest.md)
 - [SendToAddressResponse](./Models/SendToAddressResponse.md)
 - [Sequence](./Models/Sequence.md)
 - [SetAccountRequest](./Models/SetAccountRequest.md)
 - [SetAccountResponse](./Models/SetAccountResponse.md)
 - [SetBanRequest](./Models/SetBanRequest.md)
 - [SetBanResponse](./Models/SetBanResponse.md)
 - [SetGenerateRequest](./Models/SetGenerateRequest.md)
 - [SetGenerateResponse](./Models/SetGenerateResponse.md)
 - [SetTxFeeRequest](./Models/SetTxFeeRequest.md)
 - [SetTxFeeResponse](./Models/SetTxFeeResponse.md)
 - [Shielded_Limit](./Models/Shielded_Limit.md)
 - [SignMessageRequest](./Models/SignMessageRequest.md)
 - [SignMessageResponse](./Models/SignMessageResponse.md)
 - [SignRawTransactionRequest](./Models/SignRawTransactionRequest.md)
 - [SignRawTransactionResponse](./Models/SignRawTransactionResponse.md)
 - [Signature](./Models/Signature.md)
 - [SignatureInfo](./Models/SignatureInfo.md)
 - [Signature_Hash_Type](./Models/Signature_Hash_Type.md)
 - [Size](./Models/Size.md)
 - [SoftFork](./Models/SoftFork.md)
 - [Spend](./Models/Spend.md)
 - [SpendDetail](./Models/SpendDetail.md)
 - [Start_Height](./Models/Start_Height.md)
 - [Status](./Models/Status.md)
 - [StorageFeeGetFeeResponse](./Models/StorageFeeGetFeeResponse.md)
 - [StorageFeeInfo](./Models/StorageFeeInfo.md)
 - [StorageFeeResponse](./Models/StorageFeeResponse.md)
 - [StorageFeeSetFeeRequest](./Models/StorageFeeSetFeeRequest.md)
 - [StorageFeeSetFeeResponse](./Models/StorageFeeSetFeeResponse.md)
 - [SubmitBlockRequest](./Models/SubmitBlockRequest.md)
 - [SubmitBlockResponse](./Models/SubmitBlockResponse.md)
 - [Subtract_Fee_From_Amount](./Models/Subtract_Fee_From_Amount.md)
 - [Subtract_Fee_From_Amount_1](./Models/Subtract_Fee_From_Amount_1.md)
 - [Synced_Blocks](./Models/Synced_Blocks.md)
 - [Synced_Headers](./Models/Synced_Headers.md)
 - [Target_Confirmations](./Models/Target_Confirmations.md)
 - [TicketFindResponse](./Models/TicketFindResponse.md)
 - [TicketSearchThumbIdsRequest](./Models/TicketSearchThumbIdsRequest.md)
 - [TicketSearchThumbIdsResponse](./Models/TicketSearchThumbIdsResponse.md)
 - [Ticket_Data](./Models/Ticket_Data.md)
 - [Ticketid](./Models/Ticketid.md)
 - [TicketsFindByLabelResponse](./Models/TicketsFindByLabelResponse.md)
 - [TicketsGetRequest](./Models/TicketsGetRequest.md)
 - [TicketsGetResponse](./Models/TicketsGetResponse.md)
 - [TicketsListResponse](./Models/TicketsListResponse.md)
 - [TicketsRegisterAcceptRequest](./Models/TicketsRegisterAcceptRequest.md)
 - [TicketsRegisterAcceptResponse](./Models/TicketsRegisterAcceptResponse.md)
 - [TicketsRegisterDownResponse](./Models/TicketsRegisterDownResponse.md)
 - [TicketsRegisterEthereumAddressRequest](./Models/TicketsRegisterEthereumAddressRequest.md)
 - [TicketsRegisterEthereumAddressResponse](./Models/TicketsRegisterEthereumAddressResponse.md)
 - [TicketsRegisterIdRequest](./Models/TicketsRegisterIdRequest.md)
 - [TicketsRegisterIdResponse](./Models/TicketsRegisterIdResponse.md)
 - [TicketsRegisterMnidResponse](./Models/TicketsRegisterMnidResponse.md)
 - [TicketsRegisterOfferRequest](./Models/TicketsRegisterOfferRequest.md)
 - [TicketsRegisterOfferResponse](./Models/TicketsRegisterOfferResponse.md)
 - [TicketsResponse](./Models/TicketsResponse.md)
 - [TicketsToolsRequest](./Models/TicketsToolsRequest.md)
 - [TicketsToolsResponse](./Models/TicketsToolsResponse.md)
 - [Time](./Models/Time.md)
 - [Timereceived](./Models/Timereceived.md)
 - [To](./Models/To.md)
 - [Transaction](./Models/Transaction.md)
 - [TransactionID](./Models/TransactionID.md)
 - [TransactionInfo](./Models/TransactionInfo.md)
 - [TransactionInput](./Models/TransactionInput.md)
 - [TransactionOutput](./Models/TransactionOutput.md)
 - [Transmissionkey](./Models/Transmissionkey.md)
 - [Transparent_Limit](./Models/Transparent_Limit.md)
 - [Txid](./Models/Txid.md)
 - [Type](./Models/Type.md)
 - [Unlocked_Until](./Models/Unlocked_Until.md)
 - [UnspentTransaction](./Models/UnspentTransaction.md)
 - [Upgrade](./Models/Upgrade.md)
 - [Valid_After](./Models/Valid_After.md)
 - [Valid_Before](./Models/Valid_Before.md)
 - [ValidateAddressRequest](./Models/ValidateAddressRequest.md)
 - [ValidateAddressResponse](./Models/ValidateAddressResponse.md)
 - [ValidateOwnershipRequest](./Models/ValidateOwnershipRequest.md)
 - [ValidateOwnershipResponse](./Models/ValidateOwnershipResponse.md)
 - [ValidationError](./Models/ValidationError.md)
 - [Verbose](./Models/Verbose.md)
 - [VerifyChainRequest](./Models/VerifyChainRequest.md)
 - [VerifyChainResponse](./Models/VerifyChainResponse.md)
 - [VerifyMessageRequest](./Models/VerifyMessageRequest.md)
 - [VerifyMessageResponse](./Models/VerifyMessageResponse.md)
 - [Versiongroupid](./Models/Versiongroupid.md)
 - [Vin](./Models/Vin.md)
 - [Vout](./Models/Vout.md)
 - [Vout_1](./Models/Vout_1.md)
 - [WalletInfoResponse](./Models/WalletInfoResponse.md)
 - [WalletPassphraseChangeRequest](./Models/WalletPassphraseChangeRequest.md)
 - [WalletPassphraseChangeResponse](./Models/WalletPassphraseChangeResponse.md)
 - [WalletPassphraseRequest](./Models/WalletPassphraseRequest.md)
 - [WalletPassphraseResponse](./Models/WalletPassphraseResponse.md)
 - [Walletversion](./Models/Walletversion.md)
 - [ZAddressQuery](./Models/ZAddressQuery.md)
 - [ZCBenchmarkRequest](./Models/ZCBenchmarkRequest.md)
 - [ZCBenchmarkResponse](./Models/ZCBenchmarkResponse.md)
 - [ZCBenchmarkSampleResult](./Models/ZCBenchmarkSampleResult.md)
 - [ZExportKeyRequest](./Models/ZExportKeyRequest.md)
 - [ZExportKeyResponse](./Models/ZExportKeyResponse.md)
 - [ZExportViewingKeyResponse](./Models/ZExportViewingKeyResponse.md)
 - [ZGetBalanceResponse](./Models/ZGetBalanceResponse.md)
 - [ZGetNewAddressResponse](./Models/ZGetNewAddressResponse.md)
 - [ZGetNotesCountResponse](./Models/ZGetNotesCountResponse.md)
 - [ZGetOperationResultResponse](./Models/ZGetOperationResultResponse.md)
 - [ZGetTotalBalanceRequest](./Models/ZGetTotalBalanceRequest.md)
 - [ZGetTotalBalanceResponse](./Models/ZGetTotalBalanceResponse.md)
 - [ZImportKeyResponse](./Models/ZImportKeyResponse.md)
 - [ZImportViewingKeyRequest](./Models/ZImportViewingKeyRequest.md)
 - [ZImportViewingKeyResponse](./Models/ZImportViewingKeyResponse.md)
 - [ZImportWalletResponse](./Models/ZImportWalletResponse.md)
 - [ZListOperationIdsResponse](./Models/ZListOperationIdsResponse.md)
 - [ZListReceivedByAddressRequest](./Models/ZListReceivedByAddressRequest.md)
 - [ZListReceivedByAddressResponse](./Models/ZListReceivedByAddressResponse.md)
 - [ZListUnspentResponse](./Models/ZListUnspentResponse.md)
 - [ZListUnspentResponseItem](./Models/ZListUnspentResponseItem.md)
 - [ZOperationResultInfo](./Models/ZOperationResultInfo.md)
 - [ZShieldCoinbaseRequest](./Models/ZShieldCoinbaseRequest.md)
 - [ZShieldCoinbaseResponse](./Models/ZShieldCoinbaseResponse.md)
 - [ZValidateAddressResponse](./Models/ZValidateAddressResponse.md)
 - [ZViewTransactionResponse](./Models/ZViewTransactionResponse.md)
 - [endpoint_functions__NetworkInfo__1](./Models/endpoint_functions__NetworkInfo__1.md)
 - [endpoint_functions__NetworkInfo__2](./Models/endpoint_functions__NetworkInfo__2.md)
 - [endpoint_functions__OutputDetail__1](./Models/endpoint_functions__OutputDetail__1.md)
 - [endpoint_functions__OutputDetail__2](./Models/endpoint_functions__OutputDetail__2.md)
 - [endpoint_functions__TicketInfo__1](./Models/endpoint_functions__TicketInfo__1.md)
 - [endpoint_functions__TicketInfo__2](./Models/endpoint_functions__TicketInfo__2.md)
 - [endpoint_functions__TransactionDetail__1](./Models/endpoint_functions__TransactionDetail__1.md)
 - [endpoint_functions__TransactionDetail__2](./Models/endpoint_functions__TransactionDetail__2.md)


<a name="documentation-for-authorization"></a>
## Documentation for Authorization

All endpoints do not require authorization.
