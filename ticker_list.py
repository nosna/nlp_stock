tickers = ["A", "AA", "AACG", "AACQ", "AACQU", "AACQW", "AAIC", "AAIC^B", "AAIC^C", "AAL", "AAMC", "AAME", "AAN",
           "AAOI", "AAON", "AAP", "AAPL", "AAT", "AAU", "AAWW", "AB", "ABB", "ABBV", "ABC", "ABCB", "ABCL", "ABCM",
           "ABEO", "ABEV", "ABG", "ABGI", "ABIO", "ABM", "ABMD", "ABNB", "ABR", "ABR^A", "ABR^B", "ABR^C", "ABST",
           "ABT", "ABTX", "ABUS", "AC", "ACA", "ACAC", "ACACU", "ACACW", "ACAD", "ACB", "ACBI", "ACC", "ACCD", "ACCO",
           "ACEL", "ACER", "ACET", "ACEV", "ACEVU", "ACEVW", "ACGL", "ACGLO", "ACGLP", "ACH", "ACHC", "ACHV", "ACI",
           "ACIA", "ACIC", "ACIU", "ACIW", "ACKIT", "ACKIU", "ACKIW", "ACLS", "ACM", "ACMR", "ACN", "ACNB", "ACND",
           "ACOR", "ACP", "ACR", "ACR^C", "ACRE", "ACRS", "ACRX", "ACST", "ACTC", "ACTCU", "ACTCW", "ACTG", "ACU",
           "ACV", "ACY", "ADAG", "ADAP", "ADBE", "ADC", "ADCT", "ADERU", "ADES", "ADFI", "ADI", "ADIL", "ADILW", "ADM",
           "ADMA", "ADME", "ADMP", "ADMS", "ADN", "ADNT", "ADNWW", "ADOC", "ADOCR", "ADOCW", "ADP", "ADPT", "ADS",
           "ADSK", "ADT", "ADTN", "ADTX", "ADUS", "ADV", "ADVM", "ADVWW", "ADX", "ADXN", "ADXS", "AE", "AEACU", "AEB",
           "AEE", "AEF", "AEFC", "AEG", "AEGN", "AEHL", "AEHR", "AEI", "AEIS", "AEL", "AEL^A", "AEL^B", "AEM", "AEMD",
           "AENZ", "AEO", "AEP", "AEPPL", "AEPPZ", "AER", "AERI", "AES", "AESE", "AESR", "AEY", "AEYE", "AEZS", "AFB",
           "AFBI", "AFC", "AFG", "AFGB", "AFGC", "AFGD", "AFGE", "AFI", "AFIB", "AFIN", "AFINO", "AFINP", "AFL", "AFMD",
           "AFRM", "AFT", "AFYA", "AG", "AGBA", "AGBAR", "AGBAW", "AGC", "AGCB", "AGCO", "AGCUU", "AGCWW", "AGD", "AGE",
           "AGEN", "AGFS", "AGFY", "AGI", "AGIO", "AGLE", "AGM", "AGM^C", "AGM^D", "AGM^E", "AGM^F", "AGMH", "AGNC",
           "AGNCM", "AGNCN", "AGNCO", "AGNCP", "AGO", "AGO^B", "AGO^E", "AGO^F", "AGR", "AGRO", "AGRX", "AGS", "AGTC",
           "AGX", "AGYS", "AHAC", "AHACU", "AHACW", "AHC", "AHCO", "AHH", "AHH^A", "AHL^C", "AHL^D", "AHL^E", "AHPI",
           "AHT", "AHT^D", "AHT^F", "AHT^G", "AHT^H", "AHT^I", "AI", "AIC", "AIF", "AIG", "AIG^A", "AIH", "AIHS",
           "AIKI", "AIM", "AIMC", "AIN", "AINC", "AINV", "AIO", "AIR", "AIRC", "AIRG", "AIRI", "AIRT", "AIRTP", "AIRTW",
           "AIT", "AIV", "AIW", "AIZ", "AIZN", "AIZP", "AJAX", "AJG", "AJRD", "AJX", "AJXA", "AKAM", "AKBA", "AKER",
           "AKICU", "AKO/A", "AKO/B", "AKR", "AKRO", "AKTS", "AKTX", "AKU", "AKUS", "AL", "AL^A", "ALAC", "ALACR",
           "ALACW", "ALB", "ALBO", "ALC", "ALCO", "ALDX", "ALE", "ALEC", "ALEX", "ALG", "ALGM", "ALGN", "ALGS", "ALGT",
           "ALIM", "ALIN^A", "ALIN^B", "ALIN^E", "ALJJ", "ALK", "ALKS", "ALL", "ALL^B", "ALL^G", "ALL^H", "ALL^I",
           "ALLE", "ALLK", "ALLO", "ALLT", "ALLY", "ALLY^A", "ALNA", "ALNY", "ALOT", "ALP^Q", "ALPN", "ALRM", "ALRN",
           "ALRS", "ALSK", "ALSN", "ALT", "ALTA", "ALTG", "ALTG^A", "ALTM", "ALTO", "ALTR", "ALTU", "ALTUU", "ALTUW",
           "ALUS", "ALV", "ALVR", "ALX", "ALXN", "ALXO", "ALYA", "AM", "AMAL", "AMAT", "AMBA", "AMBC", "AMBO", "AMC",
           "AMCR", "AMCX", "AMD", "AME", "AMED", "AMEH", "AMER", "AMG", "AMGN", "AMH", "AMH^D", "AMH^E", "AMH^F",
           "AMH^G", "AMH^H", "AMHC", "AMHCU", "AMHCW", "AMK", "AMKR", "AMN", "AMNB", "AMOT", "AMOV", "AMP", "AMPE",
           "AMPG", "AMPGW", "AMPH", "AMPY", "AMR", "AMRB", "AMRC", "AMRK", "AMRN", "AMRS", "AMRX", "AMS", "AMSC",
           "AMSF", "AMST", "AMSWA", "AMT", "AMTB", "AMTBB", "AMTI", "AMTX", "AMWD", "AMWL", "AMX", "AMYT", "AMZN", "AN",
           "ANAB", "ANAT", "ANCN", "ANDA", "ANDAR", "ANDAW", "ANDE", "ANET", "ANF", "ANGI", "ANGN", "ANGO", "ANH",
           "ANH^A", "ANH^B", "ANH^C", "ANIK", "ANIP", "ANIX", "ANNX", "ANPC", "ANSS", "ANTE", "ANTM", "ANVS", "ANY",
           "AOD", "AON", "AONE", "AOS", "AOSL", "AOUT", "AP", "APA", "APAM", "APD", "APDN", "APEI", "APEN", "APG",
           "APH", "APHA", "API", "APLE", "APLS", "APLT", "APM", "APO", "APO^A", "APO^B", "APOG", "APOP", "APOPW",
           "APPF", "APPH", "APPHW", "APPN", "APPS", "APR", "APRE", "APRN", "APSG", "APT", "APTO", "APTS", "APTV",
           "APTV^A", "APTX", "APVO", "APWC", "APXT", "APXTU", "APXTW", "APYX", "AQB", "AQMS", "AQN", "AQNA", "AQNB",
           "AQST", "AQUA", "AR", "ARAV", "ARAY", "ARBG", "ARBGU", "ARBGW", "ARC", "ARCB", "ARCC", "ARCE", "ARCH",
           "ARCO", "ARCT", "ARD", "ARDC", "ARDS", "ARDX", "ARE", "AREC", "ARES", "ARES^A", "ARGD", "ARGO", "ARGO^A",
           "ARGX", "ARI", "ARKIU", "ARKO", "ARKOW", "ARKR", "ARL", "ARLO", "ARLP", "ARMK", "ARMP", "ARNA", "ARNC",
           "AROC", "AROW", "ARPO", "ARQT", "ARR", "ARR^C", "ARRY", "ARTL", "ARTLW", "ARTNA", "ARTW", "ARVN", "ARW",
           "ARWR", "ARYA", "ASA", "ASAN", "ASAQ", "ASAXU", "ASB", "ASB^C", "ASB^D", "ASB^E", "ASB^F", "ASC", "ASG",
           "ASGI", "ASGN", "ASH", "ASIX", "ASLE", "ASLEW", "ASLN", "ASM", "ASMB", "ASML", "ASND", "ASO", "ASPCU",
           "ASPL", "ASPN", "ASPS", "ASPU", "ASR", "ASRT", "ASRV", "ASRVP", "ASTC", "ASTE", "ASUR", "ASX", "ASYS", "AT",
           "ATA", "ATAC", "ATAX", "ATC", "ATCO", "ATCO^D", "ATCO^E", "ATCO^G", "ATCO^H", "ATCO^I", "ATCX", "ATEC",
           "ATEN", "ATEX", "ATGE", "ATH", "ATH^A", "ATH^B", "ATH^C", "ATH^D", "ATHA", "ATHE", "ATHM", "ATHX", "ATI",
           "ATIF", "ATKR", "ATLC", "ATLO", "ATNF", "ATNFW", "ATNI", "ATNM", "ATNX", "ATO", "ATOM", "ATOS", "ATR",
           "ATRA", "ATRC", "ATRI", "ATRO", "ATRS", "ATSG", "ATTO", "ATUS", "ATVI", "ATXI", "AU", "AUB", "AUBAP", "AUBN",
           "AUDC", "AUMN", "AUPH", "AUTL", "AUTO", "AUUD", "AUUDW", "AUVI", "AUY", "AVA", "AVAL", "AVAN", "AVAV", "AVB",
           "AVCO", "AVCT", "AVCTW", "AVD", "AVDG", "AVDL", "AVEO", "AVGO", "AVGOP", "AVGR", "AVID", "AVIR", "AVK",
           "AVLR", "AVNS", "AVNT", "AVNW", "AVO", "AVRO", "AVT", "AVTR", "AVTR^A", "AVXL", "AVY", "AVYA", "AWF", "AWH",
           "AWI", "AWK", "AWP", "AWR", "AWRE", "AWX", "AX", "AXAS", "AXDX", "AXGN", "AXL", "AXLA", "AXNX", "AXO",
           "AXON", "AXP", "AXR", "AXS", "AXS^E", "AXSM", "AXTA", "AXTI", "AXU", "AY", "AYI", "AYLA", "AYRO", "AYTU",
           "AYX", "AZEK", "AZN", "AZO", "AZPN", "AZRE", "AZRX", "AZUL", "AZYO", "AZZ", "B", "BA", "BABA", "BAC",
           "BAC^A", "BAC^B", "BAC^E", "BAC^K", "BAC^L", "BAC^M", "BAC^N", "BAC^O", "BAC^P", "BAF", "BAH", "BAK", "BALY",
           "BAM", "BAMH", "BAMI", "BANC", "BANC^D", "BANC^E", "BAND", "BANF", "BANFP", "BANR", "BANX", "BAOS", "BAP",
           "BASI", "BATL", "BATRA", "BATRK", "BAX", "BB", "BBAR", "BBBY", "BBCP", "BBD", "BBDC", "BBDO", "BBF", "BBGI",
           "BBI", "BBIG", "BBIO", "BBK", "BBL", "BBN", "BBQ", "BBSI", "BBU", "BBVA", "BBW", "BBY", "BC", "BC^A", "BC^B",
           "BC^C", "BCAB", "BCACU", "BCAT", "BCBP", "BCC", "BCDA", "BCDAW", "BCE", "BCEI", "BCEL", "BCH", "BCLI",
           "BCML", "BCO", "BCOR", "BCOV", "BCOW", "BCPC", "BCRX", "BCS", "BCSF", "BCTG", "BCV", "BCV^A", "BCX", "BCYC",
           "BCYP", "BCYPU", "BCYPW", "BDC", "BDJ", "BDL", "BDN", "BDR", "BDSI", "BDSX", "BDTX", "BDX", "BDXB", "BE",
           "BEAM", "BECN", "BEDU", "BEEM", "BEEMW", "BEKE", "BELFA", "BELFB", "BEN", "BENE", "BENER", "BENEU", "BENEW",
           "BEP", "BEP^A", "BEPC", "BERY", "BEST", "BF/A", "BF/B", "BFAM", "BFC", "BFI", "BFIIW", "BFIN", "BFK", "BFLY",
           "BFRA", "BFS", "BFS^D", "BFS^E", "BFST", "BFT", "BFY", "BFZ", "BG", "BGB", "BGCP", "BGFV", "BGH", "BGI",
           "BGIO", "BGLD", "BGNE", "BGR", "BGS", "BGSF", "BGT", "BGX", "BGY", "BH", "BHAT", "BHB", "BHC", "BHE", "BHF",
           "BHFAL", "BHFAN", "BHFAO", "BHFAP", "BHK", "BHLB", "BHP", "BHR", "BHR^B", "BHR^D", "BHSE", "BHSEU", "BHSEW",
           "BHTG", "BHV", "BHVN", "BIDU", "BIF", "BIG", "BIGC", "BIIB", "BILI", "BILL", "BIMI", "BIO", "BIO/B", "BIOC",
           "BIOL", "BIOTU", "BIOX", "BIP", "BIP^A", "BIP^B", "BIPC", "BIT", "BIVI", "BJ", "BJRI", "BK", "BKCC", "BKD",
           "BKE", "BKEP", "BKEPP", "BKH", "BKI", "BKN", "BKNG", "BKR", "BKSC", "BKT", "BKTI", "BKU", "BKYI", "BL",
           "BLBD", "BLCM", "BLCT", "BLD", "BLDG", "BLDP", "BLDR", "BLE", "BLFS", "BLI", "BLIN", "BLK", "BLKB", "BLL",
           "BLMN", "BLNK", "BLNKW", "BLPH", "BLRX", "BLSA", "BLTSU", "BLU", "BLUE", "BLUW", "BLUWU", "BLUWW", "BLW",
           "BLX", "BMA", "BMBL", "BME", "BMEZ", "BMI", "BML^G", "BML^H", "BML^J", "BML^L", "BMO", "BMRA", "BMRC",
           "BMRN", "BMTC", "BMTX", "BMY", "BNED", "BNFT", "BNGO", "BNGOW", "BNL", "BNR", "BNS", "BNSO", "BNTC", "BNTX",
           "BNY", "BOAC", "BOB", "BOCH", "BOE", "BOH", "BOKF", "BOKFL", "BOLT", "BOMN", "BOOM", "BOOT", "BORR", "BOSC",
           "BOTJ", "BOWX", "BOWXU", "BOWXW", "BOX", "BOXL", "BP", "BPFH", "BPMC", "BPMP", "BPOP", "BPOPM", "BPOPN",
           "BPRN", "BPT", "BPTH", "BPTS", "BPY", "BPYPN", "BPYPO", "BPYPP", "BPYU", "BPYUP", "BQ", "BR", "BRBR", "BRBS",
           "BRC", "BREZ", "BREZR", "BREZW", "BRFS", "BRG", "BRG^A", "BRG^C", "BRG^D", "BRID", "BRK/A", "BRK/B", "BRKL",
           "BRKR", "BRKS", "BRLI", "BRLIR", "BRLIU", "BRLIW", "BRMK", "BRN", "BRO", "BROG", "BROGW", "BRP", "BRPA",
           "BRPAR", "BRPAU", "BRPAW", "BRPMU", "BRQS", "BRT", "BRX", "BRY", "BSA", "BSAC", "BSBK", "BSBR", "BSD", "BSE",
           "BSET", "BSGM", "BSIG", "BSL", "BSM", "BSMX", "BSN", "BSPE", "BSQR", "BSRR", "BST", "BSTZ", "BSVN", "BSX",
           "BSX^A", "BSY", "BTA", "BTAI", "BTAQ", "BTAQU", "BTAQW", "BTBT", "BTG", "BTI", "BTN", "BTNB", "BTO", "BTRS",
           "BTRSW", "BTT", "BTU", "BTWN", "BTWNU", "BTWNW", "BTZ", "BUD", "BUFD", "BUFF", "BUI", "BUR", "BURL", "BUSE",
           "BV", "BVH", "BVN", "BVS", "BVXV", "BW", "BWA", "BWAC", "BWACU", "BWACW", "BWAY", "BWB", "BWEN", "BWFG",
           "BWG", "BWL/A", "BWMX", "BWSN", "BWXT", "BX", "BXC", "BXG", "BXMT", "BXMX", "BXP", "BXP^B", "BXRX", "BXS",
           "BXS^A", "BY", "BYD", "BYFC", "BYM", "BYND", "BYSI", "BZH", "BZM", "BZUN", "C", "C^J", "C^K", "C^N", "CAAP",
           "CAAS", "CABA", "CABO", "CAC", "CACC", "CACI", "CADE", "CAE", "CAF", "CAG", "CAH", "CAHCU", "CAI", "CAI^A",
           "CAI^B", "CAJ", "CAKE", "CAL", "CALA", "CALB", "CALM", "CALT", "CALX", "CAMP", "CAMT", "CAN", "CANF", "CANG",
           "CAP", "CAPA", "CAPAU", "CAPAW", "CAPL", "CAPR", "CAR", "CARA", "CARE", "CARG", "CARR", "CARS", "CARV",
           "CAS", "CASA", "CASH", "CASI", "CASS", "CASY", "CAT", "CATB", "CATC", "CATM", "CATO", "CATY", "CB", "CBAH",
           "CBAN", "CBAT", "CBAY", "CBB", "CBB^B", "CBD", "CBFV", "CBH", "CBIO", "CBLI", "CBMB", "CBMG", "CBNK", "CBOE",
           "CBPO", "CBRE", "CBRL", "CBSH", "CBT", "CBTG", "CBTX", "CBU", "CBZ", "CC", "CCAC", "CCAP", "CCB", "CCBG",
           "CCCC", "CCD", "CCEP", "CCF", "CCI", "CCIV", "CCJ", "CCK", "CCL", "CCLP", "CCM", "CCMP", "CCNC", "CCNE",
           "CCNEP", "CCO", "CCOI", "CCRC", "CCRN", "CCS", "CCU", "CCV", "CCX", "CCXI", "CCZ", "CD", "CDAK", "CDAY",
           "CDE", "CDEV", "CDK", "CDLX", "CDMO", "CDMOP", "CDNA", "CDNS", "CDOR", "CDR", "CDR^B", "CDR^C", "CDTX",
           "CDW", "CDXC", "CDXS", "CDZI", "CE", "CEA", "CECE", "CEE", "CEI", "CEIX", "CELC", "CELH", "CELP", "CEM",
           "CEMI", "CEN", "CENHU", "CENT", "CENTA", "CENX", "CEO", "CEPU", "CEQP", "CEQP^", "CERC", "CERE", "CEREW",
           "CERN", "CERS", "CERT", "CET", "CETX", "CETXP", "CETXW", "CEV", "CEVA", "CF", "CFAC", "CFACU", "CFACW",
           "CFB", "CFBK", "CFCV", "CFFI", "CFFN", "CFFVU", "CFG", "CFG^D", "CFG^E", "CFII", "CFIIU", "CFIIW", "CFIV",
           "CFIVU", "CFIVW", "CFMS", "CFR", "CFR^B", "CFRX", "CFVIU", "CFX", "CFXA", "CG", "CGA", "CGBD", "CGC", "CGEM",
           "CGEN", "CGIX", "CGNT", "CGNX", "CGO", "CGRO", "CGROU", "CGROW", "CHAQ", "CHCI", "CHCO", "CHCT", "CHD",
           "CHDN", "CHE", "CHEF", "CHEK", "CHEKZ", "CHFS", "CHFW", "CHGG", "CHH", "CHI", "CHK", "CHKEL", "CHKEW",
           "CHKEZ", "CHKP", "CHMA", "CHMG", "CHMI", "CHMI^A", "CHMI^B", "CHN", "CHNG", "CHNGU", "CHNR", "CHPM", "CHPMU",
           "CHPMW", "CHRA", "CHRS", "CHRW", "CHS", "CHSCL", "CHSCM", "CHSCN", "CHSCO", "CHSCP", "CHT", "CHTR", "CHUY",
           "CHW", "CHWY", "CHX", "CHY", "CI", "CIA", "CIB", "CIDM", "CIEN", "CIF", "CIG", "CIGI", "CIH", "CII", "CIIC",
           "CIICU", "CIICW", "CIK", "CIM", "CIM^A", "CIM^B", "CIM^C", "CIM^D", "CINF", "CINR", "CIO", "CIO^A", "CIR",
           "CIT", "CIT^B", "CIVB", "CIX", "CIXX", "CIZN", "CJJD", "CKH", "CKPT", "CKX", "CL", "CLA", "CLAR", "CLB",
           "CLBK", "CLBS", "CLDB", "CLDR", "CLDT", "CLDX", "CLEU", "CLF", "CLFD", "CLGN", "CLGX", "CLH", "CLI", "CLII",
           "CLIR", "CLLS", "CLM", "CLMT", "CLNC", "CLNE", "CLNN", "CLNNW", "CLNY", "CLNY^G", "CLNY^H", "CLNY^I",
           "CLNY^J", "CLOV", "CLOVW", "CLPR", "CLPS", "CLPT", "CLR", "CLRB", "CLRBZ", "CLRMU", "CLRO", "CLS", "CLSD",
           "CLSK", "CLSN", "CLVR", "CLVRW", "CLVS", "CLVT", "CLW", "CLWT", "CLX", "CLXT", "CM", "CMA", "CMBM", "CMC",
           "CMCL", "CMCM", "CMCO", "CMCSA", "CMCT", "CMD", "CME", "CMFNL", "CMG", "CMI", "CMLF", "CMLFU", "CMLFW",
           "CMLS", "CMO", "CMO^E", "CMP", "CMPI", "CMPR", "CMPS", "CMRE", "CMRE^B", "CMRE^C", "CMRE^D", "CMRE^E",
           "CMRX", "CMS", "CMS^B", "CMSA", "CMSC", "CMSD", "CMT", "CMTL", "CMU", "CNA", "CNBKA", "CNC", "CNCE", "CND",
           "CNDT", "CNET", "CNEY", "CNF", "CNFR", "CNFRL", "CNHI", "CNI", "CNK", "CNMD", "CNNB", "CNNE", "CNO", "CNO^A",
           "CNOB", "CNP", "CNP^B", "CNQ", "CNR", "CNS", "CNSL", "CNSP", "CNST", "CNTG", "CNTY", "CNX", "CNXC", "CNXN",
           "CO", "COCP", "CODA", "CODI", "CODI^A", "CODI^B", "CODI^C", "CODX", "COE", "COF", "COF^G", "COF^H", "COF^I",
           "COF^J", "COF^K", "COFS", "COG", "COGT", "COHN", "COHR", "COHU", "COKE", "COLB", "COLD", "COLL", "COLM",
           "COMM", "COMS", "COMSW", "CONE", "CONN", "CONX", "CONXU", "CONXW", "COO", "COOL", "COOLU", "COOLW", "COOP",
           "COP", "COR", "CORE", "CORR", "CORR^A", "CORT", "COST", "COTY", "COUP", "COVAU", "COWN", "COWNL", "COWNZ",
           "CP", "CPA", "CPAC", "CPAH", "CPB", "CPE", "CPF", "CPG", "CPHC", "CPHI", "CPIX", "CPK", "CPLG", "CPLP",
           "CPRI", "CPRT", "CPRX", "CPS", "CPSH", "CPSI", "CPSR", "CPSS", "CPST", "CPT", "CPTA", "CPTAG", "CPTAL",
           "CPZ", "CQP", "CR", "CRAI", "CRBP", "CRC", "CRD/A", "CRD/B", "CRDF", "CREE", "CREG", "CRESY", "CREX",
           "CREXW", "CRF", "CRH", "CRHC", "CRHM", "CRI", "CRIS", "CRK", "CRKN", "CRL", "CRM", "CRMD", "CRMT", "CRNC",
           "CRNT", "CRNX", "CRON", "CROX", "CRS", "CRSA", "CRSAU", "CRSAW", "CRSP", "CRSR", "CRT", "CRTD", "CRTDW",
           "CRTO", "CRTX", "CRUS", "CRVL", "CRVS", "CRWD", "CRWS", "CRY", "CS", "CSBR", "CSCO", "CSCW", "CSGP", "CSGS",
           "CSII", "CSIQ", "CSL", "CSLT", "CSOD", "CSPI", "CSPR", "CSQ", "CSR", "CSR^C", "CSSE", "CSSEN", "CSSEP",
           "CSTE", "CSTL", "CSTM", "CSTR", "CSU", "CSV", "CSWC", "CSWI", "CSX", "CTA^A", "CTA^B", "CTAC", "CTAQ",
           "CTAQU", "CTAQW", "CTAS", "CTB", "CTBB", "CTBI", "CTDD", "CTEK", "CTG", "CTHR", "CTIB", "CTIC", "CTK",
           "CTLT", "CTMX", "CTO", "CTR", "CTRE", "CTRM", "CTRN", "CTS", "CTSH", "CTSO", "CTT", "CTVA", "CTXR", "CTXRW",
           "CTXS", "CUB", "CUBA", "CUBB", "CUBE", "CUBI", "CUBI^C", "CUBI^D", "CUBI^E", "CUBI^F", "CUE", "CUEN",
           "CUENW", "CUK", "CULP", "CURI", "CURIW", "CURO", "CUTR", "CUZ", "CVA", "CVAC", "CVBF", "CVCO", "CVCY", "CVE",
           "CVEO", "CVET", "CVGI", "CVGW", "CVI", "CVLB", "CVLG", "CVLT", "CVLY", "CVM", "CVNA", "CVR", "CVS", "CVU",
           "CVV", "CVX", "CW", "CWBC", "CWBR", "CWCO", "CWEN", "CWH", "CWK", "CWST", "CWT", "CX", "CXDC", "CXDO", "CXE",
           "CXH", "CXP", "CXW", "CYAD", "CYAN", "CYBE", "CYBR", "CYCC", "CYCN", "CYD", "CYH", "CYRN", "CYRX", "CYTH",
           "CYTHW", "CYTK", "CZNC", "CZR", "CZWI", "CZZ", "D", "DAC", "DADA", "DAIO", "DAKT", "DAL", "DAN", "DAO",
           "DAR", "DARE", "DASH", "DAUG", "DAVA", "DB", "DBD", "DBDR", "DBDRU", "DBDRW", "DBI", "DBL", "DBOC", "DBTX",
           "DBVT", "DBX", "DCBO", "DCF", "DCI", "DCO", "DCOM", "DCOMP", "DCP", "DCP^B", "DCP^C", "DCPH", "DCRB",
           "DCRBU", "DCRBW", "DCRNU", "DCT", "DCTH", "DCUE", "DD", "DDD", "DDEC", "DDF", "DDMX", "DDMXU", "DDMXW",
           "DDOG", "DDS", "DDT", "DE", "DEA", "DECK", "DEFN", "DEH", "DEI", "DELL", "DEN", "DENN", "DEO", "DESP", "DEX",
           "DFEB", "DFFN", "DFH", "DFHT", "DFHTU", "DFHTW", "DFHY", "DFIN", "DFNS", "DFNV", "DFP", "DFPH", "DFPHU",
           "DFPHW", "DFS", "DG", "DGICA", "DGICB", "DGII", "DGLY", "DGNR", "DGNS", "DGX", "DHC", "DHCNI", "DHCNL",
           "DHF", "DHHCU", "DHI", "DHIL", "DHR", "DHR^A", "DHR^B", "DHT", "DHX", "DHY", "DIAX", "DIN", "DIOD", "DIS",
           "DISCA", "DISCB", "DISCK", "DISH", "DIT", "DJAN", "DJCO", "DJUL", "DJUN", "DK", "DKL", "DKNG", "DKS", "DL",
           "DLA", "DLB", "DLCAU", "DLHC", "DLNG", "DLNG^A", "DLNG^B", "DLPN", "DLR", "DLR^C", "DLR^J", "DLR^K", "DLR^L",
           "DLTH", "DLTR", "DLX", "DLY", "DM", "DMAC", "DMAY", "DMB", "DMF", "DMLP", "DMO", "DMRC", "DMS", "DMTK",
           "DMYD", "DMYI", "DNB", "DNK", "DNLI", "DNMR", "DNN", "DNOV", "DNOW", "DNP", "DOC", "DOCT", "DOCU", "DOGZ",
           "DOMO", "DOOO", "DOOR", "DORM", "DOV", "DOW", "DOX", "DOYU", "DPG", "DPW", "DPZ", "DQ", "DRD", "DRE", "DRH",
           "DRH^A", "DRI", "DRIO", "DRIOW", "DRNA", "DRQ", "DRRX", "DRTT", "DRUA", "DRVN", "DS", "DS^B", "DS^C", "DS^D",
           "DSAC", "DSACU", "DSACW", "DSE", "DSEP", "DSGX", "DSKE", "DSKEW", "DSL", "DSM", "DSOC", "DSP", "DSPG", "DSS",
           "DSSI", "DSU", "DSWL", "DSX", "DSX^B", "DT", "DTB", "DTE", "DTEA", "DTF", "DTIL", "DTJ", "DTLA^", "DTP",
           "DTSS", "DTW", "DTY", "DUC", "DUDE", "DUK", "DUK^A", "DUKB", "DUKH", "DUNE", "DUNEU", "DUNEW", "DUO", "DUOT",
           "DVA", "DVAX", "DVD", "DVN", "DWIN", "DWSN", "DX", "DX^C", "DXC", "DXCM", "DXF", "DXPE", "DXR", "DXYN", "DY",
           "DYAI", "DYFN", "DYN", "DYNT", "DZSI", "E", "EA", "EACPU", "EAD", "EAF", "EAI", "EAR", "EARN", "EARS",
           "EAST", "EAT", "EB", "EBAY", "EBAYL", "EBC", "EBF", "EBIX", "EBMT", "EBON", "EBR", "EBS", "EBSB", "EBTC",
           "EC", "ECC", "ECCB", "ECCX", "ECCY", "ECF", "ECF^A", "ECHO", "ECL", "ECOL", "ECOLW", "ECOM", "ECOR", "ECPG",
           "ED", "EDAP", "EDD", "EDF", "EDI", "EDIT", "EDN", "EDRY", "EDSA", "EDTK", "EDTX", "EDTXU", "EDTXW", "EDU",
           "EDUC", "EEA", "EEFT", "EEX", "EFC", "EFC^A", "EFF", "EFL", "EFOI", "EFR", "EFSC", "EFT", "EFX", "EGAN",
           "EGBN", "EGF", "EGHT", "EGIS", "EGLE", "EGO", "EGOV", "EGP", "EGRX", "EGY", "EH", "EHC", "EHI", "EHT",
           "EHTH", "EIC", "EIG", "EIGR", "EIM", "EIX", "EKSO", "EL", "ELA", "ELAN", "ELAT", "ELC", "ELDN", "ELF",
           "ELLO", "ELMD", "ELOX", "ELP", "ELS", "ELSE", "ELTK", "ELVT", "ELY", "ELYS", "EMAN", "EMCF", "EMD", "EME",
           "EMF", "EMKR", "EML", "EMN", "EMO", "EMP", "EMPW", "EMR", "EMX", "ENB", "ENBA", "ENBL", "ENDP", "ENFAU",
           "ENG", "ENIA", "ENIC", "ENJ", "ENLC", "ENLV", "ENNVU", "ENO", "ENOB", "ENPC", "ENPH", "ENR", "ENR^A", "ENS",
           "ENSG", "ENSV", "ENTA", "ENTG", "ENTX", "ENTXW", "ENV", "ENVA", "ENVB", "ENVIU", "ENX", "ENZ", "EOD", "EOG",
           "EOI", "EOLS", "EOS", "EOSE", "EOSEW", "EOT", "EP^C", "EPAC", "EPAM", "EPAY", "EPC", "EPD", "EPHYU", "EPIX",
           "EPM", "EPR", "EPR^C", "EPR^E", "EPR^G", "EPRT", "EPSN", "EPZM", "EQ", "EQBK", "EQC", "EQC^D", "EQD", "EQH",
           "EQH^A", "EQH^C", "EQIX", "EQNR", "EQOS", "EQOSW", "EQR", "EQS", "EQT", "EQX", "ERC", "ERES", "ERESU",
           "ERESW", "ERF", "ERH", "ERIC", "ERIE", "ERII", "ERJ", "ERYP", "ES", "ESBK", "ESCA", "ESE", "ESEA", "ESGC",
           "ESGR", "ESGRO", "ESGRP", "ESI", "ESLT", "ESNT", "ESP", "ESPR", "ESQ", "ESRT", "ESS", "ESSA", "ESSC",
           "ESSCR", "ESSCU", "ESSCW", "ESTA", "ESTC", "ESTE", "ESXB", "ET", "ETAC", "ETACU", "ETACW", "ETB", "ETG",
           "ETH", "ETI^", "ETJ", "ETM", "ETN", "ETNB", "ETO", "ETON", "ETP^C", "ETP^D", "ETP^E", "ETR", "ETRN", "ETSY",
           "ETTX", "ETV", "ETW", "ETWO", "ETX", "ETY", "EUCG", "EUCR", "EUCRU", "EUCRW", "EURN", "EUSGU", "EV", "EVA",
           "EVAX", "EVBG", "EVBN", "EVC", "EVER", "EVF", "EVFM", "EVG", "EVGN", "EVH", "EVI", "EVK", "EVLO", "EVM",
           "EVN", "EVOJU", "EVOK", "EVOL", "EVOP", "EVR", "EVRG", "EVRI", "EVT", "EVTC", "EVV", "EVY", "EW", "EWBC",
           "EXAS", "EXC", "EXD", "EXEL", "EXFO", "EXG", "EXK", "EXLS", "EXN", "EXP", "EXPC", "EXPCU", "EXPCW", "EXPD",
           "EXPE", "EXPI", "EXPO", "EXPR", "EXR", "EXTN", "EXTR", "EYE", "EYEG", "EYEN", "EYES", "EYESW", "EYPT",
           "EZGO", "EZPW", "F", "F^B", "F^C", "FAF", "FAII", "FAM", "FAMI", "FANG", "FANH", "FARM", "FARO", "FAST",
           "FAT", "FATBP", "FATBW", "FATE", "FAUG", "FAX", "FB", "FBC", "FBHS", "FBIO", "FBIOP", "FBIZ", "FBK", "FBMS",
           "FBNC", "FBP", "FBRX", "FBSS", "FC", "FCAC", "FCACU", "FCACW", "FCAP", "FCBC", "FCBP", "FCCO", "FCCY",
           "FCEL", "FCF", "FCFS", "FCN", "FCNCA", "FCNCP", "FCO", "FCPT", "FCRD", "FCRZ", "FCT", "FCX", "FDBC", "FDEC",
           "FDEU", "FDG", "FDMT", "FDP", "FDS", "FDUS", "FDUSG", "FDUSZ", "FDX", "FE", "FEBZ", "FEDU", "FEDX", "FEI",
           "FEIM", "FELE", "FEN", "FENC", "FENG", "FEO", "FET", "FEYE", "FF", "FFA", "FFBC", "FFBW", "FFC", "FFEB",
           "FFG", "FFHL", "FFIC", "FFIN", "FFIV", "FFNW", "FFWM", "FGB", "FGBI", "FGEN", "FGF", "FGFPP", "FGNA", "FGRO",
           "FHB", "FHI", "FHN", "FHN^A", "FHN^B", "FHN^C", "FHN^D", "FHN^E", "FHTX", "FI", "FIBK", "FICO", "FIF",
           "FIII", "FIIIU", "FIIIW", "FINMU", "FINS", "FINV", "FIS", "FISI", "FISV", "FITB", "FITBI", "FITBO", "FITBP",
           "FIV", "FIVE", "FIVN", "FIX", "FIXX", "FIZZ", "FJAN", "FJUL", "FJUN", "FL", "FLAC", "FLACU", "FLACW", "FLC",
           "FLDM", "FLEX", "FLGT", "FLIC", "FLIR", "FLL", "FLMN", "FLMNW", "FLNG", "FLNT", "FLO", "FLOW", "FLR", "FLS",
           "FLT", "FLUX", "FLV", "FLWS", "FLXN", "FLXS", "FLY", "FMAC", "FMAG", "FMAO", "FMAY", "FMBH", "FMBI", "FMBIO",
           "FMBIP", "FMC", "FMN", "FMNB", "FMO", "FMS", "FMTX", "FMX", "FMY", "FN", "FNB", "FNB^E", "FNCB", "FND",
           "FNF", "FNHC", "FNKO", "FNLC", "FNOV", "FNV", "FNWB", "FOCS", "FOCT", "FOE", "FOF", "FOLD", "FONR", "FOR",
           "FORD", "FOREU", "FORM", "FORR", "FORTY", "FOSL", "FOUR", "FOX", "FOXA", "FOXF", "FOXWU", "FPAC", "FPAY",
           "FPF", "FPH", "FPI", "FPI^B", "FPL", "FPRO", "FPRX", "FR", "FRA", "FRAF", "FRBA", "FRBK", "FRC", "FRC^G",
           "FRC^H", "FRC^I", "FRC^J", "FRC^K", "FRC^L", "FRD", "FREE", "FREEW", "FREQ", "FRG", "FRGAP", "FRGI", "FRHC",
           "FRLN", "FRME", "FRO", "FROG", "FRPH", "FRPT", "FRSX", "FRT", "FRT^C", "FRTA", "FRX", "FSBW", "FSD", "FSEA",
           "FSEP", "FSFG", "FSI", "FSII", "FSK", "FSKR", "FSLF", "FSLR", "FSLY", "FSM", "FSMO", "FSP", "FSR", "FSRV",
           "FSRVU", "FSRVW", "FSRXU", "FSS", "FSSIU", "FST", "FSTR", "FSTX", "FSV", "FT", "FTAI", "FTAI^A", "FTAI^B",
           "FTCH", "FTCV", "FTCVU", "FTCVW", "FTDR", "FTEK", "FTF", "FTFT", "FTHM", "FTHY", "FTI", "FTIV", "FTIVU",
           "FTIVW", "FTK", "FTNT", "FTOC", "FTOCU", "FTOCW", "FTS", "FTSI", "FTV", "FTV^A", "FUBO", "FUL", "FULC",
           "FULT", "FULTP", "FUN", "FUNC", "FUND", "FUNL", "FURY", "FUSB", "FUSE", "FUSN", "FUTU", "FUV", "FVAM",
           "FVCB", "FVE", "FVRR", "FWAA", "FWONA", "FWONK", "FWP", "FWRD", "FXNC", "G", "GAB", "GAB^G", "GAB^H",
           "GAB^J", "GAB^K", "GABC", "GAIA", "GAIN", "GAINL", "GAINM", "GALT", "GAM", "GAM^B", "GAN", "GASS", "GATO",
           "GATX", "GAU", "GB", "GBAB", "GBCI", "GBDC", "GBIO", "GBL", "GBLI", "GBLIL", "GBNY", "GBOX", "GBR", "GBS",
           "GBT", "GBX", "GCACU", "GCBC", "GCI", "GCMG", "GCMGW", "GCO", "GCP", "GCV", "GD", "GDDY", "GDEN", "GDL",
           "GDL^C", "GDO", "GDOT", "GDP", "GDRX", "GDS", "GDV", "GDV^G", "GDV^H", "GDYN", "GDYNW", "GE", "GECC",
           "GECCL", "GECCM", "GECCN", "GEF", "GEG", "GEL", "GEN", "GENC", "GENE", "GEO", "GEOS", "GER", "GERN", "GES",
           "GEVO", "GF", "GFED", "GFF", "GFI", "GFL", "GFLU", "GFN", "GFNCP", "GFNSZ", "GFX", "GGAL", "GGB", "GGG",
           "GGM", "GGN", "GGN^B", "GGO", "GGO^A", "GGT", "GGT^E", "GGT^G", "GGZ", "GGZ^A", "GH", "GHACU", "GHC", "GHG",
           "GHL", "GHLD", "GHM", "GHSI", "GHVI", "GHVIU", "GHVIW", "GHY", "GIB", "GIFI", "GIGGU", "GIGM", "GIII", "GIK",
           "GIL", "GILD", "GILT", "GIM", "GIS", "GIX", "GJH", "GJO", "GJP", "GJR", "GJS", "GJT", "GKOS", "GL", "GL^C",
           "GLAD", "GLADL", "GLAQ", "GLAQU", "GLAQW", "GLBS", "GLBZ", "GLDD", "GLDG", "GLEO", "GLG", "GLMD", "GLNG",
           "GLO", "GLOB", "GLOG", "GLOG^A", "GLOP", "GLOP^A", "GLOP^B", "GLOP^C", "GLP", "GLP^A", "GLPG", "GLPI", "GLQ",
           "GLRE", "GLSI", "GLT", "GLTO", "GLU", "GLU^A", "GLU^B", "GLUU", "GLV", "GLW", "GLYC", "GM", "GMAB", "GMBL",
           "GMBLW", "GMBTU", "GMDA", "GME", "GMED", "GMIIU", "GMLP", "GMLPP", "GMRE", "GMRE^A", "GMS", "GMTA", "GMTX",
           "GNACU", "GNCA", "GNE", "GNE^A", "GNFT", "GNK", "GNL", "GNL^A", "GNL^B", "GNLN", "GNMK", "GNOG", "GNOGW",
           "GNPK", "GNPX", "GNRC", "GNRS", "GNRSU", "GNRSW", "GNSS", "GNT", "GNT^A", "GNTX", "GNTY", "GNUS", "GNW",
           "GO", "GOAC", "GOCO", "GOED", "GOEV", "GOEVW", "GOF", "GOGL", "GOGO", "GOL", "GOLD", "GOLF", "GOOD", "GOODM",
           "GOODN", "GOOG", "GOOGL", "GOOS", "GORO", "GOSS", "GOVX", "GOVXW", "GOVZ", "GP", "GPACU", "GPC", "GPI",
           "GPJA", "GPK", "GPL", "GPM", "GPMT", "GPN", "GPP", "GPRE", "GPRK", "GPRO", "GPS", "GPX", "GRA", "GRAY",
           "GRBK", "GRC", "GRCL", "GRCY", "GRCYU", "GRCYW", "GRF", "GRFS", "GRIL", "GRIN", "GRMN", "GRNQ", "GRNV",
           "GRNVR", "GRNVU", "GRNVW", "GROW", "GRPN", "GRSV", "GRSVU", "GRSVW", "GRTS", "GRTX", "GRUB", "GRVY", "GRWG",
           "GRX", "GS", "GS^A", "GS^C", "GS^D", "GS^J", "GS^K", "GS^N", "GSAH", "GSAQU", "GSAT", "GSBC", "GSBD", "GSEE",
           "GSHD", "GSID", "GSIT", "GSK", "GSKY", "GSL", "GSL^B", "GSLD", "GSM", "GSMG", "GSMGW", "GSS", "GSUM", "GSUS",
           "GSV", "GSX", "GT", "GTBP", "GTE", "GTEC", "GTES", "GTH", "GTHX", "GTIM", "GTIP", "GTLS", "GTN", "GTS",
           "GTT", "GTY", "GTYH", "GURE", "GUT", "GUT^A", "GUT^C", "GVA", "GVP", "GWAC", "GWACW", "GWB", "GWGH", "GWPH",
           "GWRE", "GWRS", "GWW", "GXGX", "GXGXU", "GXGXW", "GYRO", "H", "HA", "HAAC", "HAACU", "HAACW", "HAE", "HAFC",
           "HAIN", "HAL", "HALL", "HALO", "HAPP", "HARP", "HAS", "HASI", "HAYN", "HBAN", "HBANN", "HBANO", "HBB",
           "HBCP", "HBI", "HBIO", "HBM", "HBMD", "HBNC", "HBP", "HBT", "HCA", "HCAP", "HCAPZ", "HCAQ", "HCAR", "HCARU",
           "HCARW", "HCAT", "HCC", "HCCCU", "HCCI", "HCDI", "HCHC", "HCI", "HCICU", "HCIIU", "HCKT", "HCM", "HCSG",
           "HCXY", "HCXZ", "HD", "HDB", "HDSN", "HE", "HEAR", "HEC", "HECCU", "HECCW", "HEES", "HEGD", "HEI", "HEI/A",
           "HELE", "HELX", "HEP", "HEPA", "HEQ", "HES", "HESM", "HEXO", "HFBL", "HFC", "HFFG", "HFRO", "HFRO^A", "HFWA",
           "HGBL", "HGEN", "HGH", "HGLB", "HGSH", "HGV", "HHC", "HHR", "HI", "HIBB", "HIE", "HIFS", "HIG", "HIG^G",
           "HIGA", "HIHO", "HII", "HIL", "HIMS", "HIMX", "HIO", "HIW", "HIX", "HJLI", "HJLIW", "HKIB", "HL", "HL^B",
           "HLAHU", "HLF", "HLG", "HLI", "HLIO", "HLIT", "HLM^", "HLNE", "HLT", "HLX", "HLXA", "HMC", "HMCO", "HMCOU",
           "HMCOW", "HMG", "HMHC", "HMI", "HMLP", "HMLP^A", "HMN", "HMNF", "HMPT", "HMST", "HMSY", "HMTV", "HMY",
           "HNGR", "HNI", "HNNA", "HNP", "HNRG", "HNW", "HOFT", "HOFV", "HOFVW", "HOG", "HOL", "HOLI", "HOLUU", "HOLUW",
           "HOLX", "HOMB", "HOME", "HON", "HONE", "HOOK", "HOPE", "HOTH", "HOV", "HOVNP", "HP", "HPE", "HPF", "HPI",
           "HPK", "HPKEW", "HPP", "HPQ", "HPR", "HPS", "HPX", "HQH", "HQI", "HQL", "HQY", "HR", "HRB", "HRC", "HRI",
           "HRL", "HRMY", "HROW", "HRTG", "HRTX", "HRZN", "HSAQ", "HSBC", "HSC", "HSDT", "HSIC", "HSII", "HSKA", "HSON",
           "HST", "HSTM", "HSTO", "HSY", "HT", "HT^C", "HT^D", "HT^E", "HTA", "HTBI", "HTBK", "HTBX", "HTD", "HTFA",
           "HTGC", "HTGM", "HTH", "HTHT", "HTIA", "HTLD", "HTLF", "HTLFP", "HTOO", "HTOOW", "HTPA", "HTY", "HUBB",
           "HUBG", "HUBS", "HUDI", "HUGE", "HUIZ", "HUM", "HUN", "HURC", "HURN", "HUSA", "HUSN", "HUYA", "HVBC", "HVT",
           "HVT/A", "HWBK", "HWC", "HWCC", "HWCPL", "HWCPZ", "HWKN", "HWM", "HWM^", "HX", "HXL", "HY", "HYB", "HYFM",
           "HYI", "HYLN", "HYMC", "HYMCL", "HYMCW", "HYMCZ", "HYRE", "HYT", "HZAC", "HZN", "HZNP", "HZO", "HZON", "IAA",
           "IAC", "IACA", "IAE", "IAF", "IAG", "IART", "IBA", "IBCP", "IBEX", "IBHF", "IBIO", "IBKR", "IBM", "IBN",
           "IBOC", "IBP", "IBTX", "ICAD", "ICBK", "ICCC", "ICCH", "ICD", "ICE", "ICFI", "ICHR", "ICL", "ICLK", "ICLR",
           "ICMB", "ICON", "ICPT", "ICUI", "ID", "IDA", "IDCC", "IDE", "IDEX", "IDN", "IDRA", "IDT", "IDXG", "IDXX",
           "IDYA", "IEA", "IEAWW", "IEC", "IEP", "IESC", "IEX", "IFF", "IFFT", "IFMK", "IFN", "IFRX", "IFS", "IGA",
           "IGAC", "IGACU", "IGACW", "IGC", "IGD", "IGI", "IGIC", "IGICW", "IGMS", "IGNYU", "IGR", "IGT", "IH", "IHC",
           "IHD", "IHG", "IHIT", "IHRT", "IHT", "IHTA", "IIAC", "IID", "IIF", "III", "IIII", "IIIIU", "IIIIW", "IIIN",
           "IIIV", "IIM", "IIN", "IIPR", "IIPR^A", "IIVI", "IIVIP", "IKNX", "IKT", "ILMN", "ILPT", "IMAB", "IMAC",
           "IMACW", "IMAX", "IMBI", "IMCR", "IMGN", "IMH", "IMKTA", "IMMP", "IMMR", "IMNM", "IMO", "IMOS", "IMPX",
           "IMRA", "IMRN", "IMRNW", "IMTE", "IMTX", "IMTXW", "IMUX", "IMV", "IMVT", "IMXI", "INBK", "INBKL", "INBKZ",
           "INBX", "INCY", "INDB", "INDO", "INDT", "INFI", "INFN", "INFO", "INFU", "INFY", "ING", "INGN", "INGR",
           "INKAU", "INM", "INMB", "INMD", "INN", "INN^D", "INN^E", "INO", "INOD", "INOV", "INPX", "INS", "INSE",
           "INSG", "INSI", "INSM", "INSP", "INSW", "INSW^A", "INT", "INTC", "INTG", "INTT", "INTU", "INTZ", "INUV",
           "INVA", "INVE", "INVH", "INVO", "INZY", "IO", "IONS", "IOR", "IOSP", "IOVA", "IP", "IPA", "IPAR", "IPDN",
           "IPG", "IPGP", "IPHA", "IPHI", "IPI", "IPLDP", "IPOD", "IPOE", "IPOF", "IPV", "IPWR", "IQ", "IQI", "IQV",
           "IR", "IRBT", "IRCP", "IRDM", "IRIX", "IRL", "IRM", "IRMD", "IROQ", "IRR", "IRS", "IRT", "IRTC", "IRWD",
           "ISBC", "ISD", "ISDR", "ISEE", "ISIG", "ISNS", "ISR", "ISRG", "ISSC", "ISTR", "ISUN", "IT", "ITAC", "ITACU",
           "ITACW", "ITCB", "ITCI", "ITGR", "ITHXU", "ITI", "ITIC", "ITMR", "ITOS", "ITP", "ITQRU", "ITRG", "ITRI",
           "ITRM", "ITRN", "ITT", "ITUB", "ITW", "IVA", "IVAC", "IVC", "IVDG", "IVH", "IVLC", "IVR", "IVR^A", "IVR^B",
           "IVR^C", "IVRA", "IVSG", "IVZ", "IX", "IZEA", "J", "JACK", "JAGX", "JAKK", "JAMF", "JAN", "JANZ", "JAX",
           "JAZZ", "JBGS", "JBHT", "JBK", "JBL", "JBLU", "JBSS", "JBT", "JCE", "JCI", "JCICU", "JCO", "JCOM", "JCS",
           "JCTCF", "JD", "JDD", "JE", "JEF", "JELD", "JEMD", "JEQ", "JFIN", "JFR", "JFU", "JG", "JGH", "JHAA", "JHB",
           "JHG", "JHI", "JHS", "JHX", "JIH", "JILL", "JJSF", "JKHY", "JKS", "JLL", "JLS", "JMIA", "JMM", "JMP",
           "JMPNL", "JMPNZ", "JNCE", "JNJ", "JNPR", "JOB", "JOBS", "JOE", "JOF", "JOFFU", "JOUT", "JP", "JPC", "JPI",
           "JPM", "JPM^C", "JPM^D", "JPM^G", "JPM^H", "JPM^J", "JPS", "JPT", "JQC", "JRI", "JRJC", "JRO", "JRS", "JRSH",
           "JRVR", "JSD", "JSM", "JT", "JTA", "JTD", "JUPW", "JUPWW", "JVA", "JW/A", "JW/B", "JWN", "JWS", "JYAC",
           "JYNT", "K", "KAI", "KAIIU", "KAIRU", "KALA", "KALU", "KALV", "KAMN", "KAR", "KB", "KBAL", "KBH", "KBNT",
           "KBNTW", "KBR", "KBSF", "KC", "KCAPL", "KDMN", "KDNY", "KDP", "KE", "KELYA", "KELYB", "KEN", "KEP", "KEQU",
           "KERN", "KERNW", "KEX", "KEY", "KEY^I", "KEY^J", "KEY^K", "KEYS", "KF", "KFFB", "KFRC", "KFS", "KFY", "KGC",
           "KHC", "KIDS", "KIIIU", "KIM", "KIM^L", "KIM^M", "KIN", "KINS", "KINZ", "KINZU", "KINZW", "KIO", "KIQ",
           "KIRK", "KJUL", "KKR", "KKR^A", "KKR^B", "KKR^C", "KL", "KLAC", "KLAQU", "KLDO", "KLIC", "KLR", "KLXE",
           "KMB", "KMDA", "KMF", "KMI", "KMPH", "KMPR", "KMT", "KMX", "KN", "KNDI", "KNGS", "KNL", "KNOP", "KNSA",
           "KNSL", "KNTE", "KNX", "KO", "KOD", "KODK", "KOF", "KOP", "KOPN", "KOR", "KOS", "KOSS", "KPTI", "KR", "KRA",
           "KRBP", "KRC", "KREF", "KRG", "KRKR", "KRMD", "KRNLU", "KRNT", "KRNY", "KRO", "KRON", "KROS", "KRP", "KRTX",
           "KRUS", "KRYS", "KSM", "KSMT", "KSMTU", "KSMTW", "KSPN", "KSS", "KSU", "KSU^", "KT", "KTB", "KTCC", "KTF",
           "KTH", "KTN", "KTOS", "KTRA", "KUKE", "KURA", "KVHI", "KW", "KWAC", "KWR", "KXIN", "KYMR", "KYN", "KZIA",
           "KZR", "L", "LABP", "LAC", "LACQ", "LACQU", "LACQW", "LAD", "LADR", "LAIX", "LAKE", "LAMR", "LANC", "LAND",
           "LANDM", "LANDO", "LARK", "LASR", "LATN", "LATNU", "LATNW", "LAUR", "LAWS", "LAZ", "LAZR", "LAZRW", "LAZY",
           "LB", "LBAI", "LBC", "LBRDA", "LBRDK", "LBRDP", "LBRT", "LBTYA", "LBTYB", "LBTYK", "LC", "LCAP", "LCAPU",
           "LCAPW", "LCI", "LCII", "LCNB", "LCTX", "LCUT", "LCY", "LCYAU", "LCYAW", "LDI", "LDL", "LDOS", "LDP", "LE",
           "LEA", "LEAF", "LEAP", "LECO", "LEDS", "LEE", "LEG", "LEGH", "LEGN", "LEGOU", "LEJU", "LEN", "LEO", "LESL",
           "LEU", "LEVI", "LEVL", "LEVLP", "LEXX", "LEXXW", "LFC", "LFT", "LFTR", "LFTRU", "LFTRW", "LFUS", "LFVN",
           "LGACU", "LGHL", "LGHLW", "LGI", "LGIH", "LGL", "LGND", "LGVN", "LH", "LHCG", "LHDX", "LHX", "LI", "LIFE",
           "LII", "LILA", "LILAK", "LIN", "LINC", "LIND", "LINX", "LIQT", "LITB", "LITE", "LIV", "LIVE", "LIVK",
           "LIVKU", "LIVKW", "LIVN", "LIVX", "LIXT", "LIXTW", "LIZI", "LJAQU", "LJPC", "LKCO", "LKFN", "LKQ", "LL",
           "LLIT", "LLNW", "LLY", "LMACU", "LMAOU", "LMAT", "LMB", "LMFA", "LMND", "LMNL", "LMNR", "LMNX", "LMPX",
           "LMRK", "LMRKN", "LMRKO", "LMRKP", "LMST", "LMT", "LNC", "LND", "LNDC", "LNFA", "LNG", "LNN", "LNSR", "LNT",
           "LNTH", "LOAC", "LOACR", "LOACW", "LOAN", "LOB", "LOCO", "LODE", "LOGC", "LOGI", "LOKB", "LOMA", "LOOP",
           "LOPE", "LORL", "LOTZ", "LOTZW", "LOV", "LOVE", "LOW", "LPCN", "LPG", "LPI", "LPL", "LPLA", "LPRO", "LPSN",
           "LPTH", "LPTX", "LPX", "LQDA", "LQDT", "LRCX", "LRMR", "LRN", "LSAQ", "LSBK", "LSCC", "LSEA", "LSEAW", "LSF",
           "LSI", "LSPD", "LSTR", "LSXMA", "LSXMB", "LSXMK", "LTBR", "LTC", "LTHM", "LTRN", "LTRPA", "LTRPB", "LTRX",
           "LU", "LUB", "LULU", "LUMN", "LUMO", "LUNA", "LUNG", "LUV", "LUXA", "LUXAU", "LUXAW", "LUXE", "LVS", "LW",
           "LWACU", "LWAY", "LX", "LXEH", "LXFR", "LXP", "LXP^C", "LXRX", "LXU", "LYB", "LYFE", "LYFT", "LYG", "LYL",
           "LYRA", "LYTS", "LYV", "LZB", "M", "MA", "MAA", "MAA^I", "MAAC", "MAACU", "MAACW", "MAC", "MACAU", "MACK",
           "MACU", "MACUU", "MACUW", "MAG", "MAGS", "MAIN", "MAN", "MANH", "MANT", "MANU", "MAR", "MARA", "MARK",
           "MARPS", "MAS", "MASI", "MASS", "MAT", "MATW", "MATX", "MAV", "MAX", "MAXN", "MAXR", "MAYS", "MBBB", "MBCN",
           "MBI", "MBII", "MBIN", "MBINO", "MBINP", "MBIO", "MBND", "MBNKP", "MBOT", "MBRX", "MBT", "MBUU", "MBWM",
           "MC", "MCA", "MCADU", "MCB", "MCBC", "MCBS", "MCD", "MCF", "MCFE", "MCFT", "MCHP", "MCHX", "MCI", "MCK",
           "MCMJ", "MCMJW", "MCN", "MCO", "MCR", "MCRB", "MCRI", "MCS", "MCY", "MD", "MDB", "MDC", "MDCA", "MDGL",
           "MDGS", "MDGSW", "MDIA", "MDJH", "MDLA", "MDLQ", "MDLX", "MDLY", "MDLZ", "MDNA", "MDP", "MDRR", "MDRRP",
           "MDRX", "MDT", "MDU", "MDVL", "MDWD", "MDWT", "MDXG", "MEC", "MED", "MEDP", "MEDS", "MEG", "MEI", "MEIP",
           "MELI", "MEN", "MEOH", "MER^K", "MERC", "MESA", "MESO", "MET", "MET^A", "MET^E", "MET^F", "METC", "METX",
           "METXW", "MFA", "MFA^B", "MFA^C", "MFC", "MFD", "MFG", "MFGP", "MFH", "MFIN", "MFINL", "MFL", "MFM", "MFMS",
           "MFNC", "MFT", "MFV", "MG", "MGA", "MGEE", "MGF", "MGI", "MGIC", "MGLN", "MGM", "MGNI", "MGNX", "MGP",
           "MGPI", "MGR", "MGRB", "MGRC", "MGTA", "MGTX", "MGU", "MGY", "MGYR", "MH^A", "MH^C", "MH^D", "MHD", "MHE",
           "MHF", "MHH", "MHI", "MHK", "MHLA", "MHLD", "MHN", "MHNC", "MHO", "MIC", "MICT", "MIDD", "MIE", "MIG", "MIK",
           "MILE", "MILEW", "MIME", "MIN", "MIND", "MINDP", "MIRM", "MIST", "MITK", "MITO", "MITT", "MITT^A", "MITT^B",
           "MITT^C", "MIXT", "MIY", "MKC", "MKD", "MKGI", "MKL", "MKSI", "MKTX", "MLAB", "MLAC", "MLACU", "MLACW",
           "MLCO", "MLHR", "MLI", "MLM", "MLND", "MLP", "MLR", "MLSS", "MLVF", "MMAC", "MMC", "MMD", "MMI", "MMLP",
           "MMM", "MMP", "MMS", "MMSI", "MMT", "MMU", "MMX", "MMYT", "MN", "MNDO", "MNKD", "MNOV", "MNP", "MNPR", "MNR",
           "MNR^C", "MNRL", "MNRO", "MNSB", "MNSBP", "MNSO", "MNST", "MNTK", "MNTX", "MO", "MOD", "MODN", "MODV",
           "MOFG", "MOGO", "MOGU", "MOH", "MOHO", "MOMO", "MONCU", "MOR", "MORF", "MORN", "MOS", "MOSY", "MOTN",
           "MOTNU", "MOTNW", "MOTS", "MOTV", "MOV", "MOXC", "MP", "MPA", "MPAA", "MPB", "MPC", "MPLN", "MPLX", "MPV",
           "MPW", "MPWR", "MPX", "MQT", "MQY", "MRAC", "MRACU", "MRACW", "MRAM", "MRBK", "MRC", "MRCC", "MRCY", "MREO",
           "MRIN", "MRK", "MRKR", "MRLN", "MRM", "MRNA", "MRNS", "MRO", "MRSK", "MRSN", "MRTN", "MRTX", "MRUS", "MRVI",
           "MRVL", "MS", "MS^A", "MS^E", "MS^F", "MS^I", "MS^K", "MS^L", "MSA", "MSACU", "MSB", "MSBI", "MSC", "MSCI",
           "MSD", "MSEX", "MSFT", "MSGE", "MSGM", "MSGN", "MSGS", "MSI", "MSM", "MSN", "MSON", "MSP", "MSTB", "MSTR",
           "MSVB", "MSVX", "MT", "MTA", "MTAC", "MTACU", "MTACW", "MTB", "MTBC", "MTBCP", "MTC", "MTCH", "MTCN", "MTCR",
           "MTD", "MTDR", "MTEM", "MTEX", "MTG", "MTH", "MTL", "MTL^", "MTLS", "MTN", "MTNB", "MTOR", "MTP", "MTR",
           "MTRN", "MTRX", "MTSC", "MTSI", "MTSL", "MTT", "MTW", "MTX", "MTZ", "MU", "MUA", "MUC", "MUDS", "MUDSU",
           "MUDSW", "MUE", "MUFG", "MUH", "MUI", "MUJ", "MUR", "MUS", "MUSA", "MUX", "MVBF", "MVF", "MVIS", "MVO",
           "MVT", "MWA", "MWK", "MX", "MXC", "MXE", "MXF", "MXIM", "MXL", "MYC", "MYD", "MYE", "MYF", "MYFW", "MYGN",
           "MYI", "MYJ", "MYN", "MYO", "MYOV", "MYRG", "MYSZ", "MYT", "MYTE", "MZA", "NAACU", "NAC", "NAD", "NAII",
           "NAK", "NAKD", "NAN", "NAOV", "NAPR", "NARI", "NAT", "NATH", "NATI", "NATR", "NAV", "NAV^D", "NAVB", "NAVI",
           "NAZ", "NBA", "NBAC", "NBACR", "NBACU", "NBACW", "NBB", "NBEV", "NBH", "NBHC", "NBIX", "NBLX", "NBN", "NBO",
           "NBR", "NBR^A", "NBRV", "NBSE", "NBTB", "NBTX", "NBW", "NBY", "NC", "NCA", "NCB", "NCBS", "NCLH", "NCMI",
           "NCNA", "NCNO", "NCR", "NCSM", "NCTY", "NCV", "NCV^A", "NCZ", "NCZ^A", "NDAQ", "NDLS", "NDMO", "NDP", "NDRA",
           "NDRAW", "NDSN", "NEA", "NEBC", "NEBCU", "NEBCW", "NEE", "NEE^K", "NEE^N", "NEE^O", "NEE^P", "NEE^Q", "NEM",
           "NEN", "NEO", "NEOG", "NEON", "NEOS", "NEP", "NEPH", "NEPT", "NERV", "NES", "NESR", "NESRW", "NET", "NETE",
           "NETI", "NEU", "NEV", "NEW", "NEWA", "NEWR", "NEWT", "NEWTI", "NEWTL", "NEWTZ", "NEX", "NEXA", "NEXI",
           "NEXT", "NFBK", "NFE", "NFG", "NFH", "NFJ", "NFLX", "NG", "NGA", "NGAC", "NGACU", "NGACW", "NGD", "NGG",
           "NGL", "NGL^B", "NGL^C", "NGM", "NGMS", "NGS", "NGVC", "NGVT", "NH", "NHA", "NHC", "NHF", "NHF^A", "NHI",
           "NHIC", "NHICU", "NHICW", "NHLD", "NHLDW", "NHS", "NHTC", "NI", "NI^B", "NICE", "NICK", "NID", "NIE", "NIM",
           "NINE", "NIO", "NIQ", "NISN", "NIU", "NJR", "NJUL", "NJV", "NK", "NKE", "NKG", "NKLA", "NKSH", "NKTR",
           "NKTX", "NKX", "NL", "NLOK", "NLS", "NLSN", "NLSP", "NLSPW", "NLTX", "NLY", "NLY^F", "NLY^G", "NLY^I", "NM",
           "NM^G", "NM^H", "NMCI", "NMCO", "NMFC", "NMFCL", "NMI", "NMIH", "NMK^B", "NMK^C", "NML", "NMM", "NMMC",
           "NMMCU", "NMMCW", "NMR", "NMRD", "NMRK", "NMS", "NMT", "NMTR", "NMY", "NMZ", "NNA", "NNBR", "NNDM", "NNI",
           "NNN", "NNN^F", "NNOX", "NNVC", "NNY", "NOA", "NOAC", "NOACU", "NOACW", "NOAH", "NOC", "NODK", "NOG", "NOK",
           "NOM", "NOMD", "NOV", "NOVA", "NOVN", "NOVT", "NOW", "NP", "NPA", "NPAUU", "NPAWW", "NPK", "NPN", "NPO",
           "NPTN", "NPV", "NQP", "NR", "NRACU", "NRBO", "NRC", "NREF", "NREF^A", "NRG", "NRGX", "NRIM", "NRIX", "NRK",
           "NRO", "NRP", "NRT", "NRUC", "NRZ", "NRZ^A", "NRZ^B", "NRZ^C", "NS", "NS^A", "NS^B", "NS^C", "NSA", "NSA^A",
           "NSC", "NSCO", "NSEC", "NSH", "NSIT", "NSL", "NSP", "NSPR", "NSS", "NSSC", "NSTB", "NSTG", "NSYS", "NTAP",
           "NTB", "NTCO", "NTCT", "NTEC", "NTES", "NTG", "NTGR", "NTIC", "NTIP", "NTLA", "NTN", "NTNX", "NTP", "NTR",
           "NTRA", "NTRS", "NTRSO", "NTST", "NTUS", "NTWK", "NTZ", "NUAN", "NUE", "NUO", "NURO", "NUS", "NUV", "NUVA",
           "NUVB", "NUW", "NUZE", "NVAX", "NVCN", "NVCR", "NVDA", "NVEC", "NVEE", "NVFY", "NVG", "NVGS", "NVIV", "NVMI",
           "NVMZ", "NVO", "NVR", "NVRO", "NVS", "NVSAU", "NVST", "NVT", "NVTA", "NWBI", "NWE", "NWFL", "NWG", "NWHM",
           "NWL", "NWLI", "NWN", "NWPX", "NWS", "NWSA", "NX", "NXC", "NXE", "NXGN", "NXJ", "NXN", "NXP", "NXPI", "NXQ",
           "NXR", "NXRT", "NXST", "NXTC", "NXTD", "NYC", "NYCB", "NYCB^A", "NYCB^U", "NYMT", "NYMTM", "NYMTN", "NYMTO",
           "NYMTP", "NYMX", "NYT", "NYV", "NZF", "O", "OACB", "OAK^A", "OAK^B", "OAS", "OBAS", "OBCI", "OBLG", "OBLN",
           "OBNK", "OBSV", "OC", "OCA", "OCAXU", "OCC", "OCCI", "OCCIP", "OCDX", "OCFC", "OCFCP", "OCFT", "OCG", "OCGN",
           "OCN", "OCSI", "OCSL", "OCTZ", "OCUL", "OCUP", "OCX", "ODC", "ODFL", "ODP", "ODT", "OEC", "OEG", "OEPWU",
           "OESX", "OFC", "OFED", "OFG", "OFG^A", "OFG^B", "OFG^D", "OFIX", "OFLX", "OFS", "OFSSG", "OFSSI", "OFSSL",
           "OFSSZ", "OGE", "OGEN", "OGI", "OGS", "OHI", "OI", "OIA", "OII", "OIIM", "OIS", "OKE", "OKTA", "OLB", "OLED",
           "OLLI", "OLMA", "OLN", "OLP", "OM", "OMAB", "OMC", "OMCL", "OMEG", "OMER", "OMEX", "OMF", "OMI", "OMP", "ON",
           "ONB", "ONCR", "ONCS", "ONCT", "ONCY", "ONDS", "ONE", "ONEM", "ONEW", "ONTF", "ONTO", "ONTX", "ONTXW",
           "ONVO", "OOMA", "OPBK", "OPCH", "OPEN", "OPENW", "OPGN", "OPHC", "OPI", "OPINI", "OPINL", "OPK", "OPNT",
           "OPOF", "OPP", "OPP^A", "OPRA", "OPRT", "OPRX", "OPT", "OPTN", "OPTT", "OPY", "OR", "ORA", "ORAN", "ORBC",
           "ORC", "ORCC", "ORCL", "ORGO", "ORGS", "ORI", "ORIC", "ORLA", "ORLY", "ORMP", "ORN", "ORPH", "ORRF", "ORTX",
           "OSBC", "OSG", "OSH", "OSIS", "OSK", "OSMT", "OSN", "OSPN", "OSS", "OSTK", "OSTRU", "OSUR", "OSW", "OTEL",
           "OTEX", "OTIC", "OTIS", "OTLK", "OTLKW", "OTRA", "OTRAU", "OTRAW", "OTRK", "OTRKP", "OTTR", "OUT", "OVBC",
           "OVID", "OVLY", "OVV", "OXBR", "OXBRW", "OXFD", "OXLC", "OXLCM", "OXLCO", "OXLCP", "OXM", "OXSQ", "OXSQL",
           "OXSQZ", "OXY", "OYST", "OZK", "OZON", "PAA", "PAAS", "PAC", "PACB", "PACE", "PACK", "PACW", "PACXU", "PAE",
           "PAEWW", "PAG", "PAGP", "PAGS", "PAHC", "PAI", "PAIC", "PAICU", "PAICW", "PAM", "PAND", "PANL", "PANW",
           "PAQCU", "PAR", "PARR", "PASG", "PATI", "PATK", "PAVM", "PAVMW", "PAVMZ", "PAX", "PAYA", "PAYAW", "PAYC",
           "PAYS", "PAYX", "PB", "PBA", "PBC", "PBCT", "PBCTP", "PBF", "PBFS", "PBFX", "PBH", "PBHC", "PBI", "PBI^B",
           "PBIP", "PBLA", "PBPB", "PBR", "PBT", "PBTS", "PBY", "PBYI", "PCAR", "PCB", "PCF", "PCG", "PCG^A", "PCG^B",
           "PCG^C", "PCG^D", "PCG^G", "PCGU", "PCH", "PCI", "PCK", "PCM", "PCN", "PCOM", "PCPC", "PCQ", "PCRX", "PCSA",
           "PCSB", "PCTI", "PCTY", "PCVX", "PCYG", "PCYO", "PD", "PDAC", "PDCE", "PDCO", "PDD", "PDEX", "PDFS", "PDI",
           "PDLB", "PDM", "PDO", "PDS", "PDSB", "PDT", "PEAK", "PEB", "PEB^C", "PEB^D", "PEB^E", "PEB^F", "PEBK",
           "PEBO", "PED", "PEG", "PEGA", "PEI", "PEI^B", "PEI^C", "PEI^D", "PEN", "PENN", "PEO", "PEP", "PERI", "PESI",
           "PETQ", "PETS", "PETZ", "PFBC", "PFBI", "PFC", "PFD", "PFDRU", "PFE", "PFG", "PFGC", "PFH", "PFHD", "PFIE",
           "PFIN", "PFIS", "PFL", "PFLT", "PFMT", "PFN", "PFO", "PFPT", "PFS", "PFSI", "PFSW", "PFX", "PFXNL", "PG",
           "PGC", "PGEN", "PGNY", "PGP", "PGR", "PGRE", "PGRWU", "PGTI", "PGZ", "PH", "PHAR", "PHAS", "PHAT", "PHCF",
           "PHD", "PHG", "PHGE", "PHI", "PHIC", "PHICU", "PHICW", "PHIO", "PHIOW", "PHK", "PHM", "PHR", "PHT", "PHUN",
           "PHUNW", "PHVS", "PHX", "PI", "PIAI", "PICO", "PII", "PIM", "PINC", "PINE", "PING", "PINS", "PIPP", "PIPR",
           "PIRS", "PIXY", "PJT", "PK", "PKBK", "PKE", "PKG", "PKI", "PKO", "PKOH", "PKX", "PLAB", "PLAG", "PLAN",
           "PLAY", "PLBC", "PLBY", "PLCE", "PLD", "PLG", "PLIN", "PLL", "PLM", "PLMR", "PLNT", "PLOW", "PLPC", "PLRX",
           "PLSE", "PLT", "PLTK", "PLTR", "PLUG", "PLUS", "PLX", "PLXP", "PLXS", "PLYA", "PLYM", "PLYM^A", "PM", "PMBC",
           "PMD", "PME", "PMF", "PMGMU", "PML", "PMM", "PMO", "PMT", "PMT^A", "PMT^B", "PMVC", "PMVP", "PMX", "PNBK",
           "PNC", "PNC^P", "PNF", "PNFP", "PNFPP", "PNI", "PNM", "PNNT", "PNNTG", "PNR", "PNRG", "PNTG", "PNW", "POAI",
           "PODD", "POLA", "POOL", "POR", "POSH", "POST", "POWI", "POWL", "POWRU", "POWW", "PPBI", "PPBT", "PPC", "PPD",
           "PPG", "PPGHU", "PPIH", "PPL", "PPR", "PPSI", "PPT", "PPTA", "PPX", "PQG", "PRA", "PRAA", "PRAH", "PRAX",
           "PRCH", "PRCHW", "PRDO", "PRE^G", "PRE^H", "PRE^I", "PRFT", "PRFX", "PRG", "PRGO", "PRGS", "PRGX", "PRI",
           "PRIF^A", "PRIF^B", "PRIF^C", "PRIF^E", "PRIF^F", "PRIM", "PRK", "PRLB", "PRLD", "PRMW", "PRO", "PROF",
           "PROG", "PROS", "PROV", "PRPB", "PRPH", "PRPL", "PRPO", "PRQR", "PRS", "PRSP", "PRSRU", "PRT", "PRTA",
           "PRTC", "PRTH", "PRTK", "PRTS", "PRTY", "PRU", "PRVB", "PS", "PSA", "PSA^C", "PSA^D", "PSA^E", "PSA^F",
           "PSA^G", "PSA^H", "PSA^I", "PSA^J", "PSA^K", "PSA^L", "PSA^M", "PSA^N", "PSA^O", "PSAC", "PSACU", "PSACW",
           "PSB", "PSB^W", "PSB^X", "PSB^Y", "PSB^Z", "PSCX", "PSEC", "PSF", "PSFD", "PSFF", "PSHG", "PSMD", "PSMT",
           "PSN", "PSNL", "PSO", "PSTG", "PSTH", "PSTI", "PSTL", "PSTV", "PSTX", "PSX", "PSXP", "PT", "PTA", "PTC",
           "PTCT", "PTE", "PTEN", "PTGX", "PTIC", "PTICU", "PTICW", "PTK", "PTMN", "PTN", "PTNR", "PTON", "PTPI", "PTR",
           "PTRS", "PTSI", "PTVCA", "PTVCB", "PTVE", "PTY", "PUBM", "PUCKU", "PUK", "PUK^", "PUK^A", "PULM", "PUMP",
           "PUYI", "PVAC", "PVBC", "PVG", "PVH", "PVL", "PW", "PW^A", "PWFL", "PWOD", "PWR", "PXD", "PXLW", "PXS",
           "PXSAP", "PXSAW", "PYN", "PYPD", "PYPL", "PYS", "PYT", "PZC", "PZG", "PZN", "PZZA", "QADA", "QADB", "QCOM",
           "QCON", "QCRH", "QD", "QDEC", "QDEL", "QELL", "QELLU", "QELLW", "QEP", "QFIN", "QGEN", "QH", "QIWI", "QK",
           "QLGN", "QLI", "QLYS", "QMCO", "QNST", "QPFF", "QQQX", "QRHC", "QRTEA", "QRTEB", "QRTEP", "QRVO", "QS",
           "QSR", "QTNT", "QTRX", "QTS", "QTS^A", "QTS^B", "QTT", "QTWO", "QUAD", "QUIK", "QUMU", "QUOT", "QURE",
           "QVCC", "QVCD", "R", "RA", "RAAC", "RAACU", "RAACW", "RAAS", "RACA", "RACE", "RAD", "RADA", "RADI", "RAIL",
           "RAMP", "RAND", "RAPT", "RARE", "RAVE", "RAVN", "RBA", "RBAC", "RBB", "RBBN", "RBC", "RBCAA", "RBCN", "RBKB",
           "RBNC", "RC", "RCA", "RCB", "RCC", "RCEL", "RCG", "RCHG", "RCHGU", "RCHGW", "RCI", "RCII", "RCKT", "RCKY",
           "RCL", "RCLFU", "RCM", "RCMT", "RCON", "RCP", "RCS", "RCUS", "RDCM", "RDFI", "RDFN", "RDHL", "RDI", "RDIB",
           "RDN", "RDNT", "RDS/B", "RDUS", "RDVT", "RDWR", "RDY", "RE", "REAL", "REC", "REDU", "REED", "REFR", "REG",
           "REGI", "REGN", "REI", "REKR", "RELI", "RELIW", "RELL", "RELX", "RENN", "REPH", "REPL", "RES", "RESN",
           "RETA", "RETO", "REV", "REVG", "REX", "REXR", "REXR^A", "REXR^B", "REXR^C", "REYN", "REZI", "RF", "RF^A",
           "RF^B", "RF^C", "RFI", "RFIL", "RFL", "RFM", "RFP", "RGA", "RGCO", "RGEN", "RGLD", "RGLS", "RGNX", "RGP",
           "RGR", "RGS", "RGT", "RH", "RHE", "RHE^A", "RHI", "RHP", "RIBT", "RICE", "RICK", "RIDE", "RIG", "RIGL",
           "RILY", "RILYG", "RILYH", "RILYI", "RILYL", "RILYM", "RILYN", "RILYO", "RILYP", "RILYT", "RILYZ", "RIO",
           "RIOT", "RIV", "RIVE", "RJF", "RKDA", "RKT", "RL", "RLAY", "RLGT", "RLGY", "RLH", "RLI", "RLJ", "RLJ^A",
           "RLMD", "RLX", "RM", "RMAX", "RMBI", "RMBL", "RMBS", "RMCF", "RMD", "RMED", "RMGB", "RMGBU", "RMGBW",
           "RMGCU", "RMI", "RMM", "RMNI", "RMO", "RMPL^", "RMR", "RMRM", "RMT", "RMTI", "RNA", "RNDB", "RNET", "RNG",
           "RNGR", "RNLX", "RNP", "RNR", "RNR^E", "RNR^F", "RNST", "RNWK", "ROAD", "ROCC", "ROCCU", "ROCCW", "ROCH",
           "ROCHU", "ROCHW", "ROCK", "ROG", "ROIC", "ROK", "ROKU", "ROL", "ROLL", "ROMO", "ROOT", "ROP", "ROST", "RP",
           "RPAI", "RPAY", "RPD", "RPLA", "RPM", "RPRX", "RPT", "RPT^D", "RPTX", "RQI", "RRBI", "RRC", "RRD", "RRGB",
           "RRR", "RS", "RSF", "RSG", "RSI", "RSSS", "RSVA", "RSVAU", "RSVAW", "RTAI", "RTLR", "RTP", "RTPZ", "RTX",
           "RUBY", "RUHN", "RUN", "RUSHA", "RUSHB", "RUTH", "RVI", "RVLV", "RVMD", "RVNC", "RVP", "RVPH", "RVPHW",
           "RVSB", "RVT", "RWLK", "RWT", "RXN", "RXT", "RY", "RY^T", "RYAAY", "RYAM", "RYB", "RYI", "RYN", "RYTM",
           "RZA", "RZB", "RZLT", "SA", "SABR", "SABRP", "SACC", "SACH", "SAF", "SAFE", "SAFM", "SAFT", "SAGE", "SAH",
           "SAIA", "SAIC", "SAII", "SAIIU", "SAIIW", "SAIL", "SAK", "SAL", "SALM", "SAM", "SAMG", "SAN", "SANA", "SAND",
           "SANM", "SANW", "SAP", "SAR", "SASR", "SATS", "SAVA", "SAVE", "SB", "SB^C", "SB^D", "SBAC", "SBBA", "SBBP",
           "SBCF", "SBE", "SBFG", "SBG", "SBGI", "SBH", "SBI", "SBLK", "SBLKZ", "SBNY", "SBNYP", "SBOW", "SBR", "SBRA",
           "SBS", "SBSI", "SBSW", "SBT", "SBTX", "SBUX", "SC", "SCCB", "SCCC", "SCCO", "SCD", "SCE^G", "SCE^H", "SCE^J",
           "SCE^K", "SCE^L", "SCHL", "SCHN", "SCHW", "SCHW^C", "SCHW^D", "SCI", "SCKT", "SCL", "SCLEU", "SCM", "SCOA",
           "SCOAU", "SCOAW", "SCOBU", "SCOR", "SCPE", "SCPH", "SCPL", "SCPS", "SCS", "SCSC", "SCU", "SCVL", "SCVX",
           "SCWX", "SCX", "SCYX", "SD", "SDACU", "SDC", "SDGR", "SDH", "SDHY", "SDPI", "SE", "SEAC", "SEAH", "SEAS",
           "SEB", "SECO", "SEDG", "SEE", "SEED", "SEEL", "SEER", "SEIC", "SELB", "SELF", "SEM", "SENEA", "SENEB",
           "SENS", "SEPZ", "SESN", "SF", "SF^A", "SF^B", "SF^C", "SFB", "SFBC", "SFBS", "SFE", "SFET", "SFIX", "SFL",
           "SFM", "SFNC", "SFST", "SFT", "SFTW", "SFUN", "SG", "SGA", "SGAM", "SGAMU", "SGAMW", "SGBX", "SGC", "SGEN",
           "SGFY", "SGH", "SGLB", "SGLBW", "SGMA", "SGMO", "SGMS", "SGOC", "SGRP", "SGRY", "SGTX", "SGU", "SHACU",
           "SHAK", "SHBI", "SHC", "SHEN", "SHG", "SHI", "SHIP", "SHIPW", "SHIPZ", "SHLS", "SHLX", "SHO", "SHO^E",
           "SHO^F", "SHOO", "SHOP", "SHSP", "SHW", "SHYF", "SI", "SIBN", "SIC", "SID", "SIEB", "SIEN", "SIF", "SIFY",
           "SIG", "SIGA", "SIGI", "SIGIP", "SII", "SILC", "SILK", "SILV", "SIM", "SIMO", "SINA", "SINO", "SINT", "SIOX",
           "SIRI", "SITC", "SITC^A", "SITC^K", "SITE", "SITM", "SIVB", "SIVBP", "SIX", "SJ", "SJI", "SJIJ", "SJIU",
           "SJM", "SJR", "SJT", "SJW", "SKLZ", "SKM", "SKT", "SKX", "SKY", "SKYW", "SLAB", "SLB", "SLCA", "SLCRU",
           "SLCT", "SLDB", "SLF", "SLG", "SLG^I", "SLGG", "SLGL", "SLGN", "SLM", "SLMBP", "SLN", "SLNO", "SLP", "SLQT",
           "SLRC", "SLRX", "SLS", "SM", "SMAR", "SMBC", "SMBK", "SMCI", "SMED", "SMFG", "SMG", "SMHI", "SMID", "SMIT",
           "SMLP", "SMM", "SMMF", "SMMT", "SMP", "SMPL", "SMSI", "SMTC", "SMTI", "SMTS", "SMTX", "SNA", "SNAP", "SNBR",
           "SNCA", "SNCR", "SND", "SNDE", "SNDL", "SNDR", "SNDX", "SNE", "SNES", "SNEX", "SNFCA", "SNGX", "SNGXW",
           "SNMP", "SNN", "SNOA", "SNOW", "SNP", "SNPR", "SNPS", "SNR", "SNRH", "SNRHU", "SNRHW", "SNSE", "SNSS", "SNV",
           "SNV^D", "SNV^E", "SNX", "SNY", "SO", "SOAC", "SOGO", "SOHO", "SOHOB", "SOHON", "SOHOO", "SOHU", "SOI",
           "SOJB", "SOJC", "SOJD", "SOJE", "SOL", "SOLN", "SOLO", "SOLOW", "SOLY", "SON", "SONA", "SONM", "SONN",
           "SONO", "SOR", "SOS", "SP", "SPB", "SPCB", "SPCE", "SPE", "SPE^B", "SPFI", "SPFR", "SPG", "SPG^J", "SPGI",
           "SPH", "SPI", "SPKE", "SPKEP", "SPLK", "SPLP", "SPLP^A", "SPNE", "SPNS", "SPNV", "SPOK", "SPOT", "SPPI",
           "SPR", "SPRB", "SPRO", "SPRQ", "SPRT", "SPSC", "SPT", "SPTKU", "SPTN", "SPWH", "SPWR", "SPXC", "SPXX", "SQ",
           "SQBG", "SQFT", "SQM", "SQNS", "SQZ", "SR", "SR^A", "SRAC", "SRACU", "SRACW", "SRAX", "SRC", "SRC^A", "SRCE",
           "SRCL", "SRDX", "SRE", "SRE^B", "SREA", "SREV", "SRG", "SRG^A", "SRGA", "SRI", "SRL", "SRLP", "SRNE", "SRPT",
           "SRRA", "SRRK", "SRSA", "SRSAU", "SRSAW", "SRT", "SRTS", "SRV", "SSAAU", "SSB", "SSBI", "SSD", "SSKN", "SSL",
           "SSNC", "SSNT", "SSP", "SSPK", "SSPKU", "SSPKW", "SSRM", "SSSS", "SSTI", "SSTK", "SSY", "SSYS", "ST", "STAA",
           "STAF", "STAG", "STAG^C", "STAR", "STAR^D", "STAR^G", "STAR^I", "STAY", "STBA", "STC", "STCN", "STE", "STEP",
           "STFC", "STG", "STIC", "STIM", "STK", "STKL", "STKS", "STL", "STL^A", "STLA", "STLD", "STM", "STMP", "STN",
           "STND", "STNE", "STNG", "STOK", "STON", "STOR", "STPK", "STRA", "STRL", "STRM", "STRO", "STRR", "STRRP",
           "STRS", "STRT", "STSA", "STT", "STT^D", "STT^G", "STTK", "STWD", "STWO", "STWOU", "STWOW", "STX", "STXB",
           "STXS", "STZ", "STZ/B", "SU", "SUI", "SULR", "SUM", "SUMO", "SUMR", "SUN", "SUNS", "SUNW", "SUP", "SUPN",
           "SUPV", "SURF", "SUZ", "SV", "SVAC", "SVACU", "SVACW", "SVAL", "SVBI", "SVC", "SVFA", "SVFAU", "SVFAW",
           "SVM", "SVMK", "SVOK", "SVOKU", "SVOKW", "SVRA", "SVSVU", "SVSVW", "SVT", "SVVC", "SWAV", "SWBI", "SWCH",
           "SWETU", "SWI", "SWIR", "SWK", "SWKH", "SWKS", "SWM", "SWN", "SWT", "SWTX", "SWX", "SWZ", "SXC", "SXI",
           "SXT", "SXTC", "SY", "SYBT", "SYBX", "SYF", "SYF^A", "SYK", "SYKE", "SYN", "SYNA", "SYNC", "SYNH", "SYNL",
           "SYPR", "SYRS", "SYTA", "SYTAW", "SYX", "SYY", "SZC", "T", "T^A", "T^C", "TA", "TAC", "TACA", "TACO", "TACT",
           "TAEQ", "TAIT", "TAK", "TAL", "TALO", "TANH", "TANNI", "TANNL", "TANNZ", "TAOP", "TAP", "TARA", "TARO",
           "TARS", "TAST", "TATT", "TAYD", "TBA", "TBB", "TBBK", "TBC", "TBCPU", "TBI", "TBIO", "TBJL", "TBK", "TBKCP",
           "TBLT", "TBLTW", "TBNK", "TBPH", "TC", "TCACU", "TCBI", "TCBIL", "TCBIP", "TCBK", "TCDA", "TCF", "TCFC",
           "TCFCP", "TCI", "TCMD", "TCOM", "TCON", "TCP", "TCPC", "TCRR", "TCS", "TCX", "TD", "TDA", "TDAC", "TDACU",
           "TDACW", "TDC", "TDE", "TDF", "TDG", "TDI", "TDJ", "TDOC", "TDS", "TDW", "TDY", "TEAF", "TEAM", "TECH",
           "TECK", "TECTP", "TEDU", "TEF", "TEGS", "TEI", "TEKK", "TEKKU", "TEKKW", "TEL", "TELA", "TELL", "TEN",
           "TENB", "TENX", "TEO", "TER", "TERN", "TESS", "TEVA", "TEX", "TFC", "TFC^F", "TFC^G", "TFC^H", "TFC^I",
           "TFC^O", "TFC^R", "TFFP", "TFII", "TFJL", "TFSA", "TFSL", "TFX", "TG", "TGA", "TGB", "TGC", "TGH", "TGI",
           "TGLS", "TGNA", "TGP", "TGP^A", "TGP^B", "TGS", "TGT", "TGTX", "TH", "THBR", "THBRU", "THBRW", "THC", "THCA",
           "THCAU", "THCAW", "THCB", "THCBU", "THCBW", "THFF", "THG", "THM", "THMAU", "THMO", "THO", "THQ", "THR",
           "THRM", "THRY", "THS", "THTX", "THW", "THWWW", "THY", "TIG", "TIGO", "TIGR", "TILE", "TIMB", "TINV", "TIPT",
           "TIRX", "TISI", "TITN", "TIXT", "TJX", "TK", "TKAT", "TKC", "TKR", "TLC", "TLGT", "TLIS", "TLK", "TLMD",
           "TLMDW", "TLND", "TLRY", "TLS", "TLSA", "TLYS", "TM", "TMAT", "TMBR", "TMDI", "TMDX", "TME", "TMHC", "TMKRU",
           "TMO", "TMP", "TMPM", "TMPMU", "TMPMW", "TMQ", "TMST", "TMTS", "TMTSU", "TMTSW", "TMUS", "TMX", "TNC",
           "TNDM", "TNET", "TNK", "TNL", "TNP", "TNP^D", "TNP^E", "TNP^F", "TNXP", "TOL", "TOMZ", "TOPS", "TOT", "TOUR",
           "TOWN", "TPB", "TPC", "TPCO", "TPGY", "TPH", "TPHS", "TPIC", "TPL", "TPR", "TPRE", "TPTX", "TPVG", "TPVY",
           "TPX", "TPZ", "TR", "TRC", "TRCH", "TREB", "TREC", "TREE", "TREX", "TRGP", "TRHC", "TRI", "TRIB", "TRIL",
           "TRIN", "TRIP", "TRIT", "TRITW", "TRMB", "TRMD", "TRMK", "TRMT", "TRN", "TRNO", "TRNS", "TROW", "TROX",
           "TRP", "TRQ", "TRS", "TRST", "TRT", "TRTN", "TRTN^A", "TRTN^B", "TRTN^C", "TRTN^D", "TRTX", "TRU", "TRUE",
           "TRUP", "TRV", "TRVG", "TRVI", "TRVN", "TRX", "TRXC", "TS", "TSBK", "TSC", "TSCAP", "TSCBP", "TSCO", "TSE",
           "TSEM", "TSHA", "TSI", "TSIA", "TSIAU", "TSIAW", "TSIBU", "TSLA", "TSLX", "TSM", "TSN", "TSOC", "TSQ",
           "TSRI", "TT", "TTC", "TTCF", "TTD", "TTEC", "TTEK", "TTGT", "TTI", "TTM", "TTMI", "TTNP", "TTOO", "TTP",
           "TTWO", "TU", "TUFN", "TUP", "TURN", "TUSK", "TV", "TVAC", "TVACU", "TVACW", "TVC", "TVE", "TVTX", "TVTY",
           "TW", "TWCT", "TWCTU", "TWCTW", "TWI", "TWIN", "TWLO", "TWN", "TWND", "TWNK", "TWNKW", "TWO", "TWO^A",
           "TWO^B", "TWO^C", "TWO^D", "TWO^E", "TWOU", "TWST", "TWTR", "TX", "TXG", "TXMD", "TXN", "TXRH", "TXT", "TY",
           "TY^", "TYG", "TYHT", "TYL", "TYME", "TZOO", "TZPSU", "U", "UA", "UAA", "UAL", "UAMY", "UAN", "UAVS", "UBA",
           "UBCP", "UBER", "UBFO", "UBOH", "UBP", "UBP^H", "UBP^K", "UBS", "UBSI", "UBX", "UCBI", "UCBIO", "UCL",
           "UCTT", "UDR", "UE", "UEC", "UEIC", "UEPS", "UFAB", "UFCS", "UFI", "UFPI", "UFPT", "UFS", "UG", "UGI", "UGP",
           "UGRO", "UHAL", "UHS", "UHT", "UI", "UIHC", "UIS", "UK", "UKOMW", "UL", "ULBI", "ULH", "ULTA", "UMBF", "UMC",
           "UMH", "UMH^C", "UMH^D", "UMPQ", "UNAM", "UNB", "UNF", "UNFI", "UNH", "UNIT", "UNM", "UNMA", "UNP", "UNTY",
           "UNVR", "UONE", "UONEK", "UPLD", "UPS", "UPST", "UPWK", "URBN", "URG", "URGN", "URI", "UROV", "USA", "USAC",
           "USAK", "USAP", "USAS", "USAT", "USAU", "USB", "USB^A", "USB^H", "USB^M", "USB^P", "USB^Q", "USB^R", "USCR",
           "USDP", "USEG", "USFD", "USIO", "USLM", "USM", "USNA", "USPH", "USWS", "USWSW", "USX", "UTF", "UTG", "UTHR",
           "UTI", "UTL", "UTMD", "UTSI", "UTZ", "UUU", "UUUU", "UVE", "UVSP", "UVV", "UWMC", "UXIN", "UZA", "UZB",
           "UZC", "UZD", "UZE", "V", "VAC", "VACQ", "VACQU", "VACQW", "VALE", "VALU", "VAPO", "VAR", "VBF", "VBFC",
           "VBIV", "VBLT", "VBTX", "VC", "VCEL", "VCF", "VCIF", "VCKAU", "VCNX", "VCRA", "VCTR", "VCV", "VCVC", "VCVCU",
           "VCVCW", "VCYT", "VEC", "VECO", "VEDL", "VEEV", "VEL", "VENAU", "VEON", "VER", "VER^F", "VERB", "VERBW",
           "VERI", "VERO", "VERU", "VERX", "VERY", "VET", "VFC", "VFF", "VFL", "VG", "VGAC", "VGI", "VGM", "VGR", "VGZ",
           "VHAQ", "VHC", "VHI", "VIAC", "VIACA", "VIAO", "VIAV", "VICI", "VICR", "VIE", "VIH", "VIHAU", "VIHAW", "VII",
           "VIIAU", "VIIAW", "VINC", "VINCU", "VINCW", "VINO", "VINP", "VIOT", "VIPS", "VIR", "VIRC", "VIRI", "VIRS",
           "VIRT", "VISL", "VIST", "VITL", "VIV", "VIVE", "VIVO", "VJET", "VKI", "VKQ", "VKTX", "VKTXW", "VLDR",
           "VLDRW", "VLGEA", "VLO", "VLON", "VLRS", "VLT", "VLY", "VLYPO", "VLYPP", "VMAC", "VMACU", "VMACW", "VMAR",
           "VMC", "VMD", "VMI", "VMM", "VMO", "VMW", "VNCE", "VNDA", "VNE", "VNET", "VNO", "VNO^K", "VNO^L", "VNO^M",
           "VNO^N", "VNOM", "VNRX", "VNT", "VNTR", "VOC", "VOD", "VOLT", "VOR", "VOSOU", "VOXX", "VOYA", "VOYA^B",
           "VPG", "VPV", "VRA", "VRAY", "VRCA", "VRDN", "VREX", "VRM", "VRME", "VRMEW", "VRNA", "VRNS", "VRNT", "VRPX",
           "VRRM", "VRS", "VRSK", "VRSN", "VRT", "VRTS", "VRTV", "VRTX", "VS", "VSAT", "VSEC", "VSH", "VSPR", "VSPRU",
           "VSPRW", "VSSYW", "VST", "VSTA", "VSTM", "VSTO", "VTA", "VTAQ", "VTAQR", "VTAQU", "VTAQW", "VTGN", "VTIQU",
           "VTN", "VTNR", "VTOL", "VTR", "VTRS", "VTRU", "VTSI", "VTVT", "VUZI", "VVI", "VVNT", "VVOS", "VVPR", "VVR",
           "VVV", "VXRT", "VYGG", "VYGR", "VYNE", "VZ", "W", "WAB", "WABC", "WAFD", "WAFDP", "WAFU", "WAL", "WALA",
           "WASH", "WAT", "WATT", "WB", "WBA", "WBAI", "WBK", "WBS", "WBS^F", "WBT", "WCC", "WCC^A", "WCN", "WD",
           "WDAY", "WDC", "WDFC", "WDR", "WEA", "WEC", "WEI", "WELL", "WEN", "WERN", "WES", "WETF", "WEX", "WEYS", "WF",
           "WFC", "WFC^A", "WFC^C", "WFC^L", "WFC^N", "WFC^O", "WFC^P", "WFC^Q", "WFC^R", "WFC^W", "WFC^X", "WFC^Y",
           "WFC^Z", "WFG", "WGO", "WH", "WHD", "WHF", "WHFBZ", "WHG", "WHLM", "WHLR", "WHLRD", "WHLRP", "WHR", "WIA",
           "WIFI", "WILC", "WIMI", "WINA", "WING", "WINT", "WIRE", "WISA", "WISH", "WIT", "WIW", "WIX", "WK", "WKEY",
           "WKHS", "WLDN", "WLFC", "WLK", "WLKP", "WLL", "WLTW", "WM", "WMB", "WMC", "WMG", "WMK", "WMS", "WMT", "WNC",
           "WNEB", "WNS", "WNW", "WOOF", "WOR", "WORK", "WORX", "WOW", "WPC", "WPF", "WPG", "WPG^H", "WPG^I", "WPM",
           "WPP", "WPRT", "WRAP", "WRB", "WRB^C", "WRB^D", "WRB^E", "WRB^F", "WRB^G", "WRB^H", "WRE", "WRI", "WRK",
           "WRLD", "WRN", "WSBC", "WSBCP", "WSBF", "WSC", "WSFS", "WSM", "WSO", "WSO/B", "WSR", "WST", "WSTG", "WTBA",
           "WTER", "WTFC", "WTFCM", "WTFCP", "WTI", "WTM", "WTRE", "WTREP", "WTRG", "WTRH", "WTRU", "WTS", "WTT",
           "WTTR", "WU", "WUGI", "WVE", "WVFC", "WVVI", "WVVIP", "WW", "WWD", "WWE", "WWR", "WWW", "WY", "WYNN", "WYY",
           "X", "XAIR", "XBIO", "XBIOW", "XBIT", "XCUR", "XDAT", "XEC", "XEL", "XELA", "XELB", "XENE", "XENT", "XERS",
           "XFLT", "XFOR", "XGN", "XHR", "XIN", "XJH", "XJR", "XL", "XLNX", "XLRN", "XM", "XNCR", "XNET", "XOG", "XOM",
           "XOMA", "XOMAP", "XONE", "XP", "XPDIU", "XPEL", "XPER", "XPEV", "XPL", "XPO", "XPOA", "XRAY", "XRX", "XSPA",
           "XTLB", "XTNT", "XVV", "XXII", "XYF", "XYL", "Y", "YAC", "YALA", "YCBD", "YCBD^A", "YDEC", "YELL", "YELP",
           "YETI", "YEXT", "YGMZ", "YI", "YJ", "YMAB", "YMTX", "YNDX", "YORW", "YPF", "YQ", "YRD", "YSAC", "YSACU",
           "YSACW", "YSG", "YTEN", "YTRA", "YUM", "YUMC", "YVR", "YY", "Z", "ZAGG", "ZBH", "ZBRA", "ZCMD", "ZDGE",
           "ZEAL", "ZEN", "ZEUS", "ZG", "ZGNX", "ZGYH", "ZGYHR", "ZGYHU", "ZGYHW", "ZI", "ZIM", "ZION", "ZIONL",
           "ZIONN", "ZIONO", "ZIONP", "ZIOP", "ZIXI", "ZKIN", "ZLAB", "ZM", "ZNGA", "ZNH", "ZNTE", "ZNTEU", "ZNTEW",
           "ZNTL", "ZOM", "ZS", "ZSAN", "ZTO", "ZTR", "ZTS", "ZUMZ", "ZUO", "ZVO", "ZWRKU", "ZYME", "ZYNE", "ZYXI"]

companies = """
Agilent Technologies Inc. Common Stock
Alcoa Corporation Common Stock 
ATA Creativity Global American Depositary Shares
Artius Acquisition Inc. Class A Common Stock
Artius Acquisition Inc. Unit 
Artius Acquisition Inc Warrant
Arlington Asset Investment Corp Class A (new)
Arlington Asset Investment Corp 7.00% 
Arlington Asset Investment Corp 8.250% Seies C Fixed-to-Floating Rate Cumulative Redeemable Preferred Stock   
American Airlines Group Inc. Common Stock
Altisource Asset Management Corp Com
Atlantic American Corporation Common Stock
Aarons Holdings Company Inc. Common Stock 
Applied Optoelectronics Inc. Common Stock
AAON Inc. Common Stock
Advance Auto Parts Inc Advance Auto Parts Inc W/I
Apple Inc. Common Stock
American Assets Trust Inc. Common Stock
Almaden Minerals Ltd. Common Shares
Atlas Air Worldwide Holdings NEW Common Stock
AllianceBernstein Holding L.P.  Units
ABB Ltd Common Stock
AbbVie Inc. Common Stock
AmerisourceBergen Corporation Common Stock
Ameris Bancorp Common Stock
AbCellera Biologics Inc. Common Shares
Abcam plc American Depositary Shares
Abeona Therapeutics Inc. Common Stock
Ambev S.A. American Depositary Shares (Each representing 1 Common Share)
Asbury Automotive Group Inc Common Stock
ABG Acquisition Corp. I Class A Ordinary Shares
ARCA biopharma Inc. Common Stock
ABM Industries Incorporated Common Stock
ABIOMED Inc. Common Stock
Airbnb Inc. Class A Common Stock
Arbor Realty Trust Common Stock
Arbor Realty Trust Preferred Series A
Arbor Realty Trust Cumulative Redeemable Preferred Series B
Arbor Realty Trust Cumulative Redeemable Preferred Series C
Absolute Software Corporation Common Stock
Abbott Laboratories Common Stock
Allegiance Bancshares Inc. Common Stock
Arbutus Biopharma Corporation Common Stock
Associated Capital Group Inc. Common Stock
Arcosa Inc. Common Stock 
Acies Acquisition Corp. Class A Ordinary Share
Acies Acquisition Corp. Unit
Acies Acquisition Corp. Warrant
ACADIA Pharmaceuticals Inc. Common Stock
Aurora Cannabis Inc. Common Shares
Atlantic Capital Bancshares Inc. Common Stock
American Campus Communities Inc Common Stock
Accolade Inc. Common Stock
Acco Brands Corporation Common Stock
Accel Entertainment Inc. 
Acer Therapeutics Inc. Common Stock (DE)
Adicet Bio Inc. Common Stock 
ACE Convergence Acquisition Corp. Class A Ordinary Shares
ACE Convergence Acquisition Corp. Unit
ACE Convergence Acquisition Corp. Warrant
Arch Capital Group Ltd. Common Stock
Arch Capital Group Ltd. Depositary Shares Each Representing 1/1000th Interest in a Share of 5.45% Non-Cumulative Preferred Shares Series F
Arch Capital Group Ltd. Depositary Shares Representing Interest in 5.25% Non-Cumulative Preferred Series E Shrs
Aluminum Corporation of China Limited American Depositary Shares
Acadia Healthcare Company Inc. Common Stock
Achieve Life Sciences Inc. Common Shares
Albertsons Companies Inc. Class A Common Stock
Acacia Communications Inc. Common Stock
Atlas Crest Investment Corp. Class A Common Stock
AC Immune SA Common Stock
ACI Worldwide Inc. Common Stock
Ackrell SPAC Partners I Co. Subunits
Ackrell SPAC Partners I Co. Units
Ackrell SPAC Partners I Co. Warrants
Axcelis Technologies Inc. Common Stock
AECOM Common Stock
ACM Research Inc. Class A Common Stock
Accenture plc Class A Ordinary Shares (Ireland)
ACNB Corporation Common Stock
Ascendant Digital Acquisition Corp. Class A Ordinary Shares
Acorda Therapeutics Inc. Common Stock
Aberdeen Income Credit Strategies Fund Common Shares
ACRES Commercial Realty Corp. Common Stock
ACRES Commercial Realty Corp. 8.625% Fixed-to-Floating Series C Cumulative Redeemable Preferred Stock 
Ares Commercial Real Estate Corporation Common Stock
Aclaris Therapeutics Inc. Common Stock
AcelRx Pharmaceuticals Inc. Common Stock
Acasti Pharma Inc. Class A Common Stock
ArcLight Clean Transition Corp. Class A Ordinary Shares
ArcLight Clean Transition Corp. Unit
ArcLight Clean Transition Corp. Warrant
Acacia Research Corporation (Acacia Tech) Common Stock
Acme United Corporation. Common Stock
Virtus AllianzGI Diversified Income & Convertible Fund Common Shares of Beneficial Interest
AeroCentury Corp. Common Stock
Adagene Inc. American Depositary Shares
Adaptimmune Therapeutics plc American Depositary Shares
Adobe Inc. Common Stock
Agree Realty Corporation Common Stock
ADC Therapeutics SA Common Shares
26 Capital Acquisition Corp. Unit
Advanced Emissions Solutions Inc. Common Stock
Anfield Dynamic Fixed Income ETF
Analog Devices Inc. Common Stock
Adial Pharmaceuticals Inc Common Stock
Adial Pharmaceuticals Inc Warrant
Archer-Daniels-Midland Company Common Stock
ADMA Biologics Inc Common Stock
Aptus Drawdown Managed Equity ETF
Adamis Pharmaceuticals Corporation Common Stock
Adamas Pharmaceuticals Inc. Common Stock
Advent Technologies Holdings Inc. Class A Common Stock
Adient plc Ordinary Shares 
Advent Technologies Holdings Inc. Warrant
Edoc Acquisition Corp. Class A Ordinary Share
Edoc Acquisition Corp. Right
Edoc Acquisition Corp. Warrant
Automatic Data Processing Inc. Common Stock
Adaptive Biotechnologies Corporation Common Stock
Alliance Data Systems Corporation Common Stock
Autodesk Inc. Common Stock
ADT Inc. Common Stock
ADTRAN Inc. Common Stock
ADiTx Therapeutics Inc. Common Stock
Addus HomeCare Corporation Common Stock
Advantage Solutions Inc. Class A Common Stock
Adverum Biotechnologies Inc. Common Stock
Advantage Solutions Inc. Warrant
Adams Diversified Equity Fund Inc.
Addex Therapeutics Ltd American Depositary Shares
Advaxis Inc. Common Stock
Adams Resources & Energy Inc. Common Stock
Authentic Equity Acquisition Corp. Unit
AEGON N.V. Perp. Cap. Secs. Floating Rate (Netherlands)
Ameren Corporation Common Stock
Aberdeen Emerging Markets Equity Income Fund Inc. Common Stock
Aegon Funding Company LLC 5.10% Subordinated Notes due 2049
AEGON N.V. Common Stock
Aegion Corp Common Stock
Antelope Enterprise Holdings Limited Common Stock (0.024 par)
Aehr Test Systems Common Stock
Alset EHome International Inc. Common Stock
Advanced Energy Industries Inc. Common Stock
American Equity Investment Life Holding Company Common Stock
American Equity Investment Life Holding Company Depositary Shares each representing a 1/1000th interest in a share of 5.95% Fixed-Rate Reset Non-Cumulative Preferred Stock Series A
American Equity Investment Life Holding Company Depositary Shares each representing a 1/1000th interest in a share of 6.625% Fixed-Rate Reset Non-Cumulative Preferred Stock Series B
Agnico Eagle Mines Limited Common Stock
Aethlon Medical Inc. Common Stock
Aenza S.A.A. American Depositary Shares
American Eagle Outfitters Inc. Common Stock
American Electric Power Company Inc. Common Stock
American Electric Power Company Inc. Corporate Unit
American Electric Power Company Inc. Corporate Units
AerCap Holdings N.V. Ordinary Shares
Aerie Pharmaceuticals Inc. Common Stock
The AES Corporation Common Stock
Allied Esports Entertainment Inc. Common Stock
Anfield U.S. Equity Sector Rotation ETF
ADDvantage Technologies Group Inc. Common Stock
AudioEye Inc. Common Stock
Aeterna Zentaris Inc. Common Stock
AllianceBernstein National Municipal Income Fund Inc
Affinity Bancshares Inc. Common Stock (MD)
Allied Capital Corporation Allied Capital Corporation 6.875% Notes due April 15 2047
American Financial Group Inc. Common Stock
American Financial Group Inc. 5.875% Subordinated Debentures due 2059
American Financial Group Inc. 5.125% Subordinated Debentures due 2059
American Financial Group Inc. 5.625% Subordinated Debentures due 2060
American Financial Group Inc. 4.500% Subordinated Debentures due 2060
Armstrong Flooring Inc. Common Stock
Acutus Medical Inc. Common Stock
American Finance Trust Inc. Class A Common Stock
American Finance Trust Inc. 7.375% Series C Cumulative Redeemable Preferred Stock
American Finance Trust Inc. 7.50% Series A Cumulative Redeemable Perpetual Preferred Stock
AFLAC Incorporated Common Stock
Affimed N.V.
Affirm Holdings Inc. Class A Common Stock
Apollo Senior Floating Rate Fund Inc. Common Stock
Afya Limited Class A Common Shares
First Majestic Silver Corp. Ordinary Shares (Canada)
AGBA Acquisition Limited Ordinary Share
AGBA Acquisition Limited Right
AGBA Acquisition Limited Warrant
Altimeter Growth Corp. Class A Ordinary Shares
Altimeter Growth Corp. 2 Class A Ordinary Shares
AGCO Corporation Common Stock
Altimeter Growth Corp. Unit
Altimeter Growth Corp. Warrant
Aberdeen Global Dynamic Dividend Fund
AgeX Therapeutics Inc. Common Stock
Agenus Inc. Common Stock
AgroFresh Solutions Inc. Common Stock
Agrify Corporation Common Stock
Alamos Gold Inc. Class A Common Shares
Agios Pharmaceuticals Inc. Common Stock
Aeglea BioTherapeutics Inc. Common Stock
Federal Agricultural Mortgage Corporation Common Stock
Federal Agricultural Mortgage Corporation Preferred Series C Fixed to Fltg
Federal Agricultural Mortgage Corporation 5.700% Non-Cumulative Preferred Stock Series D
Federal Agricultural Mortgage Corporation 5.750% Non-Cumulative Preferred Stock Series E
Federal Agricultural Mortgage Corporation 5.250% Non-Cumulative Preferred Stock Series F
AGM Group Holdings Inc. Class A Ordinary Shares
AGNC Investment Corp. Common Stock
AGNC Investment Corp. Depositary Shares rep 6.875% Series D Fixed-to-Floating Cumulative Redeemable Preferred Stock
AGNC Investment Corp. Depositary Shares Each Representing a 1/1000th Interest in a Share of 7.00% Series C Fixed-To-Floating Rate Cumulative Redeemable Preferred Stock
AGNC Investment Corp. Depositary Shares each representing a 1/1000th interest in a share of 6.50% Series E Fixed-to-Floating Cumulative Redeemable Preferred Stock
AGNC Investment Corp. Depositary Shares Each Representing a 1/1000th Interest in a Share of 6.125% Series F Fixed-to-Floating Rate Cumulative Redeemable Preferred Stock
Assured Guaranty Ltd. Common Stock
Assured Guaranty Ltd.
Assured Guaranty Ltd.
Assured Guaranty Ltd.
Avangrid Inc. Common Stock
Adecoagro S.A. Common Shares
Agile Therapeutics Inc. Common Stock
PlayAGS Inc. Common Stock
Applied Genetic Technologies Corporation Common Stock
Argan Inc. Common Stock
Agilysys Inc. Common Stock
Alpha Healthcare Acquisition Corp. Class A Common Stock
Alpha Healthcare Acquisition Corp. Unit
Alpha Healthcare Acquisition Corp. Warrant
A.H. Belo Corporation (TX) Common Stock
AdaptHealth Corp. Class A Common Stock
Armada Hoffler Properties Inc. Common Stock
Armada Hoffler Properties Inc. 6.75% Series A Cumulative Redeemable Perpetual Preferred Stock
Aspen Insurance Holdings Limited 5.95% Fixed-to-Floating Rate Perpetual Non-Cumulative Preference Shares
Aspen Insurance Holdings Limited 5.625% Perpetual Non-Cumulative Preference Shares
Aspen Insurance Holdings Limited Depositary Shares each representing a 1/1000th interest in a share of 5.625% Perpetual Non-Cumulative Preference Shares
Allied Healthcare Products Inc. Common Stock
Ashford Hospitality Trust Inc Common Stock
Ashford Hospitality Trust Inc 8.45% Series D Cumulative Preferred Stock
Ashford Hospitality Trust Inc 7.375% Series F Cumulative Preferred Stock
Ashford Hospitality Trust Inc 7.375% Series G Cumulative Preferred Stock
Ashford Hospitality Trust Inc 7.50% Series H Cumulative Preferred Stock
Ashford Hospitality Trust Inc 7.50% Series I Cumulative Preferred Stock
C3.ai Inc. Class A Common Stock
Arlington Asset Investment Corp 6.750% Notes due 2025
Apollo Tactical Income Fund Inc. Common Stock
American International Group Inc. New Common Stock
American International Group Inc. Depositary Shares Each Representing a 1/1000th Interest in a Share of Series A 5.85% Non-Cumulative Perpetual Preferred Stock
Aesthetic Medical International Holdings Group Ltd. American Depositary Shares
Senmiao Technology Limited Common Stock
AIkido Pharma Inc. Common Stock
AIM ImmunoTech Inc. Common Stock
Altra Industrial Motion Corp. Common Stock
Albany International Corporation Common Stock
Ashford Inc. (Holding Company) Common Stock
Apollo Investment Corporation Common Stock
Virtus AllianzGI Artificial Intelligence & Technology Opportunities Fund Common Shares
AAR Corp. Common Stock
Apartment Income REIT Corp. Common Stock
Airgain Inc. Common Stock
Air Industries Group Common Stock
Air T Inc. Common Stock
Air T Inc. Air T Funding Alpha Income Trust Preferred Securities
Air T Inc. Air T Funding Warrants to Purchase Alpha Income Trust Preferred Expiring 08/30/2021
Applied Industrial Technologies Inc. Common Stock
Apartment Investment and Management Company Common Stock
Arlington Asset Investment Corp 6.625% Notes due 2023
Assurant Inc. Common Stock
Assurant Inc. 5.25% Subordinated Notes due 2061
Assurant Inc. 6.50% Series D Mandatory Convertible Preferred Stock $1.00 par value
Ajax I Class A Ordinary Shares
Arthur J. Gallagher & Co. Common Stock
Aerojet Rocketdyne Holdings Inc. Common Stock
Great Ajax Corp. Common Stock
Great Ajax Corp. 7.25% Convertible Senior Notes due 2024
Akamai Technologies Inc. Common Stock
Akebia Therapeutics Inc. Common Stock
Akers Biosciences Inc. Common Stock
Sports Ventures Acquisition Corp. Unit
Embotelladora Andina S.A.
Embotelladora Andina S.A.
Acadia Realty Trust Common Stock
Akero Therapeutics Inc. Common Stock
Akoustis Technologies Inc. Common Stock
Akari Therapeutics plc ADR (0.01 USD)
Akumin Inc. Common Shares
Akouos Inc. Common Stock
Air Lease Corporation Class A Common Stock
Air Lease Corporation 6.150% Fixed-to-Floating Rate Non-Cumulative Perpetual Preferred Stock Series A
Alberton Acquisition Corporation Ordinary Shares
Alberton Acquisition Corporation Rights exp April 26 2021
Alberton Acquisition Corporation Warrant
Albemarle Corporation Common Stock
Albireo Pharma Inc. Common Stock
Alcon Inc. Ordinary Shares
Alico Inc. Common Stock
Aldeyra Therapeutics Inc. Common Stock
Allete Inc.
Alector Inc. Common Stock
Alexander & Baldwin Inc. Common Stock REIT Holding Company
Alamo Group Inc. Common Stock
Allegro MicroSystems Inc. Common Stock
Align Technology Inc. Common Stock
Aligos Therapeutics Inc. Common Stock
Allegiant Travel Company Common Stock
Alimera Sciences Inc. Common Stock
Altera Infrastructure L.P. 7.25% Series A 
Altera Infrastructure L.P. 8.50% Series B 
Altera Infrastructure L.P. 8.875% Series E 
ALJ Regional Holdings Inc. Common Stock
Alaska Air Group Inc. Common Stock
Alkermes plc Ordinary Shares
Allstate Corporation (The) Common Stock
Allstate Corporation (The) 5.100% Fixed-to-Floating Rate Subordinated Debentures due 2053
Allstate Corporation (The) Depositary Shares each representing a 1/1000th interest in a share of Fixed Rate Noncumulative Perpetual Preferred Stock Series G
Allstate Corporation (The) Depositary Shares each representing a 1/1000th interest in a share of Fixed Rate Noncumulative Perpetual Preferred Stock Series H
Allstate Corporation (The) Depositary Shares each representing a 1/1000th interest in a share of Fixed Rate Noncumulative Perpetual Preferred Stock Series I
Allegion plc Ordinary Shares
Allakos Inc. Common Stock
Allogene Therapeutics Inc. Common Stock
Allot Ltd. Ordinary Shares
Ally Financial Inc. Common Stock
GMAC Capital Trust I Fixed Rate Floating Rate Trust Preferred Securities Series 2
Allena Pharmaceuticals Inc. Common Stock
Alnylam Pharmaceuticals Inc. Common Stock
AstroNova Inc. Common Stock
Alabama Power Company 5.00% Class A Preferred Stock Cumulative Par Value $1 Per Share (Stated Capital $25 Per Share)
Alpine Immune Sciences Inc. Common Stock
Alarm.com Holdings Inc. Common Stock
Aileron Therapeutics Inc. Common Stock
Alerus Financial Corporation Common Stock
Alaska Communications Systems Group Inc. Common Stock
Allison Transmission Holdings Inc. Common Stock
Altimmune Inc. Common Stock
Altabancorp Common Stock
Alta Equipment Group Inc. Class A Common Stock
Alta Equipment Group Inc. Depositary Shares (each representing 1/1000th in a share of 10% Series A Cumulative Perpetual Preferred Stock)
Altus Midstream Company Class A Common Stock
Alto Ingredients Inc. Common Stock
Altair Engineering Inc. Class A Common Stock
Altitude Acquisition Corp. Class A Common Stock
Altitude Acquisition Corp. Unit
Altitude Acquisition Corp. Warrant
Alussa Energy Acquisition Corp. Class A Ordinary Shares
Autoliv Inc. Common Stock
AlloVir Inc. Common Stock
Alexander's Inc. Common Stock
Alexion Pharmaceuticals Inc. Common Stock
ALX Oncology Holdings Inc. Common Stock
Alithya Group inc. Class A Subordinate Voting Shares
Antero Midstream Corporation Common Stock
Amalgamated Bank Class A Common Stock
Applied Materials Inc. Common Stock
Ambarella Inc. Ordinary Shares
Ambac Financial Group Inc. Common Stock
Ambow Education Holding Ltd. American Depository Shares each representing two Class A ordinary shares
AMC Entertainment Holdings Inc. Class A Common Stock
Amcor plc Ordinary Shares
AMC Networks Inc. Class A Common Stock
Advanced Micro Devices Inc. Common Stock
AMETEK Inc.
Amedisys Inc Common Stock
Apollo Medical Holdings Inc. Common Stock
Emles Made in America ETF
Affiliated Managers Group Inc. Common Stock
Amgen Inc. Common Stock
American Homes 4 Rent Common Shares of Beneficial Interest
American Homes 4 Rent 6.5% Series D Cumulative Perpetual Preferred Shares of Beneficial Interest
American Homes 4 Rent 6.35% Series E Cumulative Redeemable Perpetual Preferred Shares of Beneficial Interest
American Homes 4 Rent 5.875% Series F Cumulative Redeemable Perpetual Preferred Shares
American Homes 4 Rent Series G cumulative redeemable perpetual preferred shares of beneficial interest
American Homes 4 Rent Series H cumulative redeemable perpetual Preferred Shares of Beneficial Interest
Amplitude Healthcare Acquisition Corporation Class A Common Stock
Amplitude Healthcare Acquisition Corporation Unit
Amplitude Healthcare Acquisition Corporation Warrants
AssetMark Financial Holdings Inc. Common Stock
Amkor Technology Inc. Common Stock
AMN Healthcare Services Inc AMN Healthcare Services Inc
American National Bankshares Inc. Common Stock
Allied Motion Technologies Inc.
America Movil S.A.B. de C.V. Class A American Depositary Shares
Ameriprise Financial Inc. Common Stock
Ampio Pharmaceuticals Inc.
Amplitech Group Inc. Common Stock
Amplitech Group Inc. Warrants
Amphastar Pharmaceuticals Inc. Common Stock
Amplify Energy Corp. Common Stock
Alpha Metallurgical Resources Inc. Common Stock
American River Bankshares Common Stock
Ameresco Inc. Class A Common Stock
A-Mark Precious Metals Inc. Common Stock
Amarin Corporation plc
Amyris Inc. Common Stock
Amneal Pharmaceuticals Inc. Class A Common Stock
American Shared Hospital Services Common Stock
American Superconductor Corporation Common Stock
AMERISAFE Inc. Common Stock
Amesite Inc. Common Stock
American Software Inc. Class A Common Stock
American Tower Corporation (REIT) Common Stock
Amerant Bancorp Inc. Class A Common Stock
Amerant Bancorp Inc. Class B Common Stock
Applied Molecular Transport Inc. Common Stock
Aemetis Inc. Common Stock
American Woodmark Corporation Common Stock
American Well Corporation Class A Common Stock
America Movil S.A.B. de C.V. American Depository Receipt Series L
Amryt Pharma plc American Depositary Shares
Amazon.com Inc. Common Stock
AutoNation Inc. Common Stock
AnaptysBio Inc. Common Stock
American National Group Inc. Common Stock
Anchiano Therapeutics Ltd. American Depositary Share
Andina Acquisition Corp. III Ordinary Shares
Andina Acquisition Corp. III Right
Andina Acquisition Corp. III Warrant
Andersons Inc. (The) Common Stock
Arista Networks Inc. Common Stock
Abercrombie & Fitch Company Common Stock
ANGI Homeservices Inc. Class A Common Stock
Angion Biomedica Corp. Common Stock
AngioDynamics Inc. Common Stock
Anworth Mortgage Asset Corporation Common Stock
Anworth Mortgage Asset Corporation Series A Preferred Stock
Anworth Mortgage Asset  Corporation Preferred Stock Series B 6.25%
Anworth Mortgage Asset  Corporation 7.625% Series C Cumulative Redeemable  Preferred Stock
Anika Therapeutics Inc. Common Stock
ANI Pharmaceuticals Inc.
Anixa Biosciences Inc. Common Stock
Annexon Inc. Common Stock
AnPac Bio-Medical Science Co. Ltd. American Depositary Shares
ANSYS Inc. Common Stock
AirNet Technology Inc. American Depositary Shares
Anthem Inc. Common Stock
Annovis Bio Inc. Common Stock
Sphere 3D Corp. Common Shares
Aberdeen Total Dynamic Dividend Fund Common Stock
Aon plc Class A Ordinary Shares (Ireland)
one Class A Ordinary Shares
A.O. Smith Corporation Common Stock
Alpha and Omega Semiconductor Limited Common Shares
American Outdoor Brands Inc. Common Stock 
Ampco-Pittsburgh Corporation Common Stock
Apache Corporation Common Stock
Artisan Partners Asset Management Inc. Class A Common Stock
Air Products and Chemicals Inc. Common Stock
Applied DNA Sciences Inc. Common Stock
American Public Education Inc. Common Stock
Apollo Endosurgery Inc. Common Stock
APi Group Corporation Common Stock
Amphenol Corporation Common Stock
Aphria Inc. Common Shares
Agora Inc. American Depositary Shares
Apple Hospitality REIT Inc. Common Shares
Apellis Pharmaceuticals Inc. Common Stock
Applied Therapeutics Inc. Common Stock
Aptorum Group Limited Class A Ordinary Shares
Apollo Global Management Inc. Class A Common Stock
Apollo Global Management Inc. 6.375% Series A Preferred Shares
Apollo Global Management Inc 6.375% Series B Preferred Shares
Apogee Enterprises Inc. Common Stock
Cellect Biotechnology Ltd. American Depositary Shares
Cellect Biotechnology Ltd. Warrants to Purchase ADRs
AppFolio Inc. Class A Common Stock
AppHarvest Inc. Common Stock
AppHarvest Inc. Warrants
Appian Corporation Class A Common Stock
Digital Turbine Inc. Common Stock
Apria Inc. Common Stock
Aprea Therapeutics Inc. Common stock
Blue Apron Holdings Inc. Class A Common Stock
Apollo Strategic Growth Capital Class A Ordinary Shares
Alpha Pro Tech Ltd. Common Stock
Aptose Biosciences Inc. Common Shares
Preferred Apartment Communities Inc. Common Stock
Aptiv PLC Ordinary Shares
Aptiv PLC 5.50% Series A Mandatory Convertible Preferred Shares
Aptinyx Inc. Common Stock
Aptevo Therapeutics Inc. Common Stock
Asia Pacific Wire & Cable Corporation Ltd. Ordinary Shares (Bermuda)
Apex Technology Acquisition Corporation Class A Common Stock
Apex Technology Acquisition Corporation Unit
Apex Technology Acquisition Corporation Warrant
Apyx Medical Corporation Common Stock
AquaBounty Technologies Inc. Common Stock
Aqua Metals Inc. Common Stock
Algonquin Power & Utilities Corp. Common Shares
Algonquin Power & Utilities Corp. 6.875% Fixed-to-Floating Rate Subordinated Notes Series 2018-A due October 17 2078
Algonquin Power & Utilities Corp. 6.20% Fixed-to-Floating Subordinated Notes Series 2019-A due July 1 2079
Aquestive Therapeutics Inc. Common Stock
Evoqua Water Technologies Corp. Common Stock
Antero Resources Corporation Common Stock
Aravive Inc. Common Stock
Accuray Incorporated Common Stock
Aequi Acquisition Corp. Class A Common Stock
Aequi Acquisition Corp. Unit
Aequi Acquisition Corp. warrants
ARC Document Solutions Inc. Common Stock
ArcBest Corporation Common Stock
Ares Capital Corporation Common Stock
Arco Platform Limited Class A Common Shares
Arch Resources Inc. Class A Common Stock
Arcos Dorados Holdings Inc. Class A Shares
Arcturus Therapeutics Holdings Inc. Common Stock
Ardagh Group S.A. Common Shares
Ares Dynamic Credit Allocation Fund Inc. Common Shares
Aridis Pharmaceuticals Inc. Common Stock
Ardelyx Inc. Common Stock
Alexandria Real Estate Equities Inc. Common Stock
American Resources Corporation Class A Common Stock
Ares Management Corporation Class A Common Stock
Ares Management Corporation 7.00% Series A Preferred Stock
Argo Group International Holdings Ltd. 6.5% Senior Notes Due 2042
Argo Group International Holdings Ltd.
Argo Group International Holdings Ltd. Depositary Shares Each Representing a 1/1000th Interest in a 7.00% Resettable Fixed Rate Preference Share Series A
argenx SE American Depositary Shares
Apollo Commercial Real Estate Finance Inc
Ark Global Acquisition Corp. Unit
ARKO Corp. Common Stock
ARKO Corp. Warrant
Ark Restaurants Corp. Common Stock
American Realty Investors Inc. Common Stock
Arlo Technologies Inc. Common Stock
Alliance Resource Partners L.P. Common Units representing Limited Partners Interests
Aramark Common Stock
Armata Pharmaceuticals Inc. Common Stock
Arena Pharmaceuticals Inc. Common Stock
Arconic Corporation Common Stock 
Archrock Inc. Common Stock
Arrow Financial Corporation Common Stock
Aerpio Pharmaceuticals Inc. Common Stock
Arcutis Biotherapeutics Inc. Common Stock
ARMOUR Residential REIT Inc.
ARMOUR Residential REIT Inc. 7% Series C Cumulative Redeemable Preferred Stock (liquidation preference $25.00 per share)
Array Technologies Inc. Common Stock
Artelo Biosciences Inc. Common Stock
Artelo Biosciences Inc. Warrant
Artesian Resources Corporation Class A Common Stock
Art's-Way Manufacturing Co. Inc. Common Stock
Arvinas Inc. Common Stock
Arrow Electronics Inc. Common Stock
Arrowhead Pharmaceuticals Inc. Common Stock
ARYA Sciences Acquisition Corp III Class A Ordinary Shares
ASA  Gold and Precious Metals Limited
Asana Inc. Class A Common Stock
Atlantic Street Acquisition Corp Class A Common Stock
Astrea Acquisition Corp. Unit
Associated Banc-Corp Common Stock
Associated Banc-Corp Depositary shares each representing a 1/40th ownership interest in a share of 6.125% Non-Cumulative Perpetual Preferred Stock Series C
Associated Banc-Corp Depositary Shares each representing a 1/40th interest in a share of Associated Banc-Corp 5.375% Non-Cumulative Perpetual Preferred Stock Series D
Associated Banc-Corp Depositary Shares each representing a 1/40th interest in a share of 5.875% Non-Cumulative Perpetual Preferred Stock Series E
Associated Banc-Corp Depositary Shares each representing a 1/40th interest in a share of Associated Banc-Corp 5.625% Non-Cumulative Perpetual Preferred Stock Series F
Ardmore Shipping Corporation Common Stock
Liberty All-Star Growth Fund Inc.
Aberdeen Standard Global Infrastructure Income Fund Common Shares of Beneficial Interest
ASGN Incorporated Common Stock
Ashland Global Holdings Inc. Common Stock
AdvanSix Inc. Common Stock 
AerSale Corporation Common Stock
AerSale Corporation Warrants
ASLAN Pharmaceuticals Limited American Depositary Shares
Avino Silver & Gold Mines Ltd. Common Shares (Canada)
Assembly Biosciences Inc. Common Stock
ASML Holding N.V. New York Registry Shares
Ascendis Pharma A/S American Depositary Shares
Academy Sports and Outdoors Inc. Common Stock
Alpha Capital Acquisition Company Unit
Aspirational Consumer Lifestyle Corp. Class A Ordinary Shares
Aspen Aerogels Inc. Common Stock
Altisource Portfolio Solutions S.A. Common Stock
Aspen Group Inc. Common Stock
Grupo Aeroportuario del Sureste S.A. de C.V. Common Stock
Assertio Holdings Inc. Common Stock
AmeriServ Financial Inc. Common Stock
AmeriServ Financial Inc. AmeriServ Financial Trust I - 8.45% Beneficial Unsecured Securities Series A
Astrotech Corporation (DE) Common Stock
Astec Industries Inc. Common Stock
Asure Software Inc Common Stock
ASE Technology Holding Co. Ltd. American Depositary Shares (each representing Two Common Shares) 
Amtech Systems Inc. Common Stock
Atlantic Power Corporation Ordinary Shares (Canada)
Americas Technology Acquisition Corp. Ordinary Shares
Altimar Acquisition Corporation Class A Ordinary Shares
America First Multifamily Investors L.P. Beneficial Unit Certificates (BUCs) representing Limited Partnership Interests
Atotech Limited Common Shares
Atlas Corp. Common Shares
Atlas Corp. 7.95% Series D
Atlas Corp. 8.25% Series E
Atlas Corp. 8.20% Series G
Atlas Corp. 7.875% Series H
Atlas Corp. Series I Fixed-to-Floating 
Atlas Technical Consultants Inc. Class A Common Stock
Alphatec Holdings Inc. Common Stock
A10 Networks Inc. Common Stock
Anterix Inc. Common Stock
Adtalem Global Education Inc. Common Stock
Athene Holding Ltd. Class A Common Shares
Athene Holding Ltd. Depositary Shares Each Representing a 1/1000th Interest in a 6.35% Fixed-to-Floating Rate Perpetual Non-Cumulative Preference Share Series A
Athene Holding Ltd. Depositary Shares Each Representing a 1/1000th Interest in a 5.625% Fixed Rate Perpetual Non- Cumulative Preference Share Series B par value $1.00 per share
Athene Holding Ltd. Depositary Shares each representing a 1/1000th Interest in a Share of 6.375% Fixed-Rate Reset Perpetual Non-Cumulative Preference Shares Series C
Athene Holding Ltd. Depositary Shares Each Representing a 1/1000th Interest in a 4.875% Fixed-Rate Perpetual Non-Cumulative Preference Share Series D
Athira Pharma Inc. Common Stock
Alterity Therapeutics Limited American Depositary Shares
Autohome Inc. American Depositary Shares each representing four class A ordinary shares.
Athersys Inc. Common Stock
Allegheny Technologies Incorporated Common Stock
ATIF Holdings Limited Ordinary Shares
Atkore Inc. Common Stock
Atlanticus Holdings Corporation Common Stock
Ames National Corporation Common Stock
180 Life Sciences Corp. Common Stock
180 Life Sciences Corp. Warrant
ATN International Inc. Common Stock
Actinium Pharmaceuticals Inc. (Delaware) Common Stock
Athenex Inc. Common Stock
Atmos Energy Corporation Common Stock
Atomera Incorporated Common Stock
Atossa Therapeutics Inc. Common Stock
AptarGroup Inc. Common Stock
Atara Biotherapeutics Inc. Common Stock
AtriCure Inc. Common Stock
Atrion Corporation Common Stock
Astronics Corporation Common Stock
Antares Pharma Inc. Common Stock
Air Transport Services Group Inc
Atento S.A. Ordinary Shares
Altice USA Inc. Class A Common Stock
Activision Blizzard Inc. Common Stock
Avenue Therapeutics Inc. Common Stock
AngloGold Ashanti Limited Common Stock
Atlantic Union Bankshares Corporation Common Stock
Atlantic Union Bankshares Corporation Depositary Shares each representing a 1/400th ownership interest in a share of 6.875% Perpetual Non-Cumulative Preferred Stock Series A
Auburn National Bancorporation Inc. Common Stock
AudioCodes Ltd. Common Stock
Golden Minerals Company Common Stock
Aurinia Pharmaceuticals Inc Ordinary Shares
Autolus Therapeutics plc American Depositary Share
AutoWeb Inc. Common Stock
Auddia Inc. Common Stock
Auddia Inc. Warrants
Applied UV Inc. Common Stock
Yamana Gold Inc. Ordinary Shares (Canada)
Avista Corporation Common Stock
Grupo Aval Acciones y Valores S.A. ADR (Each representing 20 preferred shares)
Avanti Acquisition Corp. Class A Ordinary Shares
AeroVironment Inc. Common Stock
AvalonBay Communities Inc. Common Stock
Avalon GloboCare Corp. Common Stock
American Virtual Cloud Technologies Inc. Common Stock 
American Virtual Cloud Technologies Inc. Warrant expiring 4/7/2025
American Vanguard Corporation Common Stock ($0.10 Par Value)
AVDR US LargeCap ESG ETF
Avadel Pharmaceuticals plc American Depositary Shares
AVEO Pharmaceuticals Inc. Common Stock
Broadcom Inc. Common Stock
Broadcom Inc. 8.00% Mandatory Convertible Preferred Stock Series A
Avinger Inc. Common Stock
Avid Technology Inc. Common Stock
Atea Pharmaceuticals Inc. Common Stock
Advent Convertible and Income Fund
Avalara Inc. Common Stock
Avanos Medical Inc. Common Stock
Avient Corporation Common Stock
Aviat Networks Inc. Common Stock
Mission Produce Inc. Common Stock
AVROBIO Inc. Common Stock
Avnet Inc. Common Stock
Avantor Inc. Common Stock
Avantor Inc. Series A Mandatory Convertible Preferred Stock
Anavex Life Sciences Corp. Common Stock
Avery Dennison Corporation Common Stock
Avaya Holdings Corp. Common Stock
Alliancebernstein Global High Income Fund
Aspira Women's Health Inc. Common Stock
Armstrong World Industries Inc Common Stock
American Water Works Company Inc. Common Stock
Aberdeen Global Premier Properties Fund Common Shares of Beneficial Interest
American States Water Company Common Stock
Aware Inc. Common Stock
Avalon Holdings Corporation Common Stock
Axos Financial Inc. Common Stock
Abraxas Petroleum Corporation Common Stock
Accelerate Diagnostics Inc. Common Stock
Axogen Inc. Common Stock
American Axle & Manufacturing Holdings Inc. Common Stock
Axcella Health Inc. Common Stock
Axonics Modulation Technologies Inc. Common Stock
Axos Financial Inc. 6.25% Subordinated Notes Due 2026
Axon Enterprise Inc. Common Stock
American Express Company Common Stock
AMREP Corporation Common Stock
Axis Capital Holdings Limited Common Stock
Axis Capital Holdings Limited Depositary Shares each representing 1/100th interest in a share of a 5.50% Series E Preferred Shares
Axsome Therapeutics Inc. Common Stock
Axalta Coating Systems Ltd. Common Shares
AXT Inc Common Stock
Alexco Resource Corp Common Shares (Canada)
Atlantica Sustainable Infrastructure plc Ordinary Shares
Acuity Brands Inc. 
Ayala Pharmaceuticals Inc. Common Stock
AYRO Inc. Common Stock
Aytu BioScience Inc. Common Stock
Alteryx Inc. Class A Common Stock
The AZEK Company Inc. Class A Common Stock
AstraZeneca PLC American Depositary Shares
AutoZone Inc. Common Stock
Aspen Technology Inc. Common Stock
Azure Power Global Limited Equity Shares
AzurRx BioPharma Inc. Common Stock
Azul S.A. American Depositary Shares (each representing three preferred shares)
Aziyo Biologics Inc. Class A Common Stock
AZZ Inc.
Barnes Group Inc. Common Stock
Boeing Company (The) Common Stock
Alibaba Group Holding Limited American Depositary Shares each representing eight Ordinary share
Bank of America Corporation Common Stock
Bank of America Corporation Depositary Shares each representing a 1/1000 th interest in a share of Bank of America Corporation 6.000% Non-Cumulative
Bank of America Corporation Depositary Shares each representing a 1/1000th interest in a share of 6.000% Non-Cumulative Preferred Stock Series GG
Bank of America Corporation Depositary Sh repstg 1/1000th Perp Pfd Ser E
Bank of America Corporation Depositary Shares each representing a 1/1000th interest in a share of 5.875% Non- Cumulative Preferred Stock Series HH
Bank of America Corporation Non Cumulative Perpetual Conv Pfd Ser L
Bank of America Corporation Depositary Shares each representing a 1/1000th interest in a share of 5.375% Non-Cumulative Preferred Stock Series KK
Bank of America Corporation Depositary shares each representing 1/1000th interest in a share of 5.000% Non-Cumulative Preferred Stock Series LL
Bank of America Corporation Depositary shares each representing 1/1000th interest in a share of 4.375% Non-Cumulative Preferred Stock Series NN
Bank of America Corporation Depositary Shares each representing a 1/1000th interest in a share of 4.125% Non-Cumulative Preferred Stock Series PP
BlackRock Municipal Income Investment Quality Trust
Booz Allen Hamilton Holding Corporation Common Stock
Braskem SA ADR
Bally's Corporation Common Stock
Brookfield Asset Management Inc. Common Stock
Brookfield Finance Inc. 4.625% Subordinated Notes due October 16 2080
Brookfield Finance Inc. 4.50% Perpetual Subordinated Notes
Banc of California Inc. Common Stock
Banc of California Inc. Depositary Shares each representing a 1/40th interest in a share of 7.375% Non-Cumulative Perpetual Preferred Stock Series D
Banc of California Inc. Depositary Shares Each Representing a 1/40th Interest in a Share of 7.000% Non-Cumulative Perpetual Preferred Stock Series E
Bandwidth Inc. Class A Common Stock
BancFirst Corporation Common Stock
BancFirst Corporation - BFC Capital Trust II Cumulative Trust Preferred Securities
Banner Corporation Common Stock
StoneCastle Financial Corp Common Stock
Baosheng Media Group Holdings Limited Ordinary shares
Credicorp Ltd. Common Stock
Bioanalytical Systems Inc. Common Stock
Battalion Oil Corporation Common Stock
Liberty Media Corporation Series A Liberty Braves Common Stock
Liberty Media Corporation Series C Liberty Braves Common Stock
Baxter International Inc. Common Stock
BlackBerry Limited Common Stock
Banco BBVA Argentina S.A. ADS
Bed Bath & Beyond Inc. Common Stock
Concrete Pumping Holdings Inc. Common Stock
Banco Bradesco Sa American Depositary Shares
Barings BDC Inc. Common Stock
Banco Bradesco Sa American Depositary Shares (each representing one Common Share)
BlackRock Municipal Income Investment Trust
Beasley Broadcast Group Inc. Class A Common Stock
Brickell Biotech Inc. Common Stock
Vinco Ventures Inc. Common Stock
BridgeBio Pharma Inc. Common Stock
Blackrock Municipal Bond Trust
BHP Group PlcSponsored ADR
BlackRock Taxable Municipal Bond Trust Common Shares of Beneficial Interest
BBQ Holdings Inc. Common Stock
Barrett Business Services Inc. Common Stock
Brookfield Business Partners L.P. Limited Partnership Units 
Banco Bilbao Vizcaya Argentaria S.A. Common Stock
Build-A-Bear Workshop Inc. Common Stock
Best Buy Co. Inc. Common Stock
Brunswick Corporation Common Stock
Brunswick Corporation 6.500% Senior Notes due 2048
Brunswick Corporation 6.625% Senior Notes due 2049
Brunswick Corporation 6.375% Notes due 2049
BioAtla Inc. Common Stock
Brookline Capital Acquisition Corp. Units
BlackRock Capital Allocation Trust Common Shares of Beneficial Interest
BCB Bancorp Inc. (NJ) Common Stock
Boise Cascade L.L.C. Common Stock
BioCardia Inc. Common Stock
BioCardia Inc. Warrant
BCE Inc. Common Stock
Bonanza Creek Energy Inc. Common Stock
Atreca Inc. Class A Common Stock
Banco De Chile Banco De Chile ADS
Brainstorm Cell Therapeutics Inc. Common Stock
BayCom Corp Common Stock
Brinks Company (The) Common Stock
Blucora Inc. Common Stock
Brightcove Inc. Common Stock
1895 Bancorp of Wisconsin Inc. Common Stock
Balchem Corporation Common Stock
BioCryst Pharmaceuticals Inc. Common Stock
Barclays PLC Common Stock
Bain Capital Specialty Finance Inc. Common Stock
BCTG Acquisition Corp. Common Stock
Bancroft Fund Ltd.
Bancroft Fund Limited 5.375% Series A Cumulative Preferred Shares
BlackRock Resources Common Shares of Beneficial Interest
Bicycle Therapeutics plc American Depositary Shares
Big Cypress Acquisition Corp. Common stock
Big Cypress Acquisition Corp. Unit
Big Cypress Acquisition Corp. Warrant
Belden Inc Common Stock
Blackrock Enhanced Equity Dividend Trust
Flanigan's Enterprises Inc. Common Stock
Brandywine Realty Trust Common Stock
Blonder Tongue Laboratories Inc. Common Stock
BioDelivery Sciences International Inc. Common Stock
Biodesix Inc. Common Stock
Black Diamond Therapeutics Inc. Common Stock
Becton Dickinson and Company Common Stock
Becton Dickinson and Company Depositary Shares each Representing a 1/20th Interest in a Share of 6.00% Mandatory Convertible Preferred Stock Series B
Bloom Energy Corporation Class A Common Stock
Beam Therapeutics Inc. Common Stock
Beacon Roofing Supply Inc. Common Stock
Bright Scholar Education Holdings Limited American Depositary Shares each  representing one Class A Ordinary Share
Beam Global Common Stock
Beam Global Warrant
KE Holdings Inc American Depositary Shares (each representing three Class A Ordinary Shares)
Bel Fuse Inc. Class A Common Stock
Bel Fuse Inc. Class B Common Stock
Franklin Resources Inc. Common Stock
Benessere Capital Acquisition Corp. Class A Common Stock
Benessere Capital Acquisition Corp. Right
Benessere Capital Acquisition Corp. Unit
Benessere Capital Acquisition Corp. Warrant
Brookfield Renewable Partners L.P. 
Brookfield Renewable Partners L.P. 5.25% Class A Preferred Limited Partnership Units Series 17
Brookfield Renewable Corporation Class A Subordinate Voting Shares 
Berry Global Group Inc. Common Stock
BEST Inc. American Depositary Shares each representing one Class A Ordinary Share
Brown Forman Corporation
Brown Forman Corporation
Bright Horizons Family Solutions Inc. Common Stock
Bank First Corporation Common Stock
BurgerFi International Inc. Common Stock 
BurgerFi International Inc. Warrant 
BankFinancial Corporation Common Stock
BlackRock Municipal Income Trust
Butterfly Network Inc. Class A Common Stock
Biofrontera AG American Depositary Shares
Saul Centers Inc. Common Stock
Saul Centers Inc. Depositary Shares each representing 1/100th of a share of 6.125% Series D Cumulative Redeemable Preferred Stock
Saul Centers Inc. Depositary shares each representing a 1/100th fractional interest in a share of 6.000% Series E Cumulative Redeemable Preferred Stock
Business First Bancshares Inc. Common Stock
Foley Trasimene Acquisition Corp. II Class A Common Stock
BlackRock New York Municipal Income Trust II
BlackRock California Municipal Income Trust
Bunge Limited Bunge Limited
Blackstone Strategic Credit Fund Common Shares
BGC Partners Inc Class A Common Stock
Big 5 Sporting Goods Corporation Common Stock
Barings Global Short Duration High Yield Fund Common Shares of Beneficial Interests
Birks Group Inc. Common Stock
BlackRock 2022 Global Income Opportunity Trust Common Shares of Beneficial Interest
FT Cboe Vest Gold Strategy Quarterly Buffer ETF
BeiGene Ltd. American Depositary Shares
BlackRock Energy and Resources Trust
B&G Foods Inc. B&G Foods Inc. Common Stock
BGSF Inc. Common Stock
BlackRock Floating Rate Income Trust
Blackstone Long Short Credit Income Fund Common Shares
Blackrock Enhanced International Dividend Trust
Biglari Holdings Inc. Class B Common Stock
Blue Hat Interactive Entertainment Technology Ordinary Shares
Bar Harbor Bankshares Inc. Common Stock
Bausch Health Companies Inc. Common Stock
Benchmark Electronics Inc. Common Stock
Brighthouse Financial Inc. Common Stock
Brighthouse Financial Inc. 6.25% Junior Subordinated Debentures due 2058
Brighthouse Financial Inc. Depositary shares each representing a 1/1000th interest in a share of 5.375% Non-Cumulative Preferred Stock Series C
Brighthouse Financial Inc. Depositary Shares 6.75% Non-Cumulative Preferred Stock Series B
Brighthouse Financial Inc. Depositary Shares 6.6% Non-Cumulative Preferred Stock Series A
Blackrock Core Bond Trust Blackrock Core Bond Trust
Berkshire Hills Bancorp Inc. Common Stock
BHP Group Limited American Depositary Shares (Each representing two Ordinary Shares)
Braemar Hotels & Resorts Inc. Common Stock
Braemar Hotels & Resorts Inc. 5.50% Series B Cumulative Convertible Preferred Stock par value $0.01 per share
Braemar Hotels & Resorts Inc. 8.25% Series D Cumulative Preferred Stock  par value $0.01 per share
Bull Horn Holdings Corp. Ordinary Shares
Bull Horn Holdings Corp. Unit
Bull Horn Holdings Corp. Warrants
BioHiTech Global Inc. Common Stock
BlackRock Virginia Municipal Bond Trust
Biohaven Pharmaceutical Holding Company Ltd. Common Shares
Baidu Inc. ADS
Boulder Growth & Income Fund Inc.
Big Lots Inc. Common Stock
BigCommerce Holdings Inc. Series 1 Common Stock
Biogen Inc. Common Stock
Bilibili Inc. American Depositary Shares
Bill.com Holdings Inc. Common Stock
BOQI International Medical Inc. Common Stock
Bio-Rad Laboratories Inc. Class A Common Stock
Bio-Rad Laboratories Inc.
Biocept Inc. Common Stock
Biolase Inc. Common Stock
Biotech Acquisition Company Unit
Bioceres Crop Solutions Corp. Ordinary Shares
Brookfield Infrastructure Partners LP Limited Partnership Units
Brookfield Infrastructure Partners LP 5.125% Class A Preferred Limited Partnership Units Series 13
Brookfield Infrastructure Partners LP 5.000% Class A Preferred Limited Partnership Units Series 14
Brookfield Infrastructure Partners LP Class A Subordinate Voting Shares 
BlackRock Multi-Sector Income Trust Common Shares of Beneficial Interest
BioVie Inc. Class A Common Stock
BJ's Wholesale Club Holdings Inc. Common Stock
BJ's Restaurants Inc. Common Stock
The Bank of New York Mellon Corporation Common Stock
BlackRock Capital Investment Corporation Common Stock
Brookdale Senior Living Inc. Common Stock
Buckle Inc. (The) Common Stock
Blueknight Energy Partners L.P. Common Units
Blueknight Energy Partners L.P. L.L.C. Series A Preferred Units
Black Hills Corporation Common Stock
Black Knight Inc. Common Stock 
BlackRock Investment Quality Municipal Trust Inc. (The)
Booking Holdings Inc. Common Stock
Baker Hughes Company Class A Common Stock
Bank of South Carolina Corp. Common Stock
BlackRock Income Trust Inc. (The)
BK Technologies Corporation Common Stock
BankUnited Inc. Common Stock
BIO-key International Inc. Common Stock
BlackLine Inc. Common Stock
Blue Bird Corporation Common Stock
Bellicum Pharmaceuticals Inc. Common Stock
BlueCity Holdings Limited American Depositary Shares
TopBuild Corp. Common Stock
Cambria Global Real Estate ETF
Ballard Power Systems Inc. Common Shares
Builders FirstSource Inc. Common Stock
BlackRock Municipal Income Trust II
BioLife Solutions Inc. Common Stock
Berkeley Lights Inc. Common Stock
Bridgeline Digital Inc. Common Stock
BlackRock Inc. Common Stock
Blackbaud Inc. Common Stock
Ball Corporation Common Stock
Bloomin' Brands Inc. Common Stock
Blink Charging Co. Common Stock
Blink Charging Co. Warrant
Bellerophon Therapeutics Inc. Common Stock
BioLineRx Ltd. American Depositary Shares
BCLS Acquisition Corp. Class A Ordinary Shares
Bright Lights Acquisition Corp. Unit
BELLUS Health Inc. Common Shares
bluebird bio Inc. Common Stock
Blue Water Acquisition Corp. Class A Common Stock
Blue Water Acquisition Corp. Unit
Blue Water Acquisition Corp. Warrant
Blackrock Limited Duration Income Trust
Banco Latinoamericano de Comercio Exterior S.A.
Banco Macro S.A.  ADR (representing Ten Class B Common Shares)
Bumble Inc. Class A Common Stock
Blackrock Health Sciences Trust
BlackRock Health Sciences Trust II Common Shares of Beneficial Interest
Badger Meter Inc. Common Stock
Bank of America Corporation Bank of America Corporation Depositary Shares (Each representing a 1/1200th interest in a share of Floating Rate Non-Cumulative Preferred Stock  Series 1)
Bank of America Corporation Bank of America Corporation Depositary Shares (Each representing a 1/1200th interest in a Share of Floating Rate Non-Cumulative Preferred Stock Series 2)
Bank of America Corporation Bank of America Corporation Depositary Shares (Each representing a 1/1200th interest in a Share of Floating Rate Non-Cumulative Preferred Stock Series 4)
Bank of America Corporation Bank of America Corporation Depositary Shares (Each representing a 1/1200th Interest in a Share of Floating Rate Non-Cumulative Preferred Stock Series 5)
Bank Of Montreal Common Stock
Biomerica Inc. Common Stock
Bank of Marin Bancorp Common Stock
BioMarin Pharmaceutical Inc. Common Stock
Bryn Mawr Bank Corporation Common Stock
BM Technologies Inc. Common Stock
Bristol-Myers Squibb Company Common Stock
Barnes & Noble Education Inc Common Stock
Benefitfocus Inc. Common Stock
Bionano Genomics Inc. Common Stock
Bionano Genomics Inc. Warrant
Broadstone Net Lease Inc. Class A Common Stock
Burning Rock Biotech Limited American Depositary Shares
Bank Nova Scotia Halifax Pfd 3 Ordinary Shares
Bonso Electronics International Inc. Common Stock
Benitec Biopharma Inc. Common Stock
BioNTech SE American Depositary Share
BlackRock New York Municipal Income Trust
Bluescape Opportunities Acquisition Corp. Class A Ordinary Shares
Merlyn.AI Best-of-Breed Core Momentum ETF
Bank of Commerce Holdings (CA) Common Stock
Blackrock Enhanced Global Dividend Trust Common Shares of Beneficial Interest
Bank of Hawaii Corporation Common Stock
BOK Financial Corporation Common Stock
BOK Financial Corporation 5.375% Subordinated Notes due 2056
Bolt Biotherapeutics Inc. Common Stock
Boston Omaha Corporation Class A Common Stock
DMC Global Inc. Common Stock
Boot Barn Holdings Inc. Common Stock
Borr Drilling Limited Common Shares
B.O.S. Better Online Solutions Common Stock
Bank of the James Financial Group Inc. Common Stock
BowX Acquisition Corp. Class A Common Stock
BowX Acquisition Corp. Unit
BowX Acquisition Corp. Warrant
Box Inc. Class A Common Stock
Boxlight Corporation Class A Common Stock
BP p.l.c. Common Stock
Boston Private Financial Holdings Inc. Common Stock
Blueprint Medicines Corporation Common Stock
BP Midstream Partners LP Common Units representing Limited Partner Interests
Popular Inc. Common Stock
Popular Inc. Popular Capital Trust II - 6.125% Cumulative Monthly Income Trust Preferred Securities
Popular Inc. 6.70% Cumulative Monthly Income Trust Preferred Securities
The Bank of Princeton Common Stock
BP Prudhoe Bay Royalty Trust Common Stock
Bio-Path Holdings Inc. Common Stock
Biophytis SA American Depositary Share
Brookfield Property Partners L.P. Limited Partnership Units
Brookfield Property Partners L.P. 5.750% Class A Cumulative Redeemable Perpetual Preferred Units Series 3
Brookfield Property Partners L.P. 6.375% Class A Cumulative Redeemable Perpetual Preferred Units Series 2
Brookfield Property Partners L.P. 6.50% Class A Cumulative Redeemable Perpetual Preferred Units
Brookfield Property REIT Inc. Class A Common Stock
Brookfield Property REIT Inc. 6.375% Series A Preferred Stock
Boqii Holding Limited American Depositary Shares representing Class A Ordinary Shares
Broadridge Financial Solutions Inc.Common Stock
BellRing Brands Inc. Class A Common Stock
Blue Ridge Bankshares Inc. Common Stock
Brady Corporation Common Stock
Breeze Holdings Acquisition Corp. Common Stock
Breeze Holdings Acquisition Corp. Right
Breeze Holdings Acquisition Corp. Warrant
BRF S.A.
Bluerock Residential Growth REIT Inc. Class A Common Stock
Bluerock Residential Growth REIT Inc. 8.250% Series A Cumulative Redeemable Preferred Stock ($0.01 par value per share)
Bluerock Residential Growth REIT Inc. 7.625% Series C Cumulative Redeemable Preferred Stock
Bluerock Residential Growth REIT Inc. 7.125% Series D Cumulative Preferred Stock ($0.01 par value per share)
Bridgford Foods Corporation Common Stock
Berkshire Hathaway Inc.
Berkshire Hathaway Inc.
Brookline Bancorp Inc. Common Stock
Bruker Corporation Common Stock
Brooks Automation Inc.
Brilliant Acquisition Corporation Ordinary Shares
Brilliant Acquisition Corporation Rights
Brilliant Acquisition Corporation Unit
Brilliant Acquisition Corporation Warrants
Broadmark Realty Capital Inc. Common Stock
Barnwell Industries Inc. Common Stock
Brown & Brown Inc. Common Stock
Brooge Energy Limited Ordinary Shares
Brooge Holdings Limited Warrant expiring 12/20/2024
BRP Group Inc. (Insurance Company) Class A Common Stock
Big Rock Partners Acquisition Corp. Common Stock
Big Rock Partners Acquisition Corp. Right
Big Rock Partners Acquisition Corp. Unit
Big Rock Partners Acquisition Corp. Warrant
B. Riley Principal 150 Merger Corp. Unit
Borqs Technologies Inc. Ordinary Shares
BRT Apartments Corp. (MD) Common Stock
Brixmor Property Group Inc. Common Stock
Berry Corporation (bry) Common Stock
BrightSphere Investment Group Inc. 5.125% Notes due 2031
Banco Santander - Chile ADS
Bogota Financial Corp. Common Stock
Banco Santander Brasil SA American Depositary Shares each representing one unit
BlackRock Strategic Municipal Trust Inc. (The) Common Stock
Blackrock New York Municipal Income Quality Trust Common Shares of Beneficial Interest
Bassett Furniture Industries Incorporated Common Stock
BioSig Technologies Inc. Common Stock
BrightSphere Investment Group Inc. Common Stock
Blackstone Senior Floating Rate Term Fund Common Shares of Beneficial Interest
Black Stone Minerals L.P. Common units representing limited partner interests
Banco Santander Mexico S.A. Institucion de Banca Multiple Grupo Financiero Santander Mexico
Broadstone Acquisition Corp. Class A Ordinary Shares
Bespoke Capital Acquisition Corp. Class A Restricted Voting Shares
BSQUARE Corporation Common Stock
Sierra Bancorp Common Stock
BlackRock Science and Technology Trust Common Shares of Beneficial Interest
BlackRock Science and Technology Trust II Common Shares of Beneficial Interest
Bank7 Corp. Common stock
Boston Scientific Corporation Common Stock
Boston Scientific Corporation 5.50% Mandatory Convertible Preferred Stock Series A
Bentley Systems Incorporated Class B Common Stock
BlackRock Long-Term Municipal Advantage Trust BlackRock Long-Term Municipal Advantage Trust Common Shares of Beneficial Interest
BioXcel Therapeutics Inc. Common Stock
Burgundy Technology Acquisition Corporation Class A Ordinary shares
Burgundy Technology Acquisition Corporation Unit
Burgundy Technology Acquisition Corporation Warrant
Bit Digital Inc. Ordinary Shares
B2Gold Corp Common shares (Canada)
British American Tobacco  Industries p.l.c. Common Stock ADR
Ballantyne Strong Inc. Common Stock
Bridgetown 2 Holdings Limited Class A Ordinary Shares
John Hancock Financial Opportunities Fund Common Stock
BTRS Holdings Inc. Class 1 Common Stock
BTRS Holdings Inc. Warrants
BlackRock Municipal 2030 Target Term Trust
Peabody Energy Corporation Common Stock 
Bridgetown Holdings Limited Class A Ordinary Shares
Bridgetown Holdings Limited Units
Bridgetown Holdings Limited Warrants
BlackRock Credit Allocation Income Trust
Anheuser-Busch Inbev SA Sponsored ADR (Belgium)
FT Cboe Vest Fund of Deep Buffer ETF
Innovator Laddered Fund of S&P 500 Power Buffer ETFs
BlackRock Utility Infrastructure & Power Opportunities Trust
Burford Capital Limited Ordinary Shares
Burlington Stores Inc. Common Stock
First Busey Corporation Class A Common Stock
BrightView Holdings Inc. Common Stock
Bluegreen Vacations Holding Corporation Class A Common Stock
Buenaventura Mining Company Inc.
Bioventus Inc. Class A Common Stock
BiondVax Pharmaceuticals Ltd. American Depositary Shares
Babcock & Wilcox Enterprises Inc. Common Stock
BorgWarner Inc. Common Stock
Better World Acquisition Corp. Common Stock
Better World Acquisition Corp. Unit
Better World Acquisition Corp. Warrants
Brainsway Ltd. American Depositary Shares
Bridgewater Bancshares Inc. Common Stock
Broadwind Inc. Common Stock
Bankwell Financial Group Inc. Common Stock
BrandywineGLOBAL Global Income Opportunities Fund Inc.
Bowl America Inc.
Betterware de Mexico S.A.B. de C.V. Ordinary Shares
Babcock & Wilcox Enterprises Inc. 8.125% Senior Notes due 2026
BWX Technologies Inc. Common Stock
The Blackstone Group Inc. Class A Common Stock
Bluelinx Holdings Inc. Common Stock
Bluegreen Vacations Corporation Common Stock
Blackstone Mortgage Trust Inc. Common Stock
Nuveen S&P 500 Buy-Write Income Fund Common Shares of Beneficial Interest
Boston Properties Inc. Common Stock
Boston Properties Inc. Depositary Shares each representing 1/100th of a share of the Issuer's 5.25% Sockeries B Cumulative Redeemable Preferred St
Baudax Bio Inc. Common Stock
BancorpSouth Bank Common Stock
BancorpSouth Bank 5.50% Series A Non-Cumulative Perpetual Preferred Stock
Byline Bancorp Inc. Common Stock
Boyd Gaming Corporation Common Stock
Broadway Financial Corporation Common Stock
Blackrock Municipal Income Quality Trust Common Shares of Beneficial Interest
Beyond Meat Inc. Common Stock
BeyondSpring Inc. Ordinary Shares
Beazer Homes USA Inc. Common Stock
BlackRock Maryland Municipal Bond Trust Common shares of beneficial interest
Baozun Inc. American Depositary Shares
Citigroup Inc. Common Stock
Citigroup Inc. Dep Shs Repstg 1/1000 Pfd Ser J Fixed/Fltg
Citigroup Inc. Dep Shs Repstg 1/1000th Pfd Ser K
Citigroup Capital XIII 7.875% Fixed rate Floating Rate trust Preferred Securities (TruPS)
Corporacion America Airports SA Common Shares
China Automotive Systems Inc. Common Stock
Cabaletta Bio Inc. Common Stock
Cable One Inc. Common Stock
Camden National Corporation Common Stock
Credit Acceptance Corporation Common Stock
CACI International Inc. Class A Common Stock
Cadence Bancorporation Class A Common Stock
CAE Inc. Ordinary Shares
Morgan Stanley China A Share Fund Inc. Common Stock
ConAgra Brands Inc. Common Stock
Cardinal Health Inc. Common Stock
CA Healthcare Acquisition Corp. Unit
CAI International Inc. Common Stock
CAI International Inc. 8.50% Series A Fixed-to-Floating Rate Cumulative Redeemable Perpetual Preferred Stock
CAI International Inc. 8.50% Series B Fixed-to-Floating Rate Cumulative Redeemable Perpetual Preferred Stock
Canon Inc. American Depositary Shares
Cheesecake Factory Incorporated (The) Common Stock
Caleres Inc. Common Stock
Calithera Biosciences Inc. Common Stock
California BanCorp Common Stock
Cal-Maine Foods Inc. Common Stock
Calliditas Therapeutics AB American Depositary Shares
Calix Inc Common Stock
CalAmp Corp. Common Stock
Camtek Ltd. Ordinary Shares
Canaan Inc. American Depositary Shares
Can-Fite Biopharma Ltd Sponsored ADR (Israel)
Cango Inc. American Depositary Shares  each representing two (2) Class A Ordinary Shares
Capitol Investment Corp. V Class A Common Stock
HighCape Capital Acquisition Corp. Class A Common Stock
HighCape Capital Acquisition Corp. Unit
HighCape Capital Acquisition Corp. Warrant
CrossAmerica Partners LP Common Units representing limited partner interests
Capricor Therapeutics Inc. Common Stock
Avis Budget Group Inc. Common Stock
Cara Therapeutics Inc. Common Stock
Carter Bankshares Inc. Common Stock
CarGurus Inc. Class A Common Stock 
Carrier Global Corporation Common Stock 
Cars.com Inc. Common Stock 
Carver Bancorp Inc. Common Stock
Cascade Acquisition Corp. Class A Common Stock
Casa Systems Inc. Common Stock
Meta Financial Group Inc. Common Stock
CASI Pharmaceuticals Inc. Common Stock
Cass Information Systems Inc Common Stock
Casey's General Stores Inc. Common Stock
Caterpillar Inc. Common Stock
Catabasis Pharmaceuticals Inc. Common Stock
Cambridge Bancorp Common Stock
Cardtronics plc Class A Ordinary Shares (UK)
Cato Corporation (The) Class A Common Stock
Cathay General Bancorp Common Stock
Chubb Limited  Common Stock
CBRE Acquisition Holdings Inc. Class A Common Stock
Colony Bankcorp Inc. Common Stock
CBAK Energy Technology Inc. Common Stock
CymaBay Therapeutics Inc. Common Stock
Cincinnati Bell Inc. Common Stock
Cincinnati Bell Inc. Preferred Stock
Companhia Brasileira de Distribuicao American Depsitary Shares; each representing one Common Share
CB Financial Services Inc. Common Stock
Virtus AllianzGI Convertible & Income 2024 Target Term Fund Common Shares of Beneficial Interest
Catalyst Biosciences Inc. Common Stock
Cleveland BioLabs Inc. Common Stock
CBM Bancorp Inc. Common Stock
Cellular Biomedicine Group Inc. Common Stock
Capital Bancorp Inc. Common Stock
Cboe Global Markets Inc. Common Stock
China Biologic Products Holdings Inc. Ordinary Shares
CBRE Group Inc Common Stock Class A
Cracker Barrel Old Country Store Inc Common Stock
Commerce Bancshares Inc. Common Stock
Cabot Corporation Common Stock
Cabot Growth ETF
CBTX Inc. Common Stock
Community Bank System Inc. Common Stock
CBIZ Inc. Common Stock
Chemours Company (The) Common Stock
CITIC Capital Acquisition Corp. Class A Ordinary Shares
Crescent Capital BDC Inc. Common stock
Coastal Financial Corporation Common Stock
Capital City Bank Group Common Stock
C4 Therapeutics Inc. Common Stock
Calamos Dynamic Convertible & Income Fund Common Stock
Coca-Cola European Partners plc Ordinary Shares
Chase Corporation Common Stock
Crown Castle International Corp. (REIT) Common Stock
Churchill Capital Corp IV Class A Common Stock
Cameco Corporation Common Stock
Crown Holdings Inc.
Carnival Corporation Common Stock
CSI Compressco LP Common Units
Concord Medical Services Holdings Limited ADS (Each represents three ordinary shares)
CMC Materials Inc. Common Stock
Code Chain New Continent Limited Common Stock
CNB Financial Corporation Common Stock
CNB Financial Corporation Depositary Shares each representing a 1/40th ownership interest in a share of 7.125% Series A Fixed-Rate Non-Cumulative Perpetual Preferred Stock
Clear Channel Outdoor Holdings Inc. Common Stock
Cogent Communications Holdings Inc.
China Customer Relations Centers Inc. Ordinary Shares
Cross Country Healthcare Inc. Common Stock $0.0001 Par Value
Century Communities Inc. Common Stock
Compania Cervecerias Unidas S.A. Common Stock
Churchill Capital Corp V Class A Common Stock
Churchill Capital Corp II Class A Common Stock
ChemoCentryx Inc. Common Stock
Comcast Holdings ZONES
Chindata Group Holdings Limited American Depositary Shares
Codiak BioSciences Inc. Common Stock
Ceridian HCM Holding Inc. Common Stock
Coeur Mining Inc. Common Stock
Centennial Resource Development Inc. Class A Common Stock
CDK Global Inc. Common Stock
Cardlytics Inc. Common Stock
Avid Bioservices Inc. Common Stock
Avid Bioservices Inc. 10.50% Series E Convertible Preferred Stock
CareDx Inc. Common Stock
Cadence Design Systems Inc. Common Stock
Condor Hospitality Trust Inc. Common Stock
Cedar Realty Trust Inc. Common Stock
Cedar Realty Trust Inc. 7.25% Series B Cumulative Redeemable Preferred Stock
Cedar Realty Trust Inc. 6.50% Series C Cumulative Redeemable Preferred Stock
Cidara Therapeutics Inc. Common Stock
CDW Corporation Common Stock
ChromaDex Corporation Common Stock
Codexis Inc. Common Stock
CADIZ Inc. Common Stock
Celanese Corporation Celanese Corporation Common Stock
China Eastern Airlines Corporation Ltd. Common Stock
CECO Environmental Corp. Common Stock
The Central and Eastern Europe Fund Inc. (The) Common Stock
Camber Energy Inc. Common Stock
CONSOL Energy Inc. Common Stock 
Celcuity Inc. Common Stock
Celsius Holdings Inc. Common Stock
Cypress Environmental Partners L.P. Common Units representing limited partner interests
ClearBridge MLP and Midstream Fund Inc. Common Stock
Chembio Diagnostics Inc. Common Stock
Center Coast Brookfield MLP & Energy Infrastructure Fund
Centricus Acquisition Corp. Unit
Central Garden & Pet Company Common Stock
Central Garden & Pet Company Class A Common Stock Nonvoting
Century Aluminum Company Common Stock
CNOOC Limited Common Stock
Central Puerto S.A. American Depositary Shares (each represents ten Common Shares)
Crestwood Equity Partners LP
Crestwood Equity Partners LP Preferred Units representing limited partner interests
Cerecor Inc. Common Stock
Cerevel Therapeutics Holdings Inc. Common Stock
Cerevel Therapeutics Holdings Inc. Warrant
Cerner Corporation Common Stock
Cerus Corporation Common Stock
Certara Inc. Common Stock
Central Securities Corporation Common Stock
Cemtrex Inc. Common Stock
Cemtrex Inc. Series 1 Preferred Stock
Cemtrex Inc. Series 1 Warrant
Eaton Vance California Municipal Income Trust Shares of Beneficial Interest
CEVA Inc. Common Stock
CF Industries Holdings Inc. Common Stock
CF Finance Acquisition Corp. III Common Stock
CF Finance Acquisition Corp. III Unit
CF Finance Acquisition Corp. III Warrant
CrossFirst Bankshares Inc. Common Stock
CF Bankshares Inc. Common Stock
ClearBridge Focus Value ETF
C&F Financial Corporation Common Stock
Capitol Federal Financial Inc. Common Stock
CF Acquisition Corp. V Unit
Citizens Financial Group Inc. Common Stock
Citizens Financial Group Inc. Depositary Shares each representing a 1/40th Interest in a Share of 6.350% Fixed-to-Floating Rate Non-Cumulative Perpetual Preferred Stock Series D
Citizens Financial Group Inc. Depositary Shares Each Representing 1/40th Interest in a Share of 5.000% Fixed-Rate Non-Cumulative Perpetual Preferred Stock Series E
CF Finance Acquisition Corp. II Class A Common Stock
CF Finance Acquisition Corp. II Unit
CF Finance Acquisition Corp. II Warrant
CF Acquisition Corp. IV Class A common stock
CF Acquisition Corp. IV Unit
CF Acquisition Corp. IV Warrant
Conformis Inc. Common Stock
Cullen/Frost Bankers Inc. Common Stock
Cullen/Frost Bankers Inc. Depositary Shares each representing a 1/40th ownership interest in a share of 4.450% non-cumulative perpetual preferred stock Series B
ContraFect Corporation Common Stock
CF Acquisition Corp. VI Unit
Colfax Corporation Common Stock
Colfax Corporation 5.75% Tangible Equity Units
The Carlyle Group Inc. Common Stock
China Green Agriculture Inc. Common Stock
TCG BDC Inc. Common Stock
Canopy Growth Corporation Common Shares
Cullinan Management Inc. Common Stock
Compugen Ltd. Ordinary Shares
Cancer Genetics Inc. Common Stock
Cognyte Software Ltd. Ordinary Shares
Cognex Corporation Common Stock
Calamos Global Total Return Fund Common Stock
Collective Growth Corporation Class A Common Stock
Collective Growth Corporation Unit
Collective Growth Corporation Warrant
Chardan Healthcare Acquisition 2 Corp. Common Stock
Comstock Holding Companies Inc. Class A Common Stock
City Holding Company Common Stock
Community Healthcare Trust Incorporated Common Stock
Church & Dwight Company Inc. Common Stock
Churchill Downs Incorporated Common Stock
Chemed Corp
The Chefs' Warehouse Inc. Common Stock
Check-Cap Ltd. Ordinary Share
Check-Cap Ltd. Series C Warrant
CHF Solutions Inc. Common Stock
Consonance-HFW Acquisition Corp. Class A Ordinary Shares
Chegg Inc. Common Stock
Choice Hotels International Inc. Common Stock
Calamos Convertible Opportunities and Income Fund Common Stock
Chesapeake Energy Corporation Common Stock
Chesapeake Energy Corporation Class C Warrants
Chesapeake Energy Corporation Class A Warrants
Chesapeake Energy Corporation Class B Warrants
Check Point Software Technologies Ltd. Ordinary Shares
Chiasma Inc. Common Stock
Chemung Financial Corp Common Stock
Cherry Hill Mortgage Investment Corporation Common Stock
Cherry Hill Mortgage Investment Corporation 8.20% Series A Cumulative Redeemable Preferred Stock
Cherry Hill Mortgage Investment Corporation 8.250% Series B Fixed-to-Floating Rate Cumulative Redeemable Preferred Stock
China Fund Inc. (The) Common Stock
Change Healthcare Inc. Common Stock
Change Healthcare Inc. Tangible Equity Units
China Natural Resources Inc. Common Stock
CHP Merger Corp. Class A Common Stock
CHP Merger Corp. Unit
CHP Merger Corp. Warrant
Charah Solutions Inc. Common Stock
Coherus BioSciences Inc. Common Stock
C.H. Robinson Worldwide Inc. Common Stock
Chico's FAS Inc. Common Stock
CHS Inc Class B Cumulative Redeemable Preferred Stock Series 4
CHS Inc Class B Reset Rate Cumulative Redeemable Preferred Stock Series 3
CHS Inc Preferred Class B Series 2 Reset Rate
CHS Inc. Class B Cumulative Redeemable Preferred Stock
CHS Inc. 8%  Cumulative Redeemable Preferred Stock
Chunghwa Telecom Co. Ltd.
Charter Communications Inc. Class A Common Stock New
Chuy's Holdings Inc. Common Stock
Calamos Global Dynamic Income Fund Common Stock
Chewy Inc. Class A Common Stock
ChampionX Corporation Common Stock 
Calamos Convertible and High Income Fund Common Stock
Cigna Corporation Common Stock
Citizens Inc. Class A Common Stock ($1.00 Par)
BanColombia S.A. Common Stock
Cinedigm Corp. Class A Common Stock
Ciena Corporation Common Stock
MFS Intermediate High Income Fund Common Stock
Comp En De Mn Cemig ADS American Depositary Shares
Colliers International Group Inc. Subordinate Voting Shares
China Index Holdings Limited American Depository Shares
Blackrock Capital and Income Fund Inc.
CIIG Merger Corp. Class A Common Stock
CIIG Merger Corp. Units
CIIG Merger Corp. Warrants
Credit Suisse Asset Management Income Fund Inc. Common Stock
Chimera Investment Corporation Common Stock
Chimera Investment Corporation 8.00% Series A Cumulative Redeemable Preferred Stock
Chimera Investment Corporation 8.00% Series B Fixed-to-Floating Rate Cumulative Redeemable Preferred Stock
Chimera Investment Corporation 7.75% Series C Fixed-to-Floating Rate  Cumulative Redeemable  Preferred Stock
Chimera Investment Corporation 8.00% Series D Fixed-to-Floating Rate Cumulative Redeemable Preferred Stock
Cincinnati Financial Corporation Common Stock
Ciner Resources LP Common Units representing Limited Partner Interests
City Office REIT Inc. Common Stock
City Office REIT Inc. 6.625% Series A Cumulative Redeemable Preferred Stock
CIRCOR International Inc. Common Stock
CIT Group Inc (DEL) Common Stock
CIT Group Inc (DEL) 5.625 % Non-Cumulative Perpetual Preferred Stock Series B
Civista Bancshares Inc. Common Stock
CompX International Inc. Common Stock
CI Financial Corp. Common Shares
Citizens Holding Company Common Stock
China Jo-Jo Drugstores Inc. Common Stock
SEACOR Holdings Inc. Common Stock
Checkpoint Therapeutics Inc. Common Stock
CKX Lands Inc. Common Stock
Colgate-Palmolive Company Common Stock
Colonnade Acquisition Corp. Class A Ordinary Shares
Clarus Corporation Common Stock
Core Laboratories N.V. Common Stock
Columbia Financial Inc. Common Stock
Caladrius Biosciences Inc. Common Stock
Cortland Bancorp Common Stock
Cloudera Inc. Common Stock
Chatham Lodging Trust (REIT) Common Shares of Beneficial Interest
Celldex Therapeutics Inc.
China Liberal Education Holdings Limited Ordinary Shares
Cleveland-Cliffs Inc. Common Stock
Clearfield Inc. Common Stock
CollPlant Biotechnologies Ltd American Depositary Shares
CoreLogic Inc. Common Stock
Clean Harbors Inc. Common Stock
Mack-Cali Realty Corporation Common Stock
Climate Change Crisis Real Impact I Acquisition Corporation Class A Common Stock
ClearSign Technologies Corporation Common Stock
Cellectis S.A. American Depositary Shares
Cornerstone Strategic Value Fund Inc. New Common Stock
Calumet Specialty Products Partners L.P. Common Units
Colony Credit Real Estate Inc. Class A Common Stock
Clean Energy Fuels Corp. Common Stock
Clene Inc. Common Stock
Clene Inc. Warrant
Colony Capital Inc.
Colony Capital Inc. 7.50% Series G cumulative redeemable perpetual preferred stock
Colony Capital Inc. 7.125% Series H cumulative redeemable perpetual preferred stock
Colony Capital Inc. 7.15% Series I Cumulative Redeemable Perpetual Preferred Stock
Colony Capital Inc. 7.125% Series J Cumulative Redeemable Perpetual Preferred Stock
Clover Health Investments Corp. Class A Common Stock
Clover Health Investments Corp. Warrants
Clipper Realty Inc. Common Stock
CLPS Incorporation Common Stock
ClearPoint Neuro Inc. Common Stock
Continental Resources Inc. Common Stock
Cellectar Biosciences Inc.  Common Stock
Cellectar Biosciences Inc. Series A Warrants
Clarim Acquisition Corp. Unit
ClearOne Inc. (DE) Common Stock
Celestica Inc. Common Stock
Clearside Biomedical Inc. Common Stock
CleanSpark Inc. Common Stock
Celsion Corporation Common Stock
Clever Leaves Holdings Inc. Common Shares
Clever Leaves Holdings Inc. Warrant
Clovis Oncology Inc. Common Stock
Clarivate Plc Ordinary Shares
Clearwater Paper Corporation Common Stock
Euro Tech Holdings Company Limited Common Stock
Clorox Company (The) Common Stock
Calyxt Inc. Common Stock
Canadian Imperial Bank of Commerce Common Stock
Comerica Incorporated Common Stock
Cambium Networks Corporation Ordinary Shares
Commercial Metals Company Common Stock
Caledonia Mining Corporation Plc Common Shares
Cheetah Mobile Inc. American Depositary Shares each representing 10 Class Ordinary Shares
Columbus McKinnon Corporation Common Stock
Comcast Corporation Class A Common Stock
CIM Commercial Trust Corporation Common stock
Cantel Medical Corp. Common Stock
CME Group Inc. Class A Common Stock
CM Finance Inc 6.125% Notes due 2023
Chipotle Mexican Grill Inc. Common Stock
Cummins Inc. Common Stock
CM Life Sciences Inc. Class A Common Stock
CM Life Sciences Inc. Unit
CM Life Sciences Inc. Warrant
Cumulus Media Inc. Class A Common Stock
Capstead Mortgage Corporation Common Stock
Capstead Mortgage Corporation Pfd Ser E
Compass Minerals Intl Inc Common Stock
Checkmate Pharmaceuticals Inc. Common Stock
Cimpress plc Ordinary Shares (Ireland)
COMPASS Pathways Plc American Depository Shares
Costamare Inc. Common Stock $0.0001 par value
Costamare Inc. Perpetual Preferred Stock Series B (Marshall Islands)
Costamare Inc. Perpetual Preferred Series C (Marshall Islands)
Costamare Inc. 8.75% Series D Cumulative Redeemable Perpetual Preferred Stock
Costamare Inc. 8.875% Series E Cumulative Redeemable Perpetual Preferred Stock par value $0.0001
Chimerix Inc. Common Stock
CMS Energy Corporation Common Stock
CMS Energy Corporation Preferred Stock
CMS Energy Corporation 5.625% Junior Subordinated Notes due 2078
CMS Energy Corporation 5.875% Junior Subordinated Notes due 2078
CMS Energy Corporation 5.875% Junior Subordinated Notes due 2079
Core Molding Technologies Inc Common Stock
Comtech Telecommunications Corp. Common Stock
MFS Municipal Income Trust Common Stock
CNA Financial Corporation Common Stock
Century Bancorp Inc. Class A Common Stock
Centene Corporation Common Stock
Concert Pharmaceuticals Inc. Common Stock
Concord Acquisition Corp. Class A Common Stock
Conduent Incorporated Common Stock 
ZW Data Action Technologies Inc. Common Stock
CN Energy Group Inc. Ordinary Shares
CNFinance Holdings Limited American Depositary Shares each representing  twenty (20) Ordinary Shares
Conifer Holdings Inc. Common Stock
Conifer Holdings Inc. 6.75% Senior Unsecured Notes due 2023
CNH Industrial N.V. Common Shares
Canadian National Railway Company Common Stock
Cinemark Holdings Inc Cinemark Holdings Inc. Common Stock
CONMED Corporation Common Stock
Cincinnati Bancorp Inc. Common Stock
Cannae Holdings Inc. Common Stock
CNO Financial Group Inc. Common Stock
CNO Financial Group Inc. 5.125% Subordinated Debentures due 2060
ConnectOne Bancorp Inc. Common Stock
CenterPoint Energy Inc (Holding Co) Common Stock
CenterPoint Energy Inc. Depositary Shares Each Representing a 1/20th Interest in a Share of 7.00% Series B Mandatory Convertible Preferred Stock
Canadian Natural Resources Limited Common Stock
Cornerstone Building Brands Inc. Common Stock
Cohen & Steers Inc Common Stock
Consolidated Communications Holdings Inc. Common Stock
CNS Pharmaceuticals Inc. Common Stock
Constellation Pharmaceuticals Inc. Common Stock
Centogene N.V. Common Shares
Century Casinos Inc. Common Stock
CNX Resources Corporation Common Stock
Concentrix Corporation Common Stock
PC Connection Inc. Common Stock
Global Cord Blood Corporation Common Stock
Cocrystal Pharma Inc. Common Stock
Coda Octopus Group Inc. Common stock
D/B/A Compass Diversified Holdings Shares of Beneficial Interest
Compass Diversified Holdings 7.250% Series A Preferred Shares representing beneficial interest in Compass Diversified Holdings
Compass Diversified Holdings 7.875% Series B Fixed-to-Floating Rate Cumulative Preferred Shares representing beneficial interests in Compass Diversified Holdings
Compass Diversified Holdings 7.875% Series C Cumulative Preferred Shares
Co-Diagnostics Inc. Common Stock
China Online Education Group American depositary shares each representing 15 Class A ordinary shares
Capital One Financial Corporation Common Stock
Capital One Financial Corporation Depositary Shares Each Representing a 1/40th Interest in a Share of Fixed Rate Non-Cumulative Perpetual Preferred Stock Series G
Capital One Financial Corporation Depositary Shares Each Representing 1/40th Interest in a Share of Fixed Rate Non-Cumulative Perpetual Preferred Stock Series H
Capital One Financial Corporation Depositary shares each representing a 1/40th interest in a share of Fixed Rate Non-Cumulative Perpetual Preferred Stock Series I of the Issuer
Capital One Financial Corporation Depositary Shares Each Representing a 1/40th Interest in a Share of Fixed Rate Non- Cumulative Perpetual Preferred Stock Series J
Capital One Financial Corporation Depositary Shares Each Representing a 1/40th Ownership Interest in a Share of Fixed Rate Non-Cumulative Perpetual Preferred Stock Series K
ChoiceOne Financial Services Inc. Common Stock
Cabot Oil & Gas Corporation Common Stock
Cogent Biosciences Inc. Common Stock
Cohen & Company Inc.
Coherent Inc. Common Stock
Cohu Inc. Common Stock
Coca-Cola Consolidated Inc. Common Stock
Columbia Banking System Inc. Common Stock
Americold Realty Trust Common Shares
Collegium Pharmaceutical Inc. Common Stock
Columbia Sportswear Company Common Stock
CommScope Holding Company Inc. Common Stock
ComSovereign Holding Corp. Common Stock
ComSovereign Holding Corp. Warrants
CyrusOne Inc Common Stock
Conn's Inc. Common Stock
CONX Corp. Class A Common Stock
CONX Corp. Unit
CONX Corp. Warrant
The Cooper Companies Inc. Common Stock
Corner Growth Acquisition Corp. Class A Ordinary Shares
Corner Growth Acquisition Corp. Unit
Corner Growth Acquisition Corp. Warrant
Mr. Cooper Group Inc. Common Stock
ConocoPhillips Common Stock
CoreSite Realty Corporation Common Stock
Core Mark Holding Co Inc Common Stock
CorEnergy Infrastructure Trust Inc. Common Stock
CorEnergy Infrastructure Trust Inc. Depositary Shares each representing a 1/100th fractional interest of a share of 7.375% Series A Cumulative Redeemable Preferred Stock
Corcept Therapeutics Incorporated Common Stock
Costco Wholesale Corporation Common Stock
Coty Inc. Class A Common Stock
Coupa Software Incorporated Common Stock
COVA Acquisition Corp. Unit
Cowen Inc. Class A Common Stock
Cowen Inc. 7.75% Senior Notes due 2033
Cowen Inc. 7.35% Senior Notes Due 2027
Canadian Pacific Railway Limited Common Stock
Copa Holdings S.A. Copa Holdings S.A. Class A Common Stock
Cementos Pacasmayo S.A.A. American Depositary Shares (Each representing five Common Shares)
CounterPath Corporation Common Stock
Campbell Soup Company Common Stock
Callon Petroleum Company Common Stock
Central Pacific Financial Corp New
Crescent Point Energy Corporation Ordinary Shares (Canada)
Canterbury Park Holding Corporation 'New' Common Stock
China Pharma Holdings Inc. Common Stock
Cumberland Pharmaceuticals Inc. Common Stock
Chesapeake Utilities Corporation Common Stock
CorePoint Lodging Inc. Common Stock 
Capital Product Partners L.P. Common Units
Capri Holdings Limited Ordinary Shares
Copart Inc. (DE) Common Stock
Catalyst Pharmaceuticals Inc. Common Stock
Cooper-Standard Holdings Inc. Common Stock
CPS Technologies Corp. Common Stock
Computer Programs and Systems Inc. Common Stock
Capstar Special Purpose Acquisition Corp. Class A Common Stock
Consumer Portfolio Services Inc. Common Stock
Capstone Turbine Corporation Common Stock
Camden Property Trust Common Stock
Capitala Finance Corp. Common Stock
Capitala Finance Corp. 5.75% Convertible Notes Due 2022
Capitala Finance Corp. 6% Notes Due 2022
Calamos Long/Short Equity & Dynamic Income Trust Common Stock
Cheniere Energy Partners LP Cheniere Energy Partners LP Common Units
Crane Co. Common Stock
CRA International Inc. Common Stock
Corbus Pharmaceuticals Holdings Inc. Common Stock
California Resources Corporation Common Stock
Crawford & Company
Crawford & Company
Cardiff Oncology Inc. Common Stock
Cree Inc. Common Stock
China Recycling Energy Corporation Common Stock
Cresud S.A.C.I.F. y A. American Depositary Shares
Creative Realities Inc. Common Stock
Creative Realities Inc. Warrant
Cornerstone Total Return Fund Inc. (The) Common Stock
CRH PLC American Depositary Shares
Cohn Robbins Holdings Corp. Class A Ordinary Shares
CRH Medical Corporation Common Shares of Beneficial Interest
Carter's Inc. Common Stock
Curis Inc. Common Stock
Comstock Resources Inc. Common Stock
Crown Electrokinetics Corp. Common Stock
Charles River Laboratories International Inc. Common Stock
Salesforce.com Inc Common Stock
CorMedix Inc. Common Stock
America's Car-Mart Inc Common Stock
Cerence Inc. Common Stock
Ceragon Networks Ltd. Ordinary Shares
Crinetics Pharmaceuticals Inc. Common Stock
Cronos Group Inc. Common Share
Crocs Inc. Common Stock
Carpenter Technology Corporation Common Stock
Crescent Acquisition Corp Class A Common Stock
Crescent Acquisition Corp Unit
Crescent Acquisition Corp Warrant
CRISPR Therapeutics AG Common Shares
Corsair Gaming Inc. Common Stock
Cross Timbers Royalty Trust Common Stock
Creatd Inc. Common Stock
Creatd Inc. Warrant
Criteo S.A. American Depositary Shares
Cortexyme Inc. Common Stock
Cirrus Logic Inc. Common Stock
CorVel Corp. Common Stock
Corvus Pharmaceuticals Inc. Common Stock
CrowdStrike Holdings Inc. Class A Common Stock
Crown Crafts Inc Common Stock
CryoLife Inc. Common Stock
Credit Suisse Group American Depositary Shares
Champions Oncology Inc. Common Stock
Cisco Systems Inc. Common Stock (DE)
Color Star Technology Co. Ltd. Ordinary Shares
CoStar Group Inc. Common Stock
CSG Systems International Inc. Common Stock
Cardiovascular Systems Inc. Common Stock
Canadian Solar Inc. Common Shares (BC)
Carlisle Companies Incorporated Common Stock
Castlight Health Inc. Class B Common Stock
Cornerstone OnDemand Inc. Common Stock
CSP Inc. Common Stock
Casper Sleep Inc. Common Stock
Calamos Strategic Total Return Common Stock
D/B/A Centerspace Common Stock
D/B/A Centerspace 6.625% Series C 
Chicken Soup for the Soul Entertainment Inc. Class A Common Stock
Chicken Soup for the Soul Entertainment Inc. 9.50% Notes due 2025
Chicken Soup for the Soul Entertainment Inc. 9.75% Series A Cumulative Redeemable Perpetual Preferred Stock
Caesarstone Ltd. Ordinary Shares
Castle Biosciences Inc. Common Stock
Constellium SE Ordinary Shares (France)
CapStar Financial Holdings Inc. Common Stock
Capital Senior Living Corporation Common Stock
Carriage Services Inc. Common Stock
Capital Southwest Corporation Common Stock
CSW Industrials Inc. Common Stock
CSX Corporation Common Stock
E.I. du Pont de Nemours and Company Preferred Stock
E.I. du Pont de Nemours and Company Preferred Stock
Cerberus Telecom Acquisition Corp. Class A Ordinary Shares
Carney Technology Acquisition Corp. II Class A Common Stock
Carney Technology Acquisition Corp. II Units
Carney Technology Acquisition Corp. II Warrant
Cintas Corporation Common Stock
Cooper Tire & Rubber Company Common Stock
Qwest Corporation 6.5% Notes due 2056
Community Trust Bancorp Inc. Common Stock
Qwest Corporation 6.75% Notes due 2057
CynergisTek Inc. Common Stock
Computer Task Group Inc. Common Stock
Charles & Colvard Ltd Common Stock
Yunhong CTI Ltd. Common Stock
CTI BioPharma Corp. (DE) Common Stock
CooTek (Cayman) Inc. American Depositary Shares each representing 50 Class A Ordinary Shares
Catalent Inc. Common Stock
CytomX Therapeutics Inc. Common Stock
CTO Realty Growth Inc. Common Stock
ClearBridge MLP and Midstream Total Return Fund Inc. Common Stock
CareTrust REIT Inc. Common Stock
Castor Maritime Inc. Common Shares
Citi Trends Inc. Common Stock
CTS Corporation Common Stock
Cognizant Technology Solutions Corporation Class A Common Stock
Cytosorbents Corporation Common Stock
CatchMark Timber Trust Inc. Class A Common Stock
Corteva Inc. Common Stock 
Citius Pharmaceuticals Inc. Common Stock
Citius Pharmaceuticals Inc. Warrant
Citrix Systems Inc. Common Stock
Cubic Corporation Common Stock
Herzfeld Caribbean Basin Fund Inc. (The) Common Stock
Customers Bancorp Inc 5.375% Subordinated Notes Due 2034
CubeSmart Common Shares
Customers Bancorp Inc Common Stock
Customers Bancorp Inc Fixed-to-Floating Rate Non-Cumulative Perpetual Preferred Stock Series C
Customers Bancorp Inc Fixed-to-Floating Rate Non-Cumulative Perpetual Preferred Stock Series D
Customers Bancorp Inc Fixed-to-Floating Rate Non-Cumulative Perpetual Preferred Stock Series E
Customers Bancorp Inc Fixed-to-Floating Rate Non-Cumulative Perpetual Preferred Stock Series F
Cue Biopharma Inc. Common Stock
Cuentas Inc. Common Stock
Cuentas Inc. Warrant
Carnival Plc ADS ADS
Culp Inc. Common Stock
CuriosityStream Inc. Class A Common Stock
CuriosityStream Inc. Warrant
CURO Group Holdings Corp. Common Stock
Cutera Inc. Common Stock
Cousins Properties Incorporated Common Stock
Covanta Holding Corporation Common Stock
CureVac N.V. Ordinary Shares
CVB Financial Corporation Common Stock
Cavco Industries Inc. Common Stock When Issued
Central Valley Community Bancorp Common Stock
Cenovus Energy Inc Common Stock
Civeo Corporation (Canada) Common Shares
Covetrus Inc. Common Stock
Commercial Vehicle Group Inc. Common Stock
Calavo Growers Inc. Common Stock
CVR Energy Inc. Common Stock
Conversion Labs Inc. Common Stock
Covenant Logistics Group Inc. Class A Common Stock
Commvault Systems Inc. Common Stock
Codorus Valley Bancorp Inc Common Stock
Cel-Sci Corporation Common Stock
Carvana Co. Class A Common Stock
Chicago Rivet & Machine Co. Common Stock
CVS Health Corporation Common Stock
CPI Aerostructures Inc. Common Stock
CVD Equipment Corporation Common Stock
Chevron Corporation Common Stock
Curtiss-Wright Corporation Common Stock
Community West Bancshares Common Stock
CohBar Inc. Common Stock
Consolidated Water Co. Ltd. Ordinary Shares
Clearway Energy Inc. Class C Common Stock
Camping World Holdings Inc. Class A Commom Stock
Cushman & Wakefield plc Ordinary Shares
Casella Waste Systems Inc. Class A Common Stock
California Water Service Group Common Stock
Cemex S.A.B. de C.V. Sponsored ADR
China XD Plastics Company Limited Common Stock
Crexendo Inc. Common Stock
MFS High Income Municipal Trust Common Stock
MFS Investment Grade Municipal Trust Common Stock
Columbia Property Trust Inc. Common Stock
CoreCivic Inc. Common Stock
Celyad Oncology SA American Depositary Shares
Cyanotech Corporation Common Stock
CyberOptics Corporation Common Stock
CyberArk Software Ltd. Ordinary Shares
Cyclacel Pharmaceuticals Inc. Common Stock
Cyclerion Therapeutics Inc. Common Stock
China Yuchai International Limited Common Stock
Community Health Systems Inc. Common Stock
CYREN Ltd. Ordinary Shares
CryoPort Inc. Common Stock
Cyclo Therapeutics Inc. Common Stock
Cyclo Therapeutics Inc. Warrant
Cytokinetics Incorporated Common Stock
Citizens & Northern Corp Common Stock
Caesars Entertainment Inc. Common Stock
Citizens Community Bancorp Inc. Common Stock
Cosan Limited Class A Common Stock
Dominion Energy Inc. Common Stock
Danaos Corporation Common Stock
Dada Nexus Limited American Depositary Shares
Data I/O Corporation Common Stock
Daktronics Inc. Common Stock
Delta Air Lines Inc. Common Stock
Dana Incorporated Common Stock 
Youdao Inc. American Depositary Shares each representing one Class A Ordinary Share
Darling Ingredients Inc. Common Stock
Dare Bioscience Inc. Common Stock
DoorDash Inc. Class A Common Stock
FT Cboe Vest U.S. Equity Deep Buffer ETF - August
Endava plc American Depositary Shares (each representing one Class A Ordinary Share)
Deutsche Bank AG Common Stock
Diebold Nixdorf Incorporated Common Stock
Roman DBDR Tech Acquisition Corp. Class A Common Stock
Roman DBDR Tech Acquisition Corp. Unit
Roman DBDR Tech Acquisition Corp. Warrant
Designer Brands Inc. Class A Common Stock
DoubleLine Opportunistic Credit Fund Common Shares of Beneficial Interest
Innovator Double Stacker 9 Buffer ETF - October
Decibel Therapeutics Inc. Common Stock
DBV Technologies S.A. American Depositary Shares
Dropbox Inc. Class A Common Stock
Docebo Inc. Common Shares
BNY Mellon Alcentra Global Credit Income 2024 Target Term Fund Inc. Common Stock
Donaldson Company Inc. Common Stock
Ducommun Incorporated Common Stock
Dime Community Bancshares Inc. Common Stock
Dime Community Bancshares Inc. Fixed-Rate Non-Cumulative Perpetual Preferred Stock Series A
DCP Midstream  LP Common Units 
DCP Midstream LP 7.875% Series B Fixed-to-Floating Rate Cumulative Redeemable Perpetual Preferred Units
DCP Midstream LP 7.95% Series C Fixed-to-Floating Rate Cumulative Redeemable Perpetual Preferred Units
Deciphera Pharmaceuticals Inc. Common Stock
Decarbonization Plus Acquisition Corporation Class A Common Stock
Decarbonization Plus Acquisition Corporation Unit
Decarbonization Plus Acquisition Corporation Warrant
Decarbonization Plus Acquisition Corporation II Unit
Duck Creek Technologies Inc. Common Stock
Delcath Systems Inc. Common Stock
Dominion Energy Inc. 2019 Series A Corporate Units
DuPont de Nemours Inc. Common Stock
3D Systems Corporation Common Stock
FT Cboe Vest U.S. Equity Deep Buffer ETF - December
Delaware Investments Dividend & Income Fund Inc. Common Stock
DD3 Acquisition Corp. II Class A Common Stock
DD3 Acquisition Corp. II Unit
DD3 Acquisition Corp. II Warrant
Datadog Inc. Class A Common Stock
Dillard's Inc. Common Stock
Dillard's Capital Trust I
Deere & Company Common Stock
Easterly Government Properties Inc. Common Stock
Deckers Outdoor Corporation Common Stock
Emles Trust Emles Protective Allocation ETF
D8 Holdings Corp. Class A Ordinary Shares
Douglas Emmett Inc. Common Stock
Dell Technologies Inc. Class C Common Stock 
Denbury Inc. Common Stock
Denny's Corporation Common Stock
Diageo plc Common Stock
Despegar.com Corp. Ordinary Shares
Delaware Enhanced Global Dividend Common Shares of Beneficial Interest
FT Cboe Vest U.S. Equity Deep Buffer ETF - February
Diffusion Pharmaceuticals Inc. Common Stock
Dream Finders Homes Inc. Class A Common Stock
Deerfield Healthcare Technology Acquisitions Corp. Class A Common Stock
Deerfield Healthcare Technology Acquisitions Corp. Unit
Deerfield Healthcare Technology Acquisitions Corp. Warrant
TrimTabs Donoghue Forlines Tactical High Yield ETF
Donnelley Financial Solutions Inc. Common Stock 
LGL Systems Acquisition Corp. Common Stock
TrimTabs Donoghue Forlines Risk Managed Innovation ETF
Flaherty & Crumrine Dynamic Preferred and Income Fund Inc. Common Stock
DFP Healthcare Acquisitions Corp. Class A Common Stock
DFP Healthcare Acquisitions Corp. Unit
DFP Healthcare Acquisitions Corp. Warrant
Discover Financial Services Common Stock
Dollar General Corporation Common Stock
Donegal Group Inc. Class A Common Stock
Donegal Group Inc. Class B Common Stock
Digi International Inc. Common Stock
Digital Ally Inc. Common Stock
Dragoneer Growth Opportunities Corp. Class A Ordinary Shares
Dragoneer Growth Opportunities Corp. II Class A Ordinary Shares
Quest Diagnostics Incorporated Common Stock
Diversified Healthcare Trust Common Shares of Beneficial Interest
Diversified Healthcare Trust 5.625% Senior Notes due 2042
Diversified Healthcare Trust 6.25% Senior Notes Due 2046
BNY Mellon High Yield Strategies Fund Common Stock
DiamondHead Holdings Corp. Unit
D.R. Horton Inc. Common Stock
Diamond Hill Investment Group Inc. Class A Common Stock
Danaher Corporation Common Stock
Danaher Corporation 4.75% Mandatory Convertible Preferred Stock Series A
Danaher Corporation 5.00% Mandatory Convertible Preferred Stock Series B
DHT Holdings Inc.
DHI Group Inc. Common Stock
Credit Suisse High Yield Bond Fund Common Stock
Nuveen Dow 30SM Dynamic Overwrite Fund Common Shares of Beneficial Interest
Dine Brands Global Inc. Common Stock
Diodes Incorporated Common Stock
Walt Disney Company (The) Common Stock
Discovery Inc. Series A Common Stock
Discovery Inc. Series B Common Stock
Discovery Inc. Series C Common Stock
DISH Network Corporation Class A Common Stock
AMCON Distributing Company Common Stock
FT Cboe Vest U.S. Equity Deep Buffer ETF - January
Daily Journal Corp. (S.C.) Common Stock
FT Cboe Vest U.S. Equity Deep Buffer ETF - July
FT Cboe Vest U.S. Equity Deep Buffer ETF - June
Delek US Holdings Inc. Common Stock
Delek Logistics Partners L.P. Common Units representing Limited Partner Interests
DraftKings Inc. Class A Common Stock
Dick's Sporting Goods Inc Common Stock
China Distance Education Holdings Limited American Depositary Shares
Delta Apparel Inc. Common Stock
Dolby Laboratories Common Stock
Deep Lake Capital Acquisition Corp. Unit
DLH Holdings Corp.
Dynagas LNG Partners LP Common Units
Dynagas LNG Partners LP 9.00% Series A Cumulative Redeemable Preferred Units
Dynagas LNG Partners LP 8.75% Series B Fixed to Floating Rate Cumulative Redeemable Perpetual Preferred Units liquidation preference $25.00 per Uni
Dolphin Entertainment Inc. Common Stock
Digital Realty Trust Inc. Common Stock
Digital Realty Trust Inc. 6.625% Series C Cumulative Redeemable Perpetual Preferred Stock
Digital Realty Trust Inc. 5.250% Series J Cumulative Redeemable Preferred Stock
Digital Realty Trust Inc. 5.850% Series K Cumulative Redeemable Preferred Stock par value $0.01 per share
Digital Realty Trust Inc. 5.200% Series L Cumulative Redeemable Preferred Stock
Duluth Holdings Inc. Class B Common Stock
Dollar Tree Inc. Common Stock
Deluxe Corporation Common Stock
DoubleLine Yield Opportunities Fund Common Shares of Beneficial Interest
Desktop Metal Inc. Class A Common Stock
DiaMedica Therapeutics Inc. Common Stock
FT Cboe Vest U.S. Equity Deep Buffer ETF - May
BNY Mellon Municipal Bond Infrastructure Fund Inc. Common Stock
BNY Mellon Municipal Income Inc. Common Stock
Dorchester Minerals L.P. Common Units Representing Limited Partnership Interests
Western Asset Mortgage Opportunity Fund Inc. Common Stock
Digimarc Corporation Common Stock
Digital Media Solutions Inc. Class A Ordinary Shares
DermTech Inc. Common Stock
dMY Technology Group Inc. II Class A Common Stock
dMY Technology Group Inc. III Class A Common Stock
Dun & Bradstreet Holdings Inc. Common Stock
Phoenix Tree Holdings Limited American Depositary Shares each representing ten (10) Class A ordinary shares
Denali Therapeutics Inc. Common Stock
Danimer Scientific Inc. Common Stock
Denison Mines Corp Ordinary Shares (Canada)
FT Cboe Vest U.S. Equity Deep Buffer ETF - November
NOW Inc. Common Stock
DNP Select Income Fund Inc. Common Stock
Physicians Realty Trust Common Shares of Beneficial Interest
FT Cboe Vest U.S. Equity Deep Buffer ETF - October
DocuSign Inc. Common Stock
Dogness (International) Corporation Class A Common Stock
Domo Inc. Class B Common Stock
BRP Inc. (Recreational Products) Common Subordinate Voting Shares
Masonite International Corporation Ordinary Shares (Canada)
Dorman Products Inc. Common Stock
Dover Corporation Common Stock
Dow Inc. Common Stock 
Amdocs Limited Ordinary Shares
DouYu International Holdings Limited ADS
Duff & Phelps Utility and Infrastructure Fund Inc.
Ault Global Holdings Inc. Common Stock
Domino's Pizza Inc Common Stock
DAQO New Energy Corp. American Depositary Shares each representing five ordinary shares
DRDGOLD Limited American Depositary Shares
Duke Realty Corporation Common Stock
Diamondrock Hospitality Company Common Stock
Diamondrock Hospitality Company 8.250% Series A Cumulative Redeemable Preferred Stock
Darden Restaurants Inc. Common Stock
DarioHealth Corp. Common Stock
DarioHealth Corp. Warrant
Dicerna Pharmaceuticals Inc. Common Stock
Dril-Quip Inc. Common Stock
DURECT Corporation Common Stock
DIRTT Environmental Solutions Ltd. Common Shares
Dominion Energy Inc. 2016 Series A 5.25% Enhanced Junior Subordinated Notes due 2076
Driven Brands Holdings Inc. Common Stock
Drive Shack Inc.
Drive Shack Inc. Preferred Series B
Drive Shack Inc. Preferred Series C
Drive Shack Inc. Pfd Ser D
Duddell Street Acquisition Corp. Class A Ordinary Shares
Duddell Street Acquisition Corp. Unit
Duddell Street Acquisition Corp. Warrant
Duff & Phelps Select MLP and Midstream Energy Fund Inc.
FT Cboe Vest U.S. Equity Deep Buffer ETF - September
Descartes Systems Group Inc. (The) Common Stock
Daseke Inc. Common Stock
Daseke Inc. Warrant
DoubleLine Income Solutions Fund Common Shares of Beneficial Interests
BNY Mellon Strategic Municipal Bond Fund Inc. Common Stock
Innovator Double Stacker ETF - October
Viant Technology Inc. Class A Common Stock
DSP Group Inc. Common Stock
Document Security Systems Inc. Common Stock
Diamond S Shipping Inc. Common Stock 
Blackrock Debt Strategies Fund Inc. Common Stock
Deswell Industries Inc. Common Shares
Diana Shipping inc. common stock
Diana Shipping Inc. Perpetual Preferred Shares Series B (Marshall Islands)
Dynatrace Inc. Common Stock
DTE Energy Company 2020 Series G 4.375% Junior Subordinated Debentures due 2080
DTE Energy Company Common Stock
DAVIDsTEA Inc. Common Stock
DTF Tax-Free Income Inc. Common Stock
Precision BioSciences Inc. Common Stock
DTE Energy Company 2016 Series B 5.375% Junior Subordinated Debentures due 2076
Brookfield DTLA Inc. 7.625% Series A Cumulative Redeemable Preferred Stock
DTE Energy Company 6.25% Corporate Units
Datasea Inc. Common Stock
DTE Energy Company 2017 Series E 5.25% Junior Subordinated Debentures due 2077
DTE Energy Company 2016 Series F 6.00% Junior Subordinated Debentures due 2076
Duff & Phelps Utility & Corporate Bond Trust Inc. Common Stock
Merlyn.AI SectorSurfer Momentum ETF
Duke Energy Corporation (Holding Company) Common Stock
Duke Energy Corporation Depositary Shares each representing a 1/1000th interest in a share of 5.75% Series A Cumulative Redeemable Perpetual Preferred Stock
Duke Energy Corporation 5.625% Junior Subordinated Debentures due 2078
Duke Energy Corporation 5.125% Junior Subordinated Debentures due 2073
Dune Acquisition Corporation Class A Common Stock
Dune Acquisition Corporation Unit
Dune Acquisition Corporation Warrant
Fangdd Network Group Ltd. American Depositary Shares
Duos Technologies Group Inc. Common Stock
DaVita Inc. Common Stock
Dynavax Technologies Corporation Common Stock
Dover Motorsports Inc. Common Stock
Devon Energy Corporation Common Stock
Delwinds Insurance Acquisition Corp. Class A Common Stock
Dawson Geophysical Company Common Stock
Dynex Capital Inc. Common Stock
Dynex Capital Inc. 6.900% Series C Fixed-to-Floating Rate Cumulative Redeemable Preferred Stock
DXC Technology Company Common Stock 
DexCom Inc. Common Stock
Dunxin Financial Holdings Limited American Depositary Shares
DXP Enterprises Inc. Common Stock
Daxor Corporation Common Stock
Dixie Group Inc. (The) Common Stock
Dycom Industries Inc. Common Stock
Dyadic International Inc. Common Stock
Angel Oak Dynamic Financial Strategies Income Term Trust Common Shares of Beneficial Interest
Dyne Therapeutics Inc. Common Stock
Dynatronics Corporation Common Stock
DZS Inc. Common Stock
ENI S.p.A. Common Stock
Electronic Arts Inc. Common Stock
Edify Acquisition Corp. Units
Wells Fargo Income Opportunities Fund Common Shares
GrafTech International Ltd. Common Stock
Entergy Arkansas LLC First Mortgage Bonds 4.875% Series Due September 1 2066
Eargo Inc. Common Stock
Ellington Residential Mortgage REIT Common Shares of Beneficial Interest
Auris Medical Holding Ltd. Common Shares 0.01 SF (Bermuda)
Eastside Distilling Inc. Common Stock
Brinker International Inc. Common Stock
Eventbrite Inc. Class A Common Stock
eBay Inc. Common Stock
eBay Inc. 6.0% Notes Due 2056
Eastern Bankshares Inc. Common Stock
Ennis Inc. Common Stock
Ebix Inc. Common Stock
Eagle Bancorp Montana Inc. Common Stock
Ebang International Holdings Inc. Class A Ordinary Shares
Centrais Electricas Brasileiras S A American Depositary Shares (Each representing one Common Share)
Emergent Biosolutions Inc. Common Stock
Meridian Bancorp Inc. Common Stock
Enterprise Bancorp Inc Common Stock
Ecopetrol S.A. American Depositary Shares
Eagle Point Credit Company Inc. Common Stock
Eagle Point Credit Company Inc. 7.75% Series B Term Preferred Stock due 2026
Eagle Point Credit Company Inc. 6.6875% Notes due 2028
Eagle Point Credit Company Inc. 6.75% Notes due 2027
Ellsworth Growth and Income Fund Ltd.
Ellsworth Growth and Income Fund Ltd. 5.25% Series A Cumulative Preferred Shares (Liquidation Preference $25.00 per share)
Echo Global Logistics Inc. Common Stock
Ecolab Inc. Common Stock
US Ecology Inc Common Stock
US Ecology Inc. Warrant
ChannelAdvisor Corporation Common Stock
electroCore Inc. Common Stock
Encore Capital Group Inc Common Stock
Consolidated Edison Inc. Common Stock
EDAP TMS S.A. American Depositary Shares
Morgan Stanley Emerging Markets Domestic Debt Fund Inc. Morgan Stanley Emerging Markets Domestic Debt Fund Inc. Common Stock
Stone Harbor Emerging Markets Income Fund Common Shares of Beneficial Interest
Stone Harbor Emerging Markets Total Income Fund Common Shares of Beneficial Interests
Editas Medicine Inc. Common Stock
Empresa Distribuidora Y Comercializadora Norte S.A. (Edenor) Empresa Distribuidora Y Comercializadora Norte S.A. (Edenor) American Depositary Shares
EuroDry Ltd. Common Shares 
Edesa Biotech Inc. Common Shares
Skillful Craftsman Education Technology Limited Ordinary Share
EdtechX Holdings Acquisition Corp. II Class A common stock
EdtechX Holdings Acquisition Corp. II Unit
EdtechX Holdings Acquisition Corp. II Warrant
New Oriental Education & Technology Group Inc. Sponsored ADR representing 1 Ordinary Share (Cayman Islands)
Educational Development Corporation Common Stock
The European Equity Fund Inc. Common Stock
Euronet Worldwide Inc. Common Stock
Emerald Holding Inc. Common Stock
Ellington Financial Inc. Common Stock 
Ellington Financial Inc. 6.750% Series A Fixed-to-Floating Rate Cumulative Redeemable Preferred Stock
Eaton vance Floating-Rate Income Plus Fund Common Shares of Beneficial Interest
Eaton Vance Floating-Rate 2022 Target Term Trust Common Shares of Beneficial Interest
Energy Focus Inc. Common Stock
Eaton Vance Senior Floating-Rate Fund Common Shares of Beneficial Interest
Enterprise Financial Services Corporation Common Stock
Eaton Vance Floating Rate Income Trust Common Shares of Beneficial Interest
Equifax Inc. Common Stock
eGain Corporation Common Stock
Eagle Bancorp Inc. Common Stock
Blackrock Enhanced Government Fund Inc. Common Stock
8x8 Inc Common Stock
2ndVote Society Defended ETF
Eagle Bulk Shipping Inc. Common Stock
Eldorado Gold Corporation Ordinary Shares
NIC Inc Common Stock
EastGroup Properties Inc. Common Stock
Eagle Pharmaceuticals Inc. Common Stock
VAALCO Energy Inc.  Common Stock
EHang Holdings Limited ADS
Encompass Health Corporation Common Stock
Western Asset Global High Income Fund Inc Common Stock
Eaton Vance 2021 Target Term Trust Common Shares of Beneficial Interest
eHealth Inc. Common Stock
Eagle Point Income Company Inc. Common Stock
Employers Holdings Inc Common Stock
Eiger BioPharmaceuticals Inc. Common Stock
Eaton Vance Municipal Bond Fund Common Shares of Beneficial Interest $.01 par value
Edison International Common Stock
Ekso Bionics Holdings Inc. Common Stock
Estee Lauder Companies Inc. (The) Common Stock
Envela Corporation Common Stock
Elanco Animal Health Incorporated Common Stock
Elanco Animal Health Incorporated 5.00% Tangible Equity Units
Entergy Louisiana Inc. Collateral Trust Mortgage Bonds 4.875 % Series due September 1 2066
Eledon Pharmaceuticals Inc. Common Stock
e.l.f. Beauty Inc. Common Stock
Ellomay Capital Ltd Ordinary Shares (Israel)
Electromed Inc. Common Stock
Eloxx Pharmaceuticals Inc. Common Stock
Companhia Paranaense de Energia (COPEL) Common Stock
Equity Lifestyle Properties Inc. Common Stock
Electro-Sensors Inc. Common Stock
Eltek Ltd. Ordinary Shares
Elevate Credit Inc. Common Stock
Callaway Golf Company Common Stock
Elys Game Technology Corp. Common Stock
eMagin Corporation Common Stock
Emclaire Financial Corp Common Stock
Western Asset Emerging Markets Debt Fund Inc Common Stock
EMCOR Group Inc. Common Stock
Templeton Emerging Markets Fund Common Stock
EMCORE Corporation Common Stock
Eastern Company (The) Common Stock
Eastman Chemical Company Common Stock
ClearBridge Energy Midstream Opportunity Fund Inc. Common Stock
Entergy Mississippi LLC First Mortgage Bonds 4.90% Series Due October 1 2066
Empower Ltd. Class A Ordinary Shares
Emerson Electric Company Common Stock
EMX Royalty Corporation Common Shares (Canada)
Enbridge Inc Common Stock
Enbridge Inc 6.375% Fixed-to-Floating Rate Subordinated Notes Series 2018-B due 2078
Enable Midstream Partners LP Common Units representing limited partner interests
Endo International plc Ordinary Shares
890 5th Avenue Partners Inc. Unit
ENGlobal Corporation Common Stock
Enel Americas S.A. American Depositary Shares
Enel Chile S.A. American Depositary Shares (Each representing 50 shares of Common Stock)
Entergy New Orleans LLC First Mortgage Bonds 5.0% Series due December 1 2052
EnLink Midstream LLC Common Units representing Limited Partner Interests
Enlivex Therapeutics Ltd. Ordinary Shares
ECP Environmental Growth Opportunities Corp. Unit
Entergy New Orleans LLC First Mortgage Bonds 5.50% Series due April 1 2066
Enochian Biosciences Inc. Common Stock
Executive Network Partnering Corporation Class A Common Stock
Enphase Energy Inc. Common Stock
Energizer Holdings Inc. Common Stock
Energizer Holdings Inc. 7.50% Series A Mandatory Convertible Preferred Stock
EnerSys Common Stock
The Ensign Group Inc. Common Stock
Enservco Corporation Common Stock
Enanta Pharmaceuticals Inc. Common Stock
Entegris Inc. Common Stock
Entera Bio Ltd. Ordinary Shares
Entera Bio Ltd. Warrant
Envestnet Inc Common Stock
Enova International Inc. Common Stock
Enveric Biosciences Inc. Common Stock
Environmental Impact Acquisition Corp. Unit
Eaton Vance New York Municipal Bond Fund Common Shares of Beneficial Interest $.01 par value
Enzo Biochem Inc. Common Stock ($0.01 Par Value)
Wells Fargo Global Dividend Opportunity Fund
EOG Resources Inc. Common Stock
Eaton Vance Enhance Equity Income Fund Eaton Vance Enhanced Equity Income Fund Shares of Beneficial Interest
Evolus Inc. Common Stock
Eaton Vance Enhance Equity Income Fund II Common Stock
Eos Energy Enterprises Inc. Class A Common Stock
Eos Energy Enterprises Inc. Warrant
Eaton Vance Municipal Income Trust EATON VANCE NATIONAL MUNICIPAL OPPORTUNITIES TRUST
El Paso Corporation Preferred Stock
Enerpac Tool Group Corp. Common Stock
EPAM Systems Inc. Common Stock
Bottomline Technologies Inc. Common Stock
Edgewell Personal Care Company Common Stock
Enterprise Products Partners L.P. Common Stock
Epiphany Technology Acquisition Corp. Unit
ESSA Pharma Inc. Common Stock
Evolution Petroleum Corporation Inc. Common Stock
EPR Properties Common Stock
EPR Properties 5.75% Series C Cumulative Convertible Preferred Shares
EPR Properties Series E Cumulative Conv Pfd Shs Ser E
EPR Properties 5.750% Series G Cumulative Redeemable Preferred Shares
Essential Properties Realty Trust Inc. Common Stock
Epsilon Energy Ltd. Common Share
Epizyme Inc. Common Stock
Equillium Inc. Common Stock
Equity Bancshares Inc. Class A Common Stock
Equity Commonwealth Common Shares of Beneficial Interest
Equity Commonwealth 6.50% Pfd Conv Shs Ser D
Equity Distribution Acquisition Corp. Class A Common Stock
Equitable Holdings Inc. Common Stock
Equitable Holdings Inc. Depositary Shares
Equitable Holdings Inc. Depositary Shares each representing a 1/1000th interest in a share of Fixed Rate Noncumulative Perpetual Preferred Stock Series C
Equinix Inc. Common Stock REIT
Equinor ASA
Diginex Limited Ordinary Shares
Diginex Limited Warrant
Equity Residential Common Shares of Beneficial Interest
Equus Total Return Inc. Common Stock
EQT Corporation Common Stock
Equinox Gold Corp. Common Shares
Wells Fargo Multi-Sector Income Fund Common Stock no par value
East Resources Acquisition Company Class A Common Stock
East Resources Acquisition Company Unit
East Resources Acquisition Company Warrant
Enerplus Corporation Common Stock
Wells Fargo Utilities and High Income Fund
Ericsson American Depositary Shares
Erie Indemnity Company Class A Common Stock
Energy Recovery Inc. Common Stock
Embraer S.A. Common Stock
Erytech Pharma S.A. American Depositary Shares
Eversource Energy (D/B/A) Common Stock
Elmira Savings Bank Elmira NY Common Stock
Escalade Incorporated Common Stock
ESCO Technologies Inc. Common Stock
Euroseas Ltd. Common Stock (Marshall Islands)
Eros STX Global Corporation A Ordinary Shares
Enstar Group Limited Ordinary Shares
Enstar Group Limited Depository Shares 7.00% Perpetual Non-Cumulative Preference Shares Series E
Enstar Group Limited Depositary Shares Each Representing 1/1000th of an interest in Preference Shares
Element Solutions Inc. Common Stock
Elbit Systems Ltd. Ordinary Shares
Essent Group Ltd. Common Shares
Espey Mfg. & Electronics Corp. Common Stock
Esperion Therapeutics Inc. Common Stock
Esquire Financial Holdings Inc. Common Stock
Empire State Realty Trust Inc. Class A Common Stock
Essex Property Trust Inc. Common Stock
ESSA Bancorp Inc. Common Stock
East Stone Acquisition Corporation Ordinary Shares
East Stone Acquisition Corporation Right
East Stone Acquisition Corporation Unit
East Stone Acquisition Corporation Warrant
Establishment Labs Holdings Inc. Common Shares
Elastic N.V. Ordinary Shares
Earthstone Energy Inc. Class A Common Stock
Community Bankers Trust Corporation Common Stock (VA)
Energy Transfer LP Common Units 
E.Merge Technology Acquisition Corp. Class A Common Stock
E.Merge Technology Acquisition Corp. Unit
E.Merge Technology Acquisition Corp. Warrant
Eaton Vance Tax-Managed Buy-Write Income Fund Eaton Vance Tax-Managed Buy-Write Income Fund Common Shares of Beneficial Interest
Eaton Vance Tax-Advantaged Global Dividend Income Fund Common Shares of Beneficial Interest
Ethan Allen Interiors Inc. Common Stock
Entergy Texas Inc 5.375% Series A Preferred Stock Cumulative No Par Value
Eaton Vance Risk-Managed Diversified Equity Income Fund Common Shares of Beneficial Interest
Entercom Communications Corp. Common Stock
Eaton Corporation PLC Ordinary Shares
89bio Inc. Common Stock
Eaton Vance Tax-Advantage Global Dividend Opp Common Stock
Eton Pharmaceuticals Inc. Common Stock
Energy Transfer Operating L.P. Series C Fixed-to-Floating Rate Cumulative Redeemable Perpetual Preferred Units
Energy Transfer Operating L.P. 7.625% Series D Fixed-to-Floating Rate Cumulative Redeemable Perpetual Preferred Units
Energy Transfer Operating L.P. Series E Fixed-to-Floating Rate Cumulative Redeemable Perpetual Preferred Units
Entergy Corporation Common Stock
Equitrans Midstream Corporation Common Stock 
Etsy Inc. Common Stock
Entasis Therapeutics Holdings Inc. Common Stock
Eaton Vance Corporation Eaton Vance Tax-Managed Buy-Write Opportunities Fund Common Shares of Beneficial Interest
Eaton Vance Corporation Eaton Vance Tax-Managed Global Buy-Write Opportunites Fund Common Shares of Beneficial Interest
E2open Parent Holdings Inc.Class A Common Stock
Eaton Vance Municipal Income 2028 Term Trust Common Shares of Beneficial Interest
Eaton Vance Tax-Managed Diversified Equity Income Fund Common Shares of Beneficial Interest
Euclid Capital Growth ETF
Eucrates Biomedical Acquisition Corp. Ordinary Shares
Eucrates Biomedical Acquisition Corp. Unit
Eucrates Biomedical Acquisition Corp. Warrant
Euronav NV Ordinary Shares
European Sustainable Growth Acquisition Corp. Unit
Eaton Vance Corporation Common Stock
Enviva Partners LP Common units representing limited partner interests
Evaxion Biotech A/S American Depositary Share
Everbridge Inc. Common Stock
Evans Bancorp Inc. Common Stock
Entravision Communications Corporation Common Stock
EverQuote Inc. Class A Common Stock
Eaton Vance Senior Income Trust Common Stock
Evofem Biosciences Inc. Common Stock
Eaton Vance Short Diversified Income Fund Eaton Vance Short Duration Diversified Income Fund Common Shares of Beneficial Interest
Evogene Ltd Ordinary Shares
Evolent Health Inc Class A Common Stock
EVI Industries Inc.  Common Stock
Ever-Glory International Group Inc. Common Stock
Evelo Biosciences Inc. Common Stock
Eaton Vance California Municipal Bond Fund Common Shares of Beneficial Interest $.01 par value
Eaton Vance Municipal Income Trust Common Stock
Evo Acquisition Corp. Unit
Evoke Pharma Inc. Common Stock
Evolving Systems Inc. Common Stock
EVO Payments Inc. Class A Common Stock
Evercore Inc. Class A Common Stock
Evergy Inc. Common Stock
Everi Holdings Inc. Common Stock
Eaton Vance Tax Advantaged Dividend Income Fund Common Shares of Beneficial Interest
Evertec Inc. Common Stock
Eaton Vance Limited Duration Income Fund Common Shares of Beneficial Interest
Eaton Vance New York Municipal Income Trust Shares of Beneficial Interest
Edwards Lifesciences Corporation Common Stock
East West Bancorp Inc. Common Stock
Exact Sciences Corporation Common Stock
Exelon Corporation Common Stock
Eaton Vance Tax-Managed Buy-Write Strategy Fund Common Shares of Beneficial Interest
Exelixis Inc. Common Stock
EXFO Inc
Eaton Vance Tax-Managed Global Diversified Equity Income Fund Eaton Vance Tax-Managed Global Diversified Equity Income Fund Common Shares of Beneficial Interest
Endeavour Silver Corporation Ordinary Shares (Canada)
ExlService Holdings Inc. Common Stock
Excellon Resources Inc. Common Shares
Eagle Materials Inc Common Stock
Experience Investment Corp. Class A Common Stock
Experience Investment Corp. Unit
Experience Investment Corp. Warrants
Expeditors International of Washington Inc. Common Stock
Expedia Group Inc. Common Stock
eXp World Holdings Inc. Common Stock
Exponent Inc. Common Stock
Express Inc. Common Stock
Extra Space Storage Inc Common Stock
Exterran Corporation Common Stock
Extreme Networks Inc. Common Stock
National Vision Holdings Inc. Common Stock
Eyegate Pharmaceuticals Inc. Common Stock
Eyenovia Inc. Common Stock
Second Sight Medical Products Inc. Common Stock
Second Sight Medical Products Inc. Warrants expiring 03/14/2024
EyePoint Pharmaceuticals Inc. Common Stock
EZGO Technologies Ltd. Ordinary Shares
EZCORP Inc. Class A Non Voting Common Stock
Ford Motor Company Common Stock
Ford Motor Company 6.20% Notes due June 1 2059
Ford Motor Company 6% Notes due December 1 2059
First American Corporation (New) Common Stock
Fortress Value Acquisition Corp. II Class A Common Stock
First Trust/Aberdeen Global Opportunity Income Fund First Trust/Aberdeen Global Opportunity Income Fund Common Shares of Beneficial Interest
Farmmi Inc. Ordinary Shares
Diamondback Energy Inc. Commmon Stock
Fanhua Inc. American Depositary Shares
Farmer Brothers Company Common Stock
FARO Technologies Inc. Common Stock
Fastenal Company Common Stock
FAT Brands Inc. Common Stock
FAT Brands Inc. 8.25% Series B Cumulative Preferred Stock
FAT Brands Inc. Warrant
Fate Therapeutics Inc. Common Stock
FT Cboe Vest U.S. Equity Buffer ETF - August
Aberdeen Asia-Pacific Income Fund Inc Common Stock
Facebook Inc. Class A Common Stock
Flagstar Bancorp Inc. Common Stock
Fortune Brands Home & Security Inc. Common Stock
Fortress Biotech Inc. Common Stock
Fortress Biotech Inc. 9.375% Series A Cumulative Redeemable Perpetual Preferred Stock
First Business Financial Services Inc. Common Stock
FB Financial Corporation Common Stock
First Bancshares Inc.
First Bancorp Common Stock
First BanCorp. New Common Stock
Forte Biosciences Inc. Common Stock
Fauquier Bankshares Inc. Common Stock
Franklin Covey Company Common Stock
Falcon Capital Acquisition Corp. Class A Common Stock
Falcon Capital Acquisition Corp. Unit
Falcon Capital Acquisition Corp. Warrant
First Capital Inc. Common Stock
First Community Bankshares Inc. (VA) Common Stock
First Choice Bancorp Common Stock
First Community Corporation Common Stock
1st Constitution Bancorp (NJ) Common Stock
FuelCell Energy Inc. Common Stock
First Commonwealth Financial Corporation Common Stock
FirstCash Inc. Common Stock
FTI Consulting Inc. Common Stock
First Citizens BancShares Inc. Class A Common Stock
First Citizens BancShares Inc. Depositary Shares
Aberdeen Global Income Fund Inc. Common Stock
Four Corners Property Trust Inc. Common Stock
First Eagle Alternative Capital BDC Inc. Common Stock
First Eagle Alternative Capital BDC Inc. 6.75% Notes due 2022
First Trust Senior Floating Rate Income Fund II Common Shares of Beneficial Interest
Freeport-McMoRan Inc. Common Stock
Fidelity D & D Bancorp Inc. Common Stock
FT Cboe Vest U.S. Equity Buffer ETF - December
First Trust Dynamic Europe Equity Income Fund Common Shares of Beneficial Interest
American Century Focused Dynamic Growth ETF
4D Molecular Therapeutics Inc. Common Stock
Fresh Del Monte Produce Inc. Common Stock
FactSet Research Systems Inc. Common Stock
Fidus Investment Corporation Common Stock
Fidus Investment Corporation 5.375% Notes Due 2024
Fidus Investment Corporation 6% Notes due 2024
FedEx Corporation Common Stock
FirstEnergy Corp. Common Stock
TrueShares Structured Outcome (February) ETF
Four Seasons Education (Cayman) Inc. American Depositary Shares each two ADSs representing one ordinary share
Emles Federal Contractors ETF
First Trust MLP and Energy Income Fund Common Shares of Beneficial Interest
Frequency Electronics Inc. Common Stock
Franklin Electric Co. Inc. Common Stock
First Trust Energy Income and Growth Fund
Fennec Pharmaceuticals Inc. Common Stock
Phoenix New Media Limited American Depositary Shares each representing 8 Class A ordinary shares.
First Trust/Aberdeen Emerging Opportunity Fund Common Shares of Beneficial Interest
Forum Energy Technologies Inc. Common Stock
FireEye Inc. Common Stock
FutureFuel Corp.  Common shares
First Trust Enhanced Equity Income Fund
First Financial Bancorp. Common Stock
FFBW Inc. Common Stock (MD)
Flaherty & Crumrine Preferred and Income Securities Fund Incorporated
FT Cboe Vest U.S. Equity Buffer ETF - February
FBL Financial Group Inc. Common Stock
Fuwei Films (Holdings) Co. Ltd. Ordinary Shares
Flushing Financial Corporation Common Stock
First Financial Bankshares Inc. Common Stock
F5 Networks Inc. Common Stock
First Financial Northwest Inc. Common Stock
First Foundation Inc. Common Stock
First Trust Specialty Finance and Financial Opportunities Fund
First Guaranty Bancshares Inc. Common Stock
FibroGen Inc Common Stock
FG Financial Group Inc. Common Stock
FG Financial Group Inc. 8.00% Cumulative Preferred Stock
FG New America Acquisition Corp. Class A Common Stock
Fidelity Growth Opportunities ETF
First Hawaiian Inc. Common Stock
Federated Hermes Inc. Common Stock
First Horizon Corporation Common Stock
First Horizon Corporation Depositary Shares
First Horizon Corporation Depositary Shares each representing a 1/400th interest in a share of Non-Cumulative Perpetual Preferred Stock Series B
First Horizon Corporation Depositary Shares each representing a 1/400th interest in a share of Non-Cumulative Perpetual Preferred Stock Series C
First Horizon Corporation Depositary Shares each representing a 1/400th interest in a share of Non-Cumulative Perpetual Preferred Stock Series D
First Horizon Corporation Depositary Shares each representing a 1/4000th interest in a share of Non-Cumulative Perpetual Preferred Stock Series E
Foghorn Therapeutics Inc. Common Stock
Frank's International N.V. Common Stock
First Interstate BancSystem Inc. Class A Common Stock
Fair Isaac Corproation Common Stock
First Trust Energy Infrastructure Fund Common Shares of Beneficial Interest
Forum Merger III Corporation Class A Common stock
Forum Merger III Corporation Units
Forum Merger III Corporation Warrant
Marlin Technology Corporation Unit
Angel Oak Financial Strategies Income Term Trust Common Shares of Beneficial Interest
FinVolution Group American Depositary Shares
Fidelity National Information Services Inc. Common Stock
Financial Institutions Inc. Common Stock
Fiserv Inc. Common Stock
Fifth Third Bancorp Common Stock
Fifth Third Bancorp Depositary Shares
Fifth Third Bancorp Depositary Shares each representing a 1/1000th ownership interest in a share of Non-Cumulative Perpetual Preferred Stock Series K
Fifth Third Bancorp Depositary Shares each representing 1/40th share of Fifth Third 6.00% Non-Cumulative Perpetual Class B Preferred Stock Series A
First Trust Senior Floating Rate 2022 Target Term Fund Common Shares of Beneficial Interest
Five Below Inc. Common Stock
Five9 Inc. Common Stock
Comfort Systems USA Inc. Common Stock
Homology Medicines Inc. Common Stock
National Beverage Corp. Common Stock
FT Cboe Vest U.S. Equity Buffer ETF - January
FT Cboe Vest U.S. Equity Buffer ETF - July
FT Cboe Vest U.S. Equity Buffer ETF - June
Foot Locker Inc.
Frazier Lifesciences Acquisition Corporation Class A Ordinary Shares
Frazier Lifesciences Acquisition Corporation Unit
Frazier Lifesciences Acquisition Corporation Warrant
Flaherty & Crumrine Total Return Fund Inc Common Stock
Fluidigm Corporation Common Stock
Flex Ltd. Ordinary Shares
Fulgent Genetics Inc. Common Stock
First of Long Island Corporation (The) Common Stock
FLIR Systems Inc. (DE) Common Stock
Full House Resorts Inc. Common Stock
Falcon Minerals Corporation Class A Common Stock
Falcon Minerals Corporation Warrant
FLEX LNG Ltd. Ordinary Shares
Fluent Inc. Common Stock
Flowers Foods Inc. Common Stock
SPX FLOW Inc. Common Stock
Fluor Corporation Common Stock
Flowserve Corporation Common Stock
FleetCor Technologies Inc. Common Stock
Flux Power Holdings Inc. Common Stock
American Century Focused Large Cap Value ETF
1-800-FLOWERS.COM Inc. Common Stock
Flexion Therapeutics Inc. Common Stock
Flexsteel Industries Inc. Common Stock
Fly Leasing Limited
FirstMark Horizon Acquisition Corp. Class A Common Stock
Fidelity Magellan ETF
Farmers & Merchants Bancorp Inc. Common Stock
FT Cboe Vest U.S. Equity Buffer ETF - May
First Mid Bancshares Inc. Common Stock
First Midwest Bancorp Inc. Common Stock
First Midwest Bancorp Inc. Depositary Shares Each Representing a 1/40th Interest in a Share of Fixed Rate Non-Cumulative Perpetual Preferred Stock Series C
First Midwest Bancorp Inc. Depositary Shares Each Representing a 1/40th Interest in a Share of Fixed Rate Non-Cumulative Perpetual Preferred Stock Series A
FMC Corporation Common Stock
Federated Hermes Premier Municipal Income Fund
Farmers National Banc Corp. Common Stock
Fiduciary/Claymore Energy Infrastructure Fund Common Shares of Beneficial Interest
Fresenius Medical Care AG Common Stock
Forma Therapeutics Holdings Inc. Common Stock
Fomento Economico Mexicano S.A.B. de C.V. Common Stock
First Trust Motgage Income Fund Common Shares of Beneficial Interest
Fabrinet Ordinary Shares
F.N.B. Corporation Common Stock
F.N.B. Corporation Depositary Shares each representing a 1/40th interest in a share of Fixed-to-Floating Rate Non-Cumulative Perpetual Preferred  Stock Series E
FNCB Bancorp Inc. Common Stock
Floor & Decor Holdings Inc. Common Stock
FNF Group of Fidelity National Financial Inc. Common Stock
FedNat Holding Company Common Stock
Funko Inc. Class A Common Stock
First Bancorp Inc  (ME) Common Stock
FT Cboe Vest U.S. Equity Buffer ETF - November
Franco-Nevada Corporation
First Northwest Bancorp Common Stock
Focus Financial Partners Inc. Class A Common Stock
FT Cboe Vest U.S. Equity Buffer ETF - October
Ferro Corporation Common Stock
Cohen & Steers Closed-End Opportunity Fund Inc. Common Stock
Amicus Therapeutics Inc. Common Stock
Fonar Corporation Common Stock
Forestar Group Inc Common Stock 
Forward Industries Inc. Common Stock
Foresight Acquisition Corp. Units
FormFactor Inc. FormFactor Inc. Common Stock
Forrester Research Inc. Common Stock
Formula Systems (1985) Ltd. American Depositary Shares
Fossil Group Inc. Common Stock
Shift4 Payments Inc. Class A Common Stock
Fox Corporation Class B Common Stock
Fox Corporation Class A Common Stock
Fox Factory Holding Corp. Common Stock
FoxWayne Enterprises Acquisition Corp. Unit
Far Peak Acquisition Corporation Class A Ordinary Shares
FlexShopper Inc. Common Stock
First Trust Intermediate Duration Preferred & Income Fund Common Shares of Beneficial Interest
Five Point Holdings LLC Class A Common Shares
Farmland Partners Inc. Common Stock
Farmland Partners Inc. Series B Participating Preferred Stock
First Trust New Opportunities MLP & Energy Fund Common Shares of Beneficial Interest
Fidelity Real Estate Investment ETF
Five Prime Therapeutics Inc. Common Stock
First Industrial Realty Trust Inc. Common Stock
Blackrock Floating Rate Income Strategies Fund Inc  Common Stock
Franklin Financial Services Corporation Common Stock
First Bank Common Stock
Republic First Bancorp Inc. Common Stock
FIRST REPUBLIC BANK Common Stock
FIRST REPUBLIC BANK Depositary Shares each representing a 1/40th interest in a share of 5.50% Noncumulative Perpetual Series G Preferred Stock
FIRST REPUBLIC BANK Depositary Shares each representing a 1/40th interest in a share of 5.125% Noncumulative Perpetual Series H Preferred Stock par value $0.01 per share
FIRST REPUBLIC BANK Depositary Shares each representing a 1/40th interest in a share of 5.50% Noncumulative Perpetual Series I Preferred Stock par value $0.01 per share
FIRST REPUBLIC BANK Depositary Shares Each Representing a 1/40th Interest in a Share of 4.70% Noncumulative Perpetual Series J Preferred Stock
FIRST REPUBLIC BANK Depositary Shares Each Representing a 1/40th Interest in a Share of 4.125% Noncumulative Perpetual Series K Preferred Stock
FIRST REPUBLIC BANK Depositary Shares Each Representing a 1/40th Interest in a Share of 4.250% Noncumulative Perpetual Series L Preferred Stock
Friedman Industries Inc. Common Stock
Whole Earth Brands Inc. Class A Common Stock
Whole Earth Brands Inc. Warrant
Frequency Therapeutics Inc. Common Stock
Franchise Group Inc. Common Stock
Franchise Group Inc. 7.50% Series A Cumulative Perpetual Preferred Stock
Fiesta Restaurant Group Inc. Common Stock
Freedom Holding Corp. Common Stock
Freeline Therapeutics Holdings plc American Depositary Shares
First Merchants Corporation Common Stock
Frontline Ltd. Ordinary Shares
JFrog Ltd. Ordinary Shares
FRP Holdings Inc. Common Stock
Freshpet Inc. Common Stock
Foresight Autonomous Holdings Ltd. American Depositary Shares
Federal Realty Investment Trust Common Stock
Federal Realty Investment Trust Depositary Shares each representing a 1/1000th interest in a 5.000% Series C Cumulative Redeemable Preferred Share
Forterra Inc. Common Stock
Forest Road Acquisition Corp. Class A Common Stock
FS Bancorp Inc. Common Stock
First Trust High Income Long Short Fund Common Shares of Beneficial Interest
First Seacoast Bancorp Common Stock
FT Cboe Vest U.S. Equity Buffer ETF - September
First Savings Financial Group Inc. Common Stock
Flexible Solutions International Inc. Common Stock (CDA)
FS Development Corp. II Class A Common Stock
FS KKR Capital Corp. Common Stock
FS KKR Capital Corp. II Common Stock
First Eagle Senior Loan Fund 
First Solar Inc. Common Stock
Fastly Inc. Class A Common Stock
Fortuna Silver Mines Inc Ordinary Shares (Canada)
Fidelity Small-Mid Cap Opportunities ETF
Franklin Street Properties Corp. Common Stock
Fisker Inc. Class A Common Stock
FinServ Acquisition Corp. Class A Common Stock
FinServ Acquisition Corp. Unit
FinServ Acquisition Corp. Warrant
FinServ Acquisition Corp. II Unit
Federal Signal Corporation Common Stock
Fortistar Sustainable Solutions Corp. Unit
FAST Acquisition Corp. Class A Common Stock
L.B. Foster Company Common Stock
F-star Therapeutics Inc. Common Stock
FirstService Corporation Common Shares
Franklin Universal Trust Common Stock
Fortress Transportation and Infrastructure Investors LLC Common Shares
Fortress Transportation and Infrastructure Investors LLC 8.25% Fixed to Floating Rate Series A Cumulative Perpetual Redeemable Preferred Shares
Fortress Transportation and Infrastructure Investors LLC 8.00% Fixed-to-Floating Rate Series B Cumulative Perpetual Redeemable Preferred Shares
Farfetch Limited Class A Ordinary Shares
FinTech Acquisition Corp. V Class A Common Stock
FinTech Acquisition Corp. V Unit
FinTech Acquisition Corp. V Warrant
frontdoor inc. Common Stock
Fuel Tech Inc. Common Stock
Franklin Limited Duration Income Trust Common Shares of Beneficial Interest
Future FinTech Group Inc. Common Stock
Fathom Holdings Inc. Common Stock
First Trust High Yield Opportunities 2027 Term Fund Common Stock
TechnipFMC plc Ordinary Share
FinTech Acquisition Corp. IV Class A Common Stock
FinTech Acquisition Corp. IV Unit
FinTech Acquisition Corp. IV Warrant
Flotek Industries Inc. Common Stock
Fortinet Inc. Common Stock
FTAC Olympus Acquisition Corp. Class A Ordinary Shares
FTAC Olympus Acquisition Corp. Unit
FTAC Olympus Acquisition Corp. Warrant
Fortis Inc. Common Shares
FTS International Inc. Class A Common Stock
Fortive Corporation Common Stock 
Fortive Corporation 5.00% Mandatory Convertible Preferred Stock Series A
fuboTV Inc. Common Stock
H. B. Fuller Company Common Stock
Fulcrum Therapeutics Inc. Common Stock
Fulton Financial Corporation Common Stock
Fulton Financial Corporation Depositary Shares Each Representing a 1/40th Interest in a Share of Fixed Rate Non-Cumulative Perpetual Preferred Stock Series A
Cedar Fair L.P. Common Stock
First United Corporation Common Stock
Sprott Focus Trust Inc. Common Stock
CornerCap Fundametrics Large-Cap ETF
Fury Gold Mines Limited Common Shares
First US Bancshares Inc. Common Stock
Fusion Acquisition Corp. Class A Common Stock
Fusion Pharmaceuticals Inc. Common Shares
Futu Holdings Limited American Depositary Shares
Arcimoto Inc. Common Stock
5:01 Acquisition Corp. Class A Common Stock
FVCBankcorp Inc. Common Stock
Five Star Senior Living Inc. Common Stock
Fiverr International Ltd. Ordinary Shares no par value
Fifth Wall Acquisition Corp. I Class A Common Stock
Liberty Media Corporation Series A Liberty Formula One Common Stock
Liberty Media Corporation Series C Liberty Formula One Common Stock
Forward Pharma A/S American Depositary Shares
Forward Air Corporation Common Stock
First National Corporation Common Stock
Genpact Limited Common Stock
Gabelli Equity Trust Inc. (The) Common Stock
Gabelli Equity Trust Inc. (The) Series G Cumulative Preferred Stock
Gabelli Equity Trust Inc. (The) Pfd Ser H
Gabelli Equity Trust Inc. (The) 5.45% Series J Cumulative Preferred Stock
Gabelli Equity Trust Inc. (The) 5.00% Series K Cumulative Preferred Stock
German American Bancorp Inc. Common Stock
Gaia Inc. Class A Common Stock
Gladstone Investment Corporation Business Development Company
Gladstone Investment Corporation 6.375% Series E Cumulative Term Preferred Stock due 2025
Gladstone Investment Corporation 6.25% Series D Cumulative Term Preferred Stock
Galectin Therapeutics Inc. Common Stock
General American Investors Inc. Common Stock
General American Investors Company Inc. Cumulative Preferred Stock
GAN Limited Ordinary Shares
StealthGas Inc. Common Stock
Gatos Silver Inc. Common Stock
GATX Corporation Common Stock
Galiano Gold Inc.
Global Blue Group Holding AG Ordinary Shares
Guggenheim Taxable Municipal Bond & Investment Grade Debt Trust Common Shares of Beneficial Interest
Glacier Bancorp Inc. Common Stock
Golub Capital BDC Inc. Common Stock
Generation Bio Co. Common Stock
Gamco Investors Inc. Common Stock
Global Indemnity Group LLC Class A Common Stock (DE)
Global Indemnity Group LLC 7.875% Subordinated Notes due 2047
Generations Bancorp NY Inc. Common Stock
Greenbox POS Common Stock
New Concept Energy Inc Common Stock
GBS Inc. Common Stock
Global Blood Therapeutics Inc. Common Stock
Greenbrier Companies Inc. (The) Common Stock
Growth Capital Acquisition Corp. Unit
Greene County Bancorp Inc. Common Stock
Gannett Co. Inc. Common Stock
GCM Grosvenor Inc. Class A Common Stock
GCM Grosvenor Inc. Warrant
Genesco Inc. Common Stock
GCP Applied Technologies Inc. Common Stock
Gabelli Convertible and Income Securities Fund Inc. (The) Common Stock
General Dynamics Corporation Common Stock
GoDaddy Inc. Class A Common Stock
Golden Entertainment Inc. Common Stock
GDL Fund The Common Shares of Beneficial Interest
The GDL Fund Series C Cumulative Puttable and Callable Preferred Shares
Western Asset Global Corporate Defined Opportunity Fund Inc. Western Asset Global Corporate Defined Opportunity Fund Inc.
Green Dot Corporation Class A Common Stock $0.001 par value
Goodrich Petroleum Corporation Common Stock
GoodRx Holdings Inc. Class A Common Stock
GDS Holdings Limited ADS
Gabelli Dividend & Income Trust Common Shares of Beneficial Interest
Gabelli Dividend 5.25% Series G Cumulative Preferred Shares par value $0.001 per share
The Gabelli Dividend & Income Trust 5.375% Series H Cumulative Preferred Shares
Grid Dynamics Holdings Inc. Class A Common Stock
Grid Dynamics Holdings Inc. Warrant
General Electric Company Common Stock
Great Elm Capital Corp. Common Stock
Great Elm Capital Corp. 6.50% Notes due 2022
Great Elm Capital Corp. 6.75% Notes Due 2025
Great Elm Capital Corp. 6.5% Notes due 2024
Greif Inc. Class A Common Stock
Great Elm Group Inc. Common Stock
Genesis Energy L.P. Common Units
Genesis Healthcare Inc. Common Stock
Gencor Industries Inc. Common Stock
Genetic Technologies Ltd  Sponsored ADR
Geo Group Inc (The) REIT
Geospace Technologies Corporation Common Stock (Texas)
Goldman Sachs MLP Energy Renaissance Fund
Geron Corporation Common Stock
Guess? Inc. Common Stock
Gevo Inc. Common Stock
New Germany Fund Inc. (The) Common Stock
Guaranty Federal Bancshares Inc. Common Stock
Griffon Corporation Common Stock
Gold Fields Limited American Depositary Shares
GFL Environmental Inc. Subordinate voting shares no par value
GFL Environmental Inc. Tangible Equity Units
General Finance Corporation General Finance Corporation Common Stock
General Finance Corporation Cumulative Redeemable Perpetual Preferred Series C
General Finance Corporation 7.875% Senior Notes due 2025
Golden Falcon Acquisition Corp. Class A Common Stock
Grupo Financiero Galicia S.A. American Depositary Shares
Gerdau S.A. Common Stock
Graco Inc. Common Stock
Guggenheim Credit Allocation Fund Common Shares of Beneficial Interest
GAMCO Global Gold Natural Resources & Income Trust
GAMCO Global Gold Natural Reources & Income Trust 5.00% Series B Cumulative 25.00 Liquidation Preference
The Gabelli Go Anywhere Trust Common Shares of Beneficial Interest
The Gabelli Go Anywhere Trust Series A Cumulative Puttable and Callable Preferred Shares
Gabelli Multi-Media Trust Inc. (The) Common Stock
Gabelli Multi-Media Trust Inc. (The) 5.125% Series E Cumulative Preferred Stock
Gabelli Multi-Media Trust Inc. (The) 5.125% Series G Cumulative Preferred Shares
Gabelli Global Small and Mid Cap Value Trust (The) Common Shares of Beneficial Interest
Gabelli Global Small and Mid Cap Value Trust (The) 5.450% Series A Cumulative Preferred Shares (Liquidation Preference $25.00 per share)
Guardant Health Inc. Common Stock
Gaming & Hospitality Acquisition Corp. Unit
Graham Holdings Company Common Stock
GreenTree Hospitality Group Ltd. American depositary shares each representing one Class A ordinary share
Greenhill & Co. Inc. Common Stock
Guild Holdings Company Class A Common Stock
Graham Corporation Common Stock
Guardion Health Sciences Inc. Common Stock
Gores Holdings VI Inc. Class A Common Stock
Gores Holdings VI Inc. Unit
Gores Holdings VI Inc. Warrant
PGIM Global High Yield Fund Inc.
CGI Inc. Common Stock
Gulf Island Fabrication Inc. Common Stock
GigCapital4 Inc. Unit
GigaMedia Limited Ordinary Shares
G-III Apparel Group LTD. Common Stock
GigCapital3 Inc. Common Stock
Gildan Activewear Inc. Class A Sub. Vot. Common Stock
Gilead Sciences Inc. Common Stock
Gilat Satellite Networks Ltd. Ordinary Shares
Templeton Global Income Fund Inc. Common Stock
General Mills Inc. Common Stock
GigCapital2 Inc. Common Stock
Synthetic Fixed-Income Securities Inc 6.375% (STRATS) Cl A-1
Synthetic Fixed-Income Securities Inc. Synthetic Fixed-Income Securities Inc. on behalf of STRATS(SM) Trust for Wal-Mart Stores Inc. Securities Series 2004-5
Synthetic Fixed-Income Securities Inc. Synthetic Fixed-Income Securities Inc. on behalf of STRATS (SM) Trust for Dominion Resources Inc. Securities Series 2005-6 Floating Rate Structured Repackaged Asset-Backed Trust Securities (STRATS) Certificates
Synthetic Fixed-Income Securities Inc. STRATS Trust for Procter&Gamble Securities Series 2006-1
Goldman Sachs Group Securities STRATS Trust for Goldman Sachs Group Securities Series 2006-2
Synthetic Fixed-Income Securities Inc. Synthetic Fixed-Income Securities Inc. Floating Rate Structured Repackaged Asset-Backed Trust Securities Certificates Series 2006-3
Glaukos Corporation Common Stock
Globe Life Inc. Common Stock
Globe Life Inc. 6.125% Junior Subordinated Debentures due 2056
Gladstone Capital Corporation Common Stock
Gladstone Capital Corporation 5.375% Notes due 2024
Globis Acquisition Corp. common stock
Globis Acquisition Corp. Unit
Globis Acquisition Corp. Warrant
Globus Maritime Limited Common Stock
Glen Burnie Bancorp Common Stock
Great Lakes Dredge & Dock Corporation Common Stock
GoldMining Inc. Common Shares
Galileo Acquisition Corp. Ordinary Shares
TD Holdings Inc. Common Stock
Galmed Pharmaceuticals Ltd. Ordinary Shares
Golar Lng Ltd
Clough Global Opportunities Fund Common Stock
Globant S.A. Common Shares
GasLog Ltd. Common Shares
GasLog LP. 8.75% Series A Cumulative Redeemable Perpetual Preference Shares
GasLog Partners LP Common Units representing limited partnership interests
GasLog Partners LP 8.625% Series A Cumulative Redeemable Perpetual Fixed to Floating Rate Preference Units
GasLog Partners LP 8.200% Series B Cumulative Redeemable Perpetual Fixed to Floating Rate Preference Units
GasLog Partners LP 8.500% Series C Cumulative Redeemable Perpetual Fixed to Floating Rate Preference Units
Global Partners LP Global Partners LP Common Units representing Limited Partner Interests
Global Partners LP 9.75% Series A Fixed-to-Floating Rate Cumulative Redeemable Perpetual Preferred Units representing limited partner interests
Galapagos NV American Depositary Shares
Gaming and Leisure Properties Inc. Common Stock
Clough Global Equity Fund Clough Global Equity Fund Common Shares of Beneficial Interest
Greenlight Capital Re Ltd. Class A Ordinary Shares
Greenwich LifeSciences Inc. Common Stock
Glatfelter Corporation Common Stock
Galecto Inc. Common Stock
Gabelli Global Utility Common Shares of Beneficial Ownership
The Gabelli Global Utility and Income Trust Series A Cumulative Puttable and Callable Preferred Shares
The Gabelli Global Utility and Income Trust Series B Cumulative Puttable and Callable Preferred Shares
Glu Mobile Inc. Common Stock
Clough Global Dividend and Income Fund Common Shares of beneficial interest
Corning Incorporated Common Stock
GlycoMimetics Inc. Common Stock
General Motors Company Common Stock
Genmab A/S ADS
Esports Entertainment Group Inc. Common Stock
Esports Entertainment Group Inc. Warrant
Queen's Gambit Growth Capital Unit
Gamida Cell Ltd. Ordinary Shares
GameStop Corporation Common Stock
Globus Medical Inc. Class A Common Stock
Gores Metropoulos II Inc. Unit
Golar LNG Partners LP Common Units Representing Limited Partnership
Golar LNG Partners LP 8.75% Series A Cumulative Redeemable Preferred Units
Global Medical REIT Inc. Common Stock
Global Medical REIT Inc. Series A Cumulative Redeemable Preferred Stock
GMS Inc. Common Stock
GATX Corporation 5.625% Senior Notes due 2066
Gemini Therapeutics Inc. Common Stock
Group Nine Acquisition Corp. Unit
Genocea Biosciences Inc. Common Stock
Genie Energy Ltd. Class B Common Stock Stock
Genie Energy Ltd. Series 2012 - A Preferred Stock $0.01 par value
GENFIT S.A. American Depositary Shares
Genco Shipping & Trading Limited Ordinary Shares New (Marshall Islands)
Global Net Lease Inc. Common Stock
Global Net Lease Inc. 7.25% Series A Cumulative Redeemable Preferred Stock $0.01 par value per share
Global Net Lease Inc. 6.875% Series B Cumulative Redeemable Perpetual Preferred Stock
Greenlane Holdings Inc. Class A Common Stock
GenMark Diagnostics Inc. Common Stock
Golden Nugget Online Gaming Inc. Class A Common Stock
Golden Nugget Online Gaming Inc. Warrant
Genesis Park Acquisition Corp. Class A Ordinary Shares
Genprex Inc. Common Stock
Generac Holdlings Inc. Common Stock
Greenrose Acquisition Corp. Common Stock
Greenrose Acquisition Corp. Unit
Greenrose Acquisition Corp. Warrant
Genasys Inc. Common Stock
GAMCO Natural Resources Gold & Income Trust
GAMCO Natural Resources Gold & Income Tust  5.20% Series A Cumulative Preferred Shares (Liquidation Preference $25.00 per share)
Gentex Corporation Common Stock
Guaranty Bancshares Inc. Common Stock
Genius Brands International Inc. Common Stock
Genworth Financial Inc Common Stock
Grocery Outlet Holding Corp. Common Stock
GO Acquisition Corp. Class A Common Stock
GoHealth Inc. Class A Common Stock
1847 Goedeker Inc. Commom Stock
Canoo Inc. Class A Common Stock
Canoo Inc. Warrant
Guggenheim Strategic Opportunities Fund Common Shares of Beneficial Interest
Golden Ocean Group Limited Common Stock
Gogo Inc. Common Stock
Gol Linhas Aereas Inteligentes S.A. Sponsored ADR representing 2 Pfd Shares
Barrick Gold Corporation Common Stock (BC)
Acushnet Holdings Corp. Common Stock
Gladstone Commercial Corporation Real Estate Investment Trust
Gladstone Commercial Corporation Series D Cumulative Redeemable Preferred Stock
Gladstone Commercial Corporation 6.625% Series E Cumulative Redeemable Preferred Stock
Alphabet Inc. Class C Capital Stock
Alphabet Inc. Class A Common Stock
Canada Goose Holdings Inc. Subordinate Voting Shares
Gold Resource Corporation Common Stock
Gossamer Bio Inc. Common Stock
GeoVax Labs Inc. Common Stock
GeoVax Labs Inc. Warrants
iShares 25  Year Treasury STRIPS Bond ETF
GreenPower Motor Company Inc. Common Shares
Global Partner Acquisition Corp II Unit
Genuine Parts Company Common Stock
Group 1 Automotive Inc. Common Stock
Georgia Power Company Series 2017A 5.00% Junior Subordinated Notes due October 1 2077
Graphic Packaging Holding Company
Great Panther Mining Limited Ordinary Shares (Canada)
Guggenheim Enhanced Equity Income Fund
Granite Point Mortgage Trust Inc. Common Stock
Global Payments Inc. Common Stock
Green Plains Partners LP Common Units
Green Plains Inc. Common Stock
Geopark Ltd Common Shares
GoPro Inc. Class A Common Stock
Gap Inc. (The) Common Stock
GP Strategies Corporation Common Stock
W.R. Grace & Co. Common Stock
Graybug Vision Inc. Common Stock
Green Brick Partners Inc. Common Stock
Gorman-Rupp Company (The) Common Stock
Gracell Biotechnologies Inc. American Depositary Shares
Greencity Acquisition Corporation Ordinary Shares
Greencity Acquisition Corporation Unit
Greencity Acquisition Corporation Warrants
Eagle Capital Growth Fund Inc. Common Stock
Grifols S.A. American Depositary Shares
Muscle Maker Inc Common Stock
Grindrod Shipping Holdings Ltd. Ordinary Shares
Garmin Ltd. Common Stock (Switzerland)
Greenpro Capital Corp. Common Stock
GreenVision Acquisition Corp Common stock
GreenVision Acquisition Corp Rights
GreenVision Acquisition Corp Unit 
GreenVision Acquisition Corp Warrant
U.S. Global Investors Inc. Class A Common Stock
Groupon Inc. Common Stock
Gores Holdings V Inc. Common stock
Gores Holdings V Inc. Unit
Gores Holdings V Inc. Warrant
Gritstone Oncology Inc. Common Stock
Galera Therapeutics Inc. Common Stock
GrubHub Inc. Common Stock
GRAVITY Co. Ltd. American Depository Shares
GrowGeneration Corp. Common Stock
The Gabelli Healthcare & Wellness Trust Common Shares of Beneficial Interest
Goldman Sachs Group Inc. (The) Common Stock
Goldman Sachs Group Inc. (The) Depositary Shares each representing 1/1000th Interest in a Share of Floating Rate Non-Cumulative Preferred Stock Series A
Goldman Sachs Group Inc. (The) Depositary Share repstg 1/1000th Preferred Series C
Goldman Sachs Group Inc. (The) Dep Shs repstg 1/1000 Pfd Ser D Fltg
Goldman Sachs Group Inc Depositary Shs Repstg 1/1000th Pfd Ser J Fixed to Fltg Rate
Goldman Sachs Group Inc. (The) Dep Shs Repstg 1/1000 Int Sh Fxd/Fltg Non Cum Pfd Stk Ser K
Goldman Sachs Group Inc. (The) Depositary Shares Each Representing 1/1000th Interest in a Share of 6.30% Non-Cumulative Preferred Stock Series N
GS Acquisition Holdings Corp II Class A Common Stock
Global Synergy Acquisition Corp. Units
Globalstar Inc. Common Stock
Great Southern Bancorp Inc. Common Stock
Goldman Sachs BDC Inc. Common Stock
Goldman Sachs MarketBeta Emerging Markets Equity ETF
Goosehead Insurance Inc. Class A Common Stock
Goldman Sachs MarketBeta International Equity ETF
GSI Technology Common Stock
GlaxoSmithKline PLC Common Stock
GreenSky Inc. Class A Common Stock
Global Ship Lease Inc New Class A Common Shares
Global Ship Lease Inc. Depository Shares Representing 1/100th Perpetual Preferred Series B% (Marshall Island)
Global Ship Lease Inc. 8.00% Senior Notes due 2024
Ferroglobe PLC Ordinary Shares
Glory Star New Media Group Holdings Limited Ordinary Share
Glory Star New Media Group Holdings Limited Warrant expiring 2/13/2025
Golden Star Resources Ltd Common Stock
Gridsum Holding Inc. American Depositary Shares
Goldman Sachs MarketBeta U.S. Equity ETF
Gold Standard Ventures Corporation Common Stock (Canada)
GSX Techedu Inc. American Depositary Shares three of which representing two Class A Ordinary Shares
The Goodyear Tire & Rubber Company Common Stock
GT Biopharma Inc. Common Stock
Gran Tierra Energy Inc. Common Stock
Greenland Technologies Holding Corporation Ordinary Shares
Gates Industrial Corporation plc Ordinary Shares
Genetron Holdings Limited ADS
G1 Therapeutics Inc. Common Stock
Good Times Restaurants Inc. Common Stock
Goldman Sachs Access Inflation Protected USD Bond ETF
Chart Industries Inc. Common Stock
Gray Television Inc. Common Stock
Triple-S Management Corporation Class B Common Stock
GTT Communications Inc. Common Stock
Getty Realty Corporation Common Stock
GTY Technology Holdings Inc. Common Stock
Gulf Resources Inc. (NV) Common Stock
Gabelli Utility Trust (The) Common Stock
Gabelli Utility Trust (The) 5.625% Series A Cumulative Preferred Shares
Gabelli Utility Trust (The) 5.375% Series C Cumulative Preferred Shares
Granite Construction Incorporated Common Stock
GSE Systems Inc. Common Stock
Good Works Acquisition Corp. Common Stock
Good Works Acquisition Corp. Warrant
Great Western Bancorp Inc. Common Stock
GWG Holdings Inc Common Stock
GW Pharmaceuticals Plc American Depositary Shares
Guidewire Software Inc. Common Stock
Global Water Resources Inc. Common Stock
W.W. Grainger Inc. Common Stock
GX Acquisiton Corp. Class A Common Stock
GX Acquisiton Corp. Unit
GX Acquisiton Corp. Warrant
Gyrodyne LLC Common Stock
Hyatt Hotels Corporation Class A Common Stock
Hawaiian Holdings Inc. Common Stock
Health Assurance Acquisition Corp. Class A Common Stock
Health Assurance Acquisition Corp. SAIL Securities
Health Assurance Acquisition Corp. Warrants
Haemonetics Corporation Common Stock
Hanmi Financial Corporation Common Stock
Hain Celestial Group Inc. (The) Common Stock
Halliburton Company Common Stock
Hallmark Financial Services Inc. Common Stock
Halozyme Therapeutics Inc. Common Stock
Happiness Biotech Group Limited Ordinary Shares
Harpoon Therapeutics Inc. Common Stock
Hasbro Inc. Common Stock
Hannon Armstrong Sustainable Infrastructure Capital Inc. Common Stock
Haynes International Inc. Common Stock
Huntington Bancshares Incorporated Common Stock
Huntington Bancshares Incorporated Depositary Shares each representing a 1/40th interest in a share of 5.875% Series C Non-Cumulative Perpetual Preferred Stock
Huntington Bancshares Incorporated Depositary Shares
Hamilton Beach Brands Holding Company Class A Common Stock 
Home Bancorp Inc. Common Stock
Hanesbrands Inc. Common Stock
Harvard Bioscience Inc. Common Stock
Hudbay Minerals Inc. Ordinary Shares (Canada)
Howard Bancorp Inc. Common Stock
Horizon Bancorp Inc. Common Stock
Huttig Building Products Inc. Common Stock
HBT Financial Inc. Common Stock
HCA Healthcare Inc. Common Stock
Harvest Capital Credit Corporation Common Stock
Harvest Capital Credit Corporation 6.125% Notes due 2022
HealthCor Catalio Acquisition Corp. Class A Ordinary Shares
Healthcare Services Acquisition Corporation Class A Common Stock
Healthcare Services Acquisition Corporation Unit
Healthcare Services Acquisition Corporation Warrant
Health Catalyst Inc Common Stock
Warrior Met Coal Inc. Common Stock
Healthcare Capital Corp. Unit
Heritage-Crystal Clean Inc. Common Stock
Harbor Custom Development Inc. Common Stock
HC2 Holdings Inc. Common Stock
HCI Group Inc. Common Stock
Hennessy Capital Investment Corp. V Units 
Hudson Executive Investment Corp. II Unit
Hackett Group Inc (The). Common Stock
Hutchison China MediTech Limited American Depositary Shares
Healthcare Services Group Inc. Common Stock
Hercules Capital Inc. 6.25% Notes due 2033
Hercules Capital Inc. 5.25% Notes due 2025
Home Depot Inc. (The) Common Stock
HDFC Bank Limited Common Stock
Hudson Technologies Inc. Common Stock
Hawaiian Electric Industries Inc. Common Stock
Turtle Beach Corporation Common Stock
Hudson Executive Investment Corp. Class A Common Stock
Hudson Executive Investment Corp. Units
Hudson Executive Investment Corp. Warrant
H&E Equipment Services Inc. Common Stock
Swan Hedged Equity US Large Cap ETF
Heico Corporation Common Stock
Heico Corporation
Helen of Troy Limited Common Stock
Franklin Genomic Advancements ETF
Holly Energy Partners L.P. Common Stock
Hepion Pharmaceuticals Inc. Common Stock
John Hancock Hedged Equity & Income Fund Common Shares of Beneficial Interest
Hess Corporation Common Stock
Hess Midstream LP Class A Share
HEXO Corp. Common Shares
Home Federal Bancorp Inc. of Louisiana Common StocK
HollyFrontier Corporation Common Stock
HF Foods Group Inc. Common Stock
Highland Income Fund
Highland Income Fund 5.375% Series A Cumulative Preferred Shares
Heritage Financial Corporation Common Stock
Heritage Global Inc. Common Stock
Humanigen Inc. Common Stock
Hartford Financial Services Group Inc. (The) 7.875% Fixed to Floating Rate Junior Subordinated Debentures due 2042
Highland Global Allocation Fund Common Stock
China HGS Real Estate Inc. Common Stock
Hilton Grand Vacations Inc. Common Stock 
Howard Hughes Corporation (The) Common Stock
HeadHunter Group PLC American Depositary Shares
Hillenbrand Inc Common Stock
Hibbett Sports Inc. Common Stock
Miller/Howard High Income Equity Fund Common Shares of Beneficial Interest
Hingham Institution for Savings Common Stock
Hartford Financial Services Group Inc. (The) Common Stock
Hartford Financial Services Group Inc. (The) Depositary Shares each representing a 1/1000th interest in a share of 6.000% Non-Cumulative Preferred Stock Series G $0.01 par value
H.I.G. Acquisition Corp. Class A Ordinary Shares
Highway Holdings Limited Common Stock
Huntington Ingalls Industries Inc. Common Stock
Hill International Inc. Common Stock
Hims & Hers Health Inc. Class A Common Stock
Himax Technologies Inc. American Depositary Shares
Western Asset High Income Opportunity Fund Inc. Common Stock
Highwoods Properties Inc. Common Stock
Western Asset High Income Fund II Inc. Common Stock
Hancock Jaffe Laboratories Inc. Common Stock
Hancock Jaffe Laboratories Inc. Warrants
AMTD International Inc. American Depositary Shares each representing one Class A Ordinary Share
Hecla Mining Company Common Stock
Hecla Mining Company Preferred Stock
Hamilton Lane Alliance Holdings I Inc. Unit
Herbalife Nutrition Ltd. Common Stock
Hailiang Education Group Inc. American Depositary Shares
Houlihan Lokey Inc. Class A Common Stock
Helios Technologies Inc. Common Stock
Harmonic Inc. Common Stock
Hillman Group Capital Trust Preferred Stock
Hamilton Lane Incorporated Class A Common Stock
Hilton Worldwide Holdings Inc. Common Stock 
Helix Energy Solutions Group Inc. Common Stock
Helix Acquisition Corp. Class A Ordinary Shares
Honda Motor Company Ltd. Common Stock
HumanCo Acquisition Corp. Class A Common Stock
HumanCo Acquisition Corp. Unit
HumanCo Acquisition Corp. Warrant
HMG/Courtland Properties Inc. Common Stock
Houghton Mifflin Harcourt Company Common Stock
Huami Corporation American Depositary Shares each representing four Class A Ordinary Shares
Hoegh LNG Partners LP Common Units representing Limited Partner Interests
Hoegh LNG Partners LP 8.75% Series A Cumulative Redeemable Preferred Units
Horace Mann Educators Corporation Common Stock
HMN Financial Inc. Common Stock
Home Point Capital Inc Common Stock
HomeStreet Inc. Common Stock
HMS Holdings Corp (DE)
Hemisphere Media Group Inc. Class A Common Stock
Harmony Gold Mining Company Limited
Hanger Inc. Common Stock
HNI Corporation Common Stock
Hennessy Advisors Inc. Common Stock
Huaneng Power Intl Common Stock
Hallador Energy Company Common Stock
Pioneer Diversified High Income Trust Pioneer Diversified High Income Trust Common Shares of Beneficial Interest
Hooker Furniture Corporation Common Stock
Hall of Fame Resort & Entertainment Company Common Stock
Hall of Fame Resort &amp; Entertainment Company Warrant
Harley-Davidson Inc. Common Stock
Holicity Inc. Class A Common Stock
Hollysys Automation Technologies Ltd. Common Shares (British Virgin Islands)
Holicity Inc. Unit
Holicity Inc. Warrant
Hologic Inc. Common Stock
Home BancShares Inc. Common Stock
At Home Group Inc. Common Stock
Honeywell International Inc. Common Stock
HarborOne Bancorp Inc. Common Stock
HOOKIPA Pharma Inc. Common Stock
Hope Bancorp Inc. Common Stock
Hoth Therapeutics Inc. Common Stock
Hovnanian Enterprises Inc. Class A Common Stock
Hovnanian Enterprises Inc Dep Shr Srs A Pfd
Helmerich & Payne Inc. Common Stock
Hewlett Packard Enterprise Company Common Stock
John Hancock Pfd Income Fund II Pfd Income Fund II
John Hancock Preferred Income Fund Common Shares of Beneficial Interest
HighPeak Energy Inc. Common Stock
HighPeak Energy Inc. Warrant
Hudson Pacific Properties Inc. Common Stock
HP Inc. Common Stock
HighPoint Resources Corporation Common Stock
John Hancock Preferred Income Fund III Preferred Income Fund III
HPX Corp. Class A Ordinary Shares
Tekla Healthcare Investors Common Stock
HireQuest Inc. Common Stock (DE)
TeklaLife Sciences Investors Common Stock
HealthEquity Inc. Common Stock
Healthcare Realty Trust Incorporated Common Stock
H&R Block Inc. Common Stock
Hill-Rom Holdings Inc Common Stock
Herc Holdings Inc. Common Stock 
Hormel Foods Corporation Common Stock
Harmony Biosciences Holdings Inc. Common Stock
Harrow Health Inc. Common Stock
Heritage Insurance Holdings Inc. Common Stock
Heron Therapeutics Inc. Common Stock
Horizon Technology Finance Corporation Common Stock
Health Sciences Acquisitions Corporation 2 Ordinary Shares
HSBC Holdings plc. Common Stock
Harsco Corporation Common Stock
Helius Medical Technologies Inc. Class A Common Stock (DE)
Henry Schein Inc. Common Stock
Heidrick & Struggles International Inc. Common Stock
Heska Corporation Common Stock
Hudson Global Inc. Common Stock
Host Hotels & Resorts Inc. Common Stock
HealthStream Inc. Common Stock
Histogen Inc. Common Stock
The Hershey Company Common Stock
Hersha Hospitality Trust Class A Common Shares of Beneficial Interest
Hersha Hospitality Trust 6.875% Series C Cumulative Redeemable Preferred Shares of Beneficial Interest
Hersha Hospitality Trust 6.50% Series D Cumulative Redeemable Preferred Shares of Beneficial Interest $0.01 par value per share
Hersha Hospitality Trust 6.50% Series E Cumulative Redeemable Preferred Shares of Beneficial Interest
Healthcare Trust of America Inc. Class A Common Stock
HomeTrust Bancshares Inc. Common Stock
Heritage Commerce Corp Common Stock
Heat Biologics Inc. Common Stock
John Hancock Tax Advantaged Dividend Income Fund Common Shares of Beneficial Interest
Horizon Technology Finance Corporation 6.25% Notes due 2022
Hercules Capital Inc. Common Stock
HTG Molecular Diagnostics Inc. Common Stock
Hilltop Holdings Inc.
Huazhu Group Limited American Depositary Shares
Healthcare Trust Inc. 7.375% Series A Cumulative Redeemable Perpetual Preferred Stock
Heartland Express Inc. Common Stock
Heartland Financial USA Inc. Common Stock
Heartland Financial USA Inc. Depositary Shares each representing a 1/400th ownership interest in a share of 7.00% Fixed-Rate Reset Non-Cumulative Perpetual Preferred Stock Series E
Fusion Fuel Green PLC Class A Ordinary Shares
Fusion Fuel Green PLC Warrant
Highland Transcend Partners I Corp. Class A Ordinary Shares
John Hancock Tax-Advantaged Global Shareholder Yield Fund Common Shares of Beneficial Interest
Hubbell Inc Common Stock
Hub Group Inc. Class A Common Stock
HubSpot Inc. Common Stock
Huadi International Group Co. Ltd. Ordinary Shares
FSD Pharma Inc. Class B Subordinate Voting Shares
Huize Holding Limited American Depositary Shares
Humana Inc. Common Stock
Huntsman Corporation Common Stock
Hurco Companies Inc. Common Stock
Huron Consulting Group Inc. Common Stock
Houston American Energy Corporation Common Stock
Hudson Capital Inc. Ordinary Shares
HUYA Inc. American depositary shares each  representing one Class A ordinary share
HV Bancorp Inc. Common Stock
Haverty Furniture Companies Inc. Common Stock
Haverty Furniture Companies Inc.
Hawthorn Bancshares Inc. Common Stock
Hancock Whitney Corporation Common Stock
Houston Wire & Cable Company Common Stock
Hancock Whitney Corporation 5.95% Subordinated Notes due 2045
Hancock Whitney Corporation 6.25% Subordinated Notes due 2060
Hawkins Inc. Common Stock
Howmet Aerospace Inc. Common Stock
Howmet Aerospace Inc. $3.75 Preferred Stock
Xiaobai Maimai Inc. ADR
Hexcel Corporation Common Stock
Hyster-Yale Materials Handling Inc. Class A Common Stock
New America High Income Fund Inc. (The) Common Stock
Hydrofarm Holdings Group Inc. Common Stock
Western Asset High Yield Defined Opportunity Fund Inc. Common Stock
Hyliion Holdings Corp. Class A Common Stock
Hycroft Mining Holding Corporation Class A Common Stock
Hycroft Mining Holding Corporation Warrants
Hycroft Mining Holding Corporation  Warrant
Hycroft Mining Holding Corporation Warrant
HyreCar Inc. Common Stock
Blackrock Corporate High Yield Fund Inc. Common Stock
Horizon Acquisition Corporation Class A Ordinary Shares
Horizon Global Corporation Common Shares
Horizon Therapeutics Public Limited Company Ordinary Shares
MarineMax Inc.  (FL) Common Stock
Horizon Acquisition Corporation II Class A Ordinary Shares
IAA Inc. Common Stock 
IAC/InterActiveCorp Common Stock
ION Acquisition Corp 1 Ltd. Class A Ordinary Shares
Voya Asia Pacific High Dividend Equity Income Fund ING Asia Pacific High Dividend Equity Income Fund Common Shares of Beneficial Interest
Aberdeen Australia Equity Fund Inc Common Stock
Iamgold Corporation Ordinary Shares
Integra LifeSciences Holdings Corporation Common Stock
Industrias Bachoco S.A.B. de C.V. Common Stock
Independent Bank Corporation Common Stock
IBEX Limited Common Shares
iShares iBonds 2026 Term High Yield and Income ETF
iBio Inc. Common Stock
Interactive Brokers Group Inc. Class A Common Stock
International Business Machines Corporation Common Stock
ICICI Bank Limited Common Stock
International Bancshares Corporation Common Stock
Installed Building Products Inc. Common Stock
Independent Bank Group Inc Common Stock
iCAD Inc. Common Stock
County Bancorp Inc. Common Stock
ImmuCell Corporation Common Stock
ICC Holdings Inc. Common Stock
Independence Contract Drilling Inc. Common Stock
Intercontinental Exchange Inc. Common Stock
ICF International Inc. Common Stock
Ichor Holdings Ordinary Shares
ICL Group Ltd. Ordinary Shares
iClick Interactive Asia Group Limited American Depositary Shares
ICON plc Ordinary Shares
Investcorp Credit Management BDC Inc. Common Stock
Iconix Brand Group Inc. Common Stock
Intercept Pharmaceuticals Inc. Common Stock
ICU Medical Inc. Common Stock
PARTS iD Inc. Class A Common Stock
IDACORP Inc. Common Stock
InterDigital Inc. Common Stock
Voya Infrastructure Industrials and Materials Fund Common Shares of Beneficial Interest
Ideanomics Inc. Common Stock
Intellicheck Inc. Common Stock
Idera Pharmaceuticals Inc. Common Stock
IDT Corporation Class B Common Stock
Interpace Biosciences Inc. Common Stock
IDEXX Laboratories Inc. Common Stock
IDEAYA Biosciences Inc. Common Stock
Infrastructure and Energy Alternatives Inc. Common Stock
Infrastructure and Energy Alternatives Inc. Warrant
IEC Electronics Corp. Common Stock
Icahn Enterprises L.P. Common Stock
IES Holdings Inc. Common Stock
IDEX Corporation Common Stock
Internationa Flavors & Fragrances Inc. Common Stock
International Flavors & Fragrances Inc. 6.00% Tangible Equity Units
iFresh Inc. Common Stock
India Fund Inc. (The) Common Stock
InflaRx N.V. Common Stock
Intercorp Financial Services Inc. Common Shares
Voya Global Advantage and Premium Opportunity Fund Common Shares of Beneficial Interest
IG Acquisition Corp. Class A Common Stock
IG Acquisition Corp. Unit
IG Acquisition Corp. Warrant
India Globalization Capital Inc. Common Stock
Voya Global Equity Dividend and Premium Opportunity Fund
Western Asset Investment Grade Defined Opportunity Trust Inc. Common Stock
International General Insurance Holdings Ltd. Ordinary Share
International General Insurance Holdings Ltd. Warrants expiring 03/17/2025
IGM Biosciences Inc. Common Stock
Ignyte Acquisition Corp. Unit
CBRE Clarion Global Real Estate Income Fund Common Stock
International Game Technology Ordinary Shares
iHuman Inc. American depositary shares each representing five Class A ordinary shares
Independence Holding Company Common Stock
Voya Emerging Markets High Income Dividend Equity Fund Common Shares
Intercontinental Hotels Group American Depositary Shares (Each representing one Ordinary Share)
Invesco High Income 2023 Target Term Fund Common Shares of Beneficial Interest
iHeartMedia Inc. Class A Common Stock
InnSuites Hospitality Trust Shares of Beneficial Interest
Invesco High Income 2024 Target Term Fund Common Shares of Beneficial Interest No par value per share
Investindustrial Acquisition Corp. Class A Ordinary Shares
Voya International High Dividend Equity Income Fund Common Shares of Beneficial Interest
Morgan Stanley India Investment Fund Inc. Common Stock
Information Services Group Inc. Information Services Group Inc. Common Stock
INSU Acquisition Corp. III Class A Common Stock
INSU Acquisition Corp. III Unit
INSU Acquisition Corp. III Warrant
Insteel Industries Inc. Common Stock
i3 Verticals Inc. Class A Common Stock
Invesco Value Municipal Income Trust Common Stock
Intricon Corporation Common Stock
Innovative Industrial Properties Inc. Common Stock
Innovative Industrial Properties Inc. 9.00% Series A Cumulative Redeemable Preferred Stock
II-VI Incorporated Common Stock
II-VI Incorporated 6.00% Series A Mandatory Convertible Preferred Stock
Ikonics Corporation
Inhibikase Therapeutics Inc. Common Stock
Illumina Inc. Common Stock
Industrial Logistics Properties Trust Common Shares of Beneficial Interest
I-MAB American Depositary Shares
IMAC Holdings Inc. Common Stock
IMAC Holdings Inc. Warrant
Imax Corporation Common Stock
iMedia Brands Inc. Class A Common Stock
Immunocore Holdings plc American Depositary Shares
ImmunoGen Inc. Common Stock
Impac Mortgage Holdings Inc. Common Stock 
Ingles Markets Incorporated Class A Common Stock
Immutep Limited American Depositary Shares
Immersion Corporation Common Stock
Immunome Inc. Common Stock
Imperial Oil Limited Common Stock
ChipMOS TECHNOLOGIES INC. American Depositary Shares
AEA-Bridges Impact Corp. Class A Ordinary Shares
IMARA Inc. Common Stock
Immuron Limited American Depositary Shares
Immuron Limited Warrants
Integrated Media Technology Limited Ordinary Shares
Immatics N.V. Ordinary Shares
Immatics N.V. Warrants
Immunic Inc. Common Stock
IMV Inc. Common Shares
Immunovant Inc. Common Stock
International Money Express Inc. Common Stock
First Internet Bancorp Common Stock
First Internet Bancorp 6.0% Fixed-to-Floating Rate Subordinated Notes due 2026
First Internet Bancorp 6.0% Fixed-to-Floating Rate Subordinated Notes Due 2029
Inhibrx Inc. Common Stock
Incyte Corp. Common Stock
Independent Bank Corp. Common Stock
Indonesia Energy Corporation Limited Ordinary Shares
INDUS Realty Trust Inc. (MD) Common Stock
Infinity Pharmaceuticals Inc. Common Stock
Infinera Corporation Common Stock
IHS Markit Ltd. Common Shares
InfuSystems Holdings Inc. Common Stock
Infosys Limited American Depositary Shares
ING Group N.V. Common Stock
Inogen Inc Common Stock
Ingredion Incorporated Common Stock
KludeIn I Acquisition Corp. Unit
InMed Pharmaceuticals Inc. Common Shares
INmune Bio Inc. Common stock
InMode Ltd. Ordinary Shares
Summit Hotel Properties Inc. Common Stock
Summit Hotel Properties Inc. 6.45% Series D Cumulative Redeemable Preferred Stock
Summit Hotel Properties Inc. 6.250% Series E Cumulative Redeemable Preferred Stock
Inovio Pharmaceuticals Inc. Common Stock
Innodata Inc. Common Stock
Inovalon Holdings Inc. Class A Common Stock
Inpixon Common Stock
Intelligent Systems Corporation Common Stock
Inspired Entertainment Inc. Common Stock
Inseego Corp. Common Stock
Insight Select Income Fund
Insmed Inc. Common Stock
Inspire Medical Systems Inc. Common Stock
International Seaways Inc. Common Stock 
International Seaways Inc. 8.50% Senior Notes due June 30 2023
World Fuel Services Corporation Common Stock
Intel Corporation Common Stock
Intergroup Corporation (The) Common Stock
inTest Corporation Common Stock
Intuit Inc. Common Stock
Intrusion Inc. Common Stock
Inuvo Inc.
Innoviva Inc. Common Stock
Identiv Inc. Common Stock
Invitation Homes Inc. Common Stock
INVO BioScience Inc. Common Stock
Inozyme Pharma Inc. Common Stock
Ion Geophysical Corporation Common Stock
Ionis Pharmaceuticals Inc. Common Stock
Income Opportunity Realty Investors Inc. Common Stock
Innospec Inc. Common Stock
Iovance Biotherapeutics Inc. Common Stock
International Paper Company Common Stock
ImmunoPrecise Antibodies Ltd. Common Stock
Inter Parfums Inc. Common Stock
Professional Diversity Network Inc. Common Stock
Interpublic Group of Companies Inc. (The) Common Stock
IPG Photonics Corporation Common Stock
Innate Pharma S.A. ADS
Inphi Corporation Common Stock
Intrepid Potash Inc Common Stock
Interstate Power & Light Company Perp Prd Ser D
Social Capital Hedosophia Holdings Corp. IV Class A Ordinary Shares
Social Capital Hedosophia Holdings Corp. V Class A Ordinary Shares
Social Capital Hedosophia Holdings Corp. VI Class A Ordinary Shares
InterPrivate Acquisition Corp. Common Stock
Ideal Power Inc. Common Stock
iQIYI Inc. American Depositary Shares
Invesco Quality Municipal Income Trust Common Stock
IQVIA Holdings Inc. Common Stock
Ingersoll Rand Inc. Common Stock
iRobot Corporation Common Stock
IRSA Propiedades Comerciales S.A. American Depositary Shares
Iridium Communications Inc Common Stock
IRIDEX Corporation Common Stock
New Ireland Fund Inc (The) Common Stock
Iron Mountain Incorporated (Delaware)Common Stock REIT
iRadimed Corporation Common Stock
IF Bancorp Inc. Common Stock
Voya Natural Resources Equity Income Fund Common Shares of Beneficial Interest
IRSA Inversiones Y Representaciones S.A. Common Stock
Independence Realty Trust Inc. Common Stock
iRhythm Technologies Inc. Common Stock
Ironwood Pharmaceuticals Inc. Class A Common Stock
Investors Bancorp Inc. Common Stock
PGIM High Yield Bond Fund Inc.
Issuer Direct Corporation Common Stock
IVERIC bio Inc. Common Stock
Insignia Systems Inc. Common Stock
Image Sensing Systems Inc. Common Stock
IsoRay Inc. Common Stock (DE)
Intuitive Surgical Inc. Common Stock
Innovative Solutions and Support Inc. Common Stock
Investar Holding Corporation Common Stock
iSun Inc. Common Stock
Gartner Inc. Common Stock
Industrial Tech Acquisitions Inc. Class A common stock
Industrial Tech Acquisitions Inc. Unit
Industrial Tech Acquisitions Inc. Warrant
Itau CorpBanca American Depositary Shares (each representing 1500 shares of Common Stock no par value)
Intra-Cellular Therapies Inc. Common Stock
Integer Holdings Corporation Common Stock
ITHAX Acquisition Corp. Unit
Iteris Inc. Common Stock
Investors Title Company Common Stock
Itamar Medical Ltd. American Depository Shares
iTeos Therapeutics Inc. Common Stock
IT Tech Packaging Inc. Common Stock
Itiquira Acquisition Corp. Unit
Integra Resources Corp. Common Shares
Itron Inc. Common Stock
Iterum Therapeutics plc Ordinary Share
Ituran Location and Control Ltd. Ordinary Shares
ITT Inc. Common Stock 
Itau Unibanco Banco Holding SA American Depositary Shares (Each repstg 500 Preferred shares)
Illinois Tool Works Inc. Common Stock
Inventiva S.A. American Depository Shares
Intevac Inc. Common Stock
Invacare Corporation Common Stock
Invesco Focused Discovery Growth ETF
Ivy High Income Opportunities Fund Common Shares of Beneficial Interest
Invesco US Large Cap Core ESG ETF
INVESCO MORTGAGE CAPITAL INC Common Stock
Invesco Mortgage Capital Inc. Pfd Ser A
Invesco Mortgage Capital Inc. Preferred Series B Cum Fxd to Fltg
INVESCO MORTGAGE CAPITAL INC 7.5% Fixed-to-Floating Series C Cumulative Redeemable Preferred Stock Liquation Preference $25.00 per Share
Invesco Real Assets ESG ETF
Invesco Select Growth ETF
Invesco Ltd Common Stock
Orix Corp Ads Common Stock
IZEA Worldwide Inc. Common Stock
Jacobs Engineering Group Inc. Common Stock
Jack In The Box Inc. Common Stock
Jaguar Health Inc. Common Stock
JAKKS Pacific Inc. Common Stock
Jamf Holding Corp. Common Stock
JanOne Inc. Common Stock (NV)
TrueShares Structured Outcome (January) ETF
J. Alexander's Holdings Inc. Common Stock
Jazz Pharmaceuticals plc Common Stock (Ireland)
JBG SMITH Properties Common Shares 
J.B. Hunt Transport Services Inc. Common Stock
Lehman ABS 3.50 3.50% Adjustable Corp Backed Tr Certs GS Cap I
Jabil Inc. Common Stock
JetBlue Airways Corporation Common Stock
John B. Sanfilippo & Son Inc. Common Stock
John Bean Technologies Corporation Common Stock
Nuveen Core Equity Alpha Fund Nuveen Core Equity Alpha Fund Common Shares of Beneficial Interest
Johnson Controls International plc Ordinary Share
Jack Creek Investment Corp. Units
Nuveen Credit Opportunities 2022 Target Term Fund Common Shares of Beneficial Interest
j2 Global Inc. Common Stock
Communications Systems Inc. Common Stock
Jewett-Cameron Trading Company Common Shares
JD.com Inc. American Depositary Shares
Nuveen Diversified Dividend and Income Fund Shares of Beneficial Interest
Just Energy Group Inc. Ordinary Shares (Canada)
Jefferies Financial Group Inc. Common Stock
JELD-WEN Holding Inc. Common Stock
Nuveen Emerging Markets Debt 2022 Target Term Fund Common Shares of Beneficial Interest $0.01 par value per share
Aberdeen Japan Equity Fund Inc.  Common Stock
Jiayin Group Inc. American Depositary Shares
Nuveen Floating Rate Income Fund Common Stock
9F Inc. American Depositary Shares
Aurora Mobile Limited American Depositary Shares
Nuveen Global High Income Fund Common Shares of Beneficial Interest
Nuveen Corporate Income 2023 Target Term Fund
Nuveen Corporate Income November 2021 Target Term Fund
Janus Henderson Group plc Ordinary Shares
John Hancock Investors Trust Common Stock
John Hancock Income Securities Trust Common Stock
James Hardie Industries plc American Depositary Shares (Ireland)
Juniper Industrial Holdings Inc. Class A Common Stock
J. Jill Inc. Common Stock
J & J Snack Foods Corp. Common Stock
Jack Henry & Associates Inc. Common Stock
JinkoSolar Holding Company Limited American Depositary Shares (each representing 4 Common Shares)
Jones Lang LaSalle Incorporated Common Stock
Nuveen Mortgage and Income Fund
Jumia Technologies AG American Depositary Shares each representing two Ordinary Shares
Nuveen Multi-Market Income Fund (MA)
JMP Group LLC Common Shares
JMP Group LLC 7.25% Senior Notes due 2027
JMP Group LLC 6.875% Senior Notes due 2029
Jounce Therapeutics Inc. Common Stock
Johnson & Johnson Common Stock
Juniper Networks Inc. Common Stock
GEE Group Inc. Common Stock
51job Inc. American Depositary Shares
St. Joe Company (The) Common Stock
Japan Smaller Capitalization Fund Inc Common Stock
JOFF Fintech Acquisition Corp. Unit
Johnson Outdoors Inc. Class A Common Stock
Jupai Holdings Limited American Depositary Shares each representing six ordinary shares
Nuveen Preferred & Income Opportunities Fund
Nuveen Preferred and Income Term Fund Common Shares of Beneficial Interest
JP Morgan Chase & Co. Common Stock
J P Morgan Chase & Co Depositary Shares each representing a 1/400th interest in a share of 6.00% Non-Cumulative  Preferred Stock Series EE
J P Morgan Chase & Co Depositary Shares each representing a 1/400th  interest in a share of 5.75% Non-Cumulative  Preferred Stock Series DD
J P Morgan Chase & Co Depositary Shares each representing a 1/400th interest in a share of 6.10% Non-Cumulative Preferred Stock Series AA
J P Morgan Chase & Co Depositary Shares each representing a 1/400th interest in a share of 6.15% Non-Cumulative Preferred Stock Series BB
J P Morgan Chase & Co Depositary Shares each representing a 1/400th interest in a share of JPMorgan Chase & Co. 4.75% Non-Cumulative Preferred Stock Series GG
Nuveen Preferred & Income Securities Fund
Nuveen Preferred and Income 2022 Term Fund Common Shares of Beneficial Interest
Nuveen Credit Strategies Income Fund Shares of Beneficial Interest
Nuveen Real Asset Income and Growth Fund Common Shares of Beneficial Interest
China Finance Online Co. Limited American Depositary Shares
Nuveen Floating Rate Income Opportuntiy Fund Shares of Beneficial Interest
Nuveen Real Estate Income Fund Common Shares of Beneficial Interest
Jerash Holdings (US) Inc. Common Stock
James River Group Holdings Ltd. Common Shares
Nuveen Short Duration Credit Opportunities Fund Common Shares of Beneficial Interest
Navient Corporation 6% Senior Notes due December 15 2043
Jianpu Technology Inc. American depositary shares
Nuveen Tax-Advantaged Total Return Strategy Fund Common Share of Beneficial Interest
Nuveen Tax-Advantaged Dividend Growth Fund Common Shares of Beneficial Interest
Jupiter Wellness Inc. Common Stock
Jupiter Wellness Inc. Warrant
Coffee Holding Co. Inc. Common Stock
John Wiley & Sons Inc.
John Wiley & Sons Inc.
Nordstrom Inc. Common Stock
Jaws Acquisition Corp. Class A Ordinary Shares
Jiya Acquisition Corp. Class A Common Stock
The Joint Corp. Common Stock
Kellogg Company Common Stock
Kadant Inc Common Stock
Kismet Acquisition Two Corp. Unit
Kairos Acquisition Corp. Unit
Kala Pharmaceuticals Inc. Common Stock
Kaiser Aluminum Corporation Common Stock
KalVista Pharmaceuticals Inc. Common Stock
Kaman Corporation Common Stock
KAR Auction Services Inc Common Stock
KB Financial Group Inc
Kimball International Inc. Class B Common Stock
KB Home Common Stock
Kubient Inc. Common Stock
Kubient Inc. Warrant
KBR Inc. Common Stock
KBS Fashion Group Limited Common Stock
Kingsoft Cloud Holdings Limited American Depositary Shares
KCAP Financial Inc. 6.125% Notes due 2022
Kadmon Holdings Inc. Common Stock
Chinook Therapeutics Inc. Common Stock
Keurig Dr Pepper Inc. Common Stock
Kimball Electronics Inc. Common Stock
Kelly Services Inc. Class A Common Stock
Kelly Services Inc. Class B Common Stock
Kenon Holdings Ltd. Ordinary Shares
Korea Electric Power Corporation Common Stock
Kewaunee Scientific Corporation Common Stock
Akerna Corp. Common Stock
Akerna Corp Warrant
Kirby Corporation Common Stock
KeyCorp Common Stock
KeyCorp Depositary Shares Each Representing a 1/40th Ownership Interest in a Share of Fixed-to-Floating Rate Perpetual Non-Cumulative Preferred Stock Series E
KeyCorp Depositary Shares each representing a 1/40th ownership interest in a share of Fixed Rate Perpetual Non-Cumulative Preferred Stock Series F
KeyCorp Depositary Shares each representing a 1/40th ownership interest in a share of Fixed Rate Perpetual Non-Cumulative Preferred Stock Series G
Keysight Technologies Inc. Common Stock
Korea Fund Inc. (The) New Common Stock
Kentucky First Federal Bancorp Common Stock
Kforce Inc. Common Stock
Kingsway Financial Services Inc. Common Stock (DE)
Korn Ferry Common Stock
Kinross Gold Corporation Common Stock
The Kraft Heinz Company Common Stock
OrthoPediatrics Corp. Common Stock
Kismet Acquisition Three Corp. Unit
Kimco Realty Corporation Common Stock
Kimco Realty Corporation Class L Depositary Shares each of which represents a one-one thousandth fractional interest in a share of 5.125% Class L Cumulative Redeemable Preferred Stock liquidation preference $25000.00 per share
Kimco Realty Corporation Class M Depositary Shares each of which represents a one-one thousandth fractional interest in a share of 5.25% Class M Cumulative Redeemable Preferred Stock liquidation preference $25000.00 per share
Kindred Biosciences Inc. Common Stock
Kingstone Companies Inc. Common Stock
KINS Technology Group Inc. Class A Common Stock
KINS Technology Group Inc. Unit
KINS Technology Group Inc. Warrant
KKR Income Opportunities Fund Common Shares
Kelso Technologies Inc Ordinary Shares
Kirkland's Inc. COMMONSTOCK
Innovator Russell 2000 Power Buffer ETF - July
KKR & Co. Inc. Common Stock
KKR & Co. Inc. 6.75% Series A Preferred Stock
KKR & Co. Inc. 6.50% Series B Preferred Stock
KKR & Co. Inc. 6.00% Series C Mandatory Convertible Preferred Stock
Kirkland Lake Gold Ltd. Common Shares
KLA Corporation Common Stock
KL Acquisition Corp Unit
Kaleido Biosciences Inc. Common Stock
Kulicke and Soffa Industries Inc. Common Stock
Kaleyra Inc. Common Stock
KLX Energy Services Holdings Inc. Common Stock
Kimberly-Clark Corporation Common Stock
Kamada Ltd. Ordinary Shares
Kayne Anderson NextGen Energy & Infrastructure Inc.
Kinder Morgan Inc. Common Stock
KemPharm Inc. Common Stock
Kemper Corporation
Kennametal Inc. Common Stock
CarMax Inc
Knowles Corporation Common Stock
Kandi Technologies Group Inc Common Stock
UPHOLDINGS Compound Kings ETF
Knoll Inc. Common Stock
KNOT Offshore Partners LP Common Units representing Limited Partner Interests
Kiniksa Pharmaceuticals Ltd. Class A Common Stock
Kinsale Capital Group Inc. Common Stock
Kinnate Biopharma Inc. Common Stock
Knight-Swift Transportation Holdings Inc.
Coca-Cola Company (The) Common Stock
Kodiak Sciences Inc Common Stock
Eastman Kodak Company Common New
Coca Cola Femsa S.A.B. de C.V.  American Depositary Shares each representing 10 Units (each Unit consists of 3 Series B Shares and 5 Series L Shares)
Koppers Holdings Inc. Koppers Holdings Inc. Common Stock
Kopin Corporation Common Stock
Corvus Gold Inc. Common Shares
Kosmos Energy Ltd. Common Shares (DE)
Koss Corporation Common Stock
Karyopharm Therapeutics Inc. Common Stock
Kroger Company (The) Common Stock
Kraton Corporation Common Stock
Kiromic BioPharma Inc. Common Stock
Kilroy Realty Corporation Common Stock
KKR Real Estate Finance Trust Inc. Common Stock
Kite Realty Group Trust Common Stock
36Kr Holdings Inc. American Depositary Shares
Repro Med Systems Inc. Common Stock
Kernel Group Holdings Inc. Units
Kornit Digital Ltd. Ordinary Shares
Kearny Financial Corp Common Stock
Kronos Worldwide Inc Common Stock
Kronos Bio Inc. Common Stock
Keros Therapeutics Inc. Common Stock
Kimbell Royalty Partners Common Units Representing Limited Partner Interests
Karuna Therapeutics Inc. Common Stock
Kura Sushi USA Inc. Class A Common Stock
Krystal Biotech Inc. Common Stock
DWS Strategic Municipal Income Trust
Kismet Acquisition One Corp Ordinary Shares
Kismet Acquisition One Corp Unit
Kismet Acquisition One Corp Warrant
Kaspien Holdings Inc. Common Stock
Kohl's Corporation Common Stock
Kansas City Southern Common Stock
Kansas City Southern Preferred Stock
KT Corporation Common Stock
Kontoor Brands Inc. Common Stock 
Key Tronic Corporation Common Stock
DWS Municipal Income Trust
Structures Products Cp 8% CorTS Issued by Peco Energy Cap Tr II Preferred Stock
Structured Products Corp 8.205% CorTS 8.205% Corporate Backed Trust Securities (CorTS)
Kratos Defense & Security Solutions Inc. Common Stock
Kintara Therapeutics Inc. Common Stock
Kuke Music Holding Limited American Depositary Shares each representing one Ordinary Share
Kura Oncology Inc. Common Stock
KVH Industries Inc. Common Stock
Kennedy-Wilson Holdings Inc. Common Stock
Kingswood Acquisition Corp. Class A Common Stock
Quaker Chemical Corporation Common Stock
Kaixin Auto Holdings Ordinary Share
Kymera Therapeutics Inc. Common Stock
Kayne Anderson Energy Infrastructure Fund Inc.
Kazia Therapeutics Limited American Depositary Shares
Kezar Life Sciences Inc. Common Stock
Loews Corporation Common Stock
Landos Biopharma Inc. Common Stock
Lithium Americas Corp. Common Shares
Leisure Acquisition Corp. Common Stock
Leisure Acquisition Corp. Unit
Leisure Acquisition Corp. Warrant
Lithia Motors Inc. Common Stock
Ladder Capital Corp Class A Common Stock
LAIX Inc. American Depositary Shares each  representing one Class A Ordinary Share
Lakeland Industries Inc. Common Stock
Lamar Advertising Company Class A Common Stock
Lancaster Colony Corporation Common Stock
Gladstone Land Corporation Common Stock
Gladstone Land Corporation 5.00% Series D Cumulative Term Preferred Stock
Gladstone Land Corporation 6.00% Series B Cumulative Redeemable Preferred Stock
Landmark Bancorp Inc. Common Stock
nLIGHT Inc. Common Stock
Union Acquisition Corp. II Ordinary Shares
Union Acquisition Corp. II Units containing one ordinary share and one redeemable warrant
Union Acquisition Corp. II Warrant
Laureate Education Inc. Class A Common Stock
Lawson Products Inc. Common Stock
Lazard LTD. Lazard LTD. Class A Common Stock
Luminar Technologies Inc.  Class A Common Stock
Luminar Technologies Inc. Warrant
Lazydays Holdings Inc. Common Stock
L Brands Inc.
Lakeland Bancorp Inc. Common Stock
Luther Burbank Corporation Common Stock
Liberty Broadband Corporation Class A Common Stock
Liberty Broadband Corporation Class C Common Stock
Liberty Broadband Corporation Series A Cumulative Redeemable Preferred Stock
Liberty Oilfield Services Inc. Class A Common Stock
Liberty Global plc Class A Ordinary Shares
Liberty Global plc Class B Ordinary Shares
Liberty Global plc Class C Ordinary Shares
LendingClub Corporation Common Stock
Lionheart Acquisition Corp. II Class A Common Stock
Lionheart Acquisition Corp. II Unit
Lionheart Acquisition Corp. II Warrant
Lannett Co Inc Common Stock
LCI Industries
LCNB Corporation Common Stock
Lineage Cell Therapeutics Inc. Common Stock
Lifetime Brands Inc. Common Stock
Landcadia Holdings III Inc. Class A Common Stock
Landcadia Holdings III Inc. Unit 
Landcadia Holdings III Inc. Warrant
loanDepot Inc. Class A Common Stock
Lydall Inc. Common Stock
Leidos Holdings Inc. Common Stock
Cohen & Steers Limited Duration Preferred and Income Fund Inc.
Lands' End Inc. Common Stock
Lear Corporation Common Stock
Leaf Group Ltd. Common Stock
Ribbit LEAP Ltd. Class A Ordinary Shares
Lincoln Electric Holdings Inc. Common Shares
SemiLEDS Corporation Common Stock
Lee Enterprises Incorporated Common Stock
Leggett & Platt Incorporated Common Stock
Legacy Housing Corporation Common Stock (TX)
Legend Biotech Corporation American Depositary Shares
Legato Merger Corp. Units
Leju Holdings Limited American Depositary Shares each representing one Ordinary share
Lennar Corporation Class A Common Stock
BNY Mellon Strategic Municipals Inc. Common Stock
Leslie's Inc. Common Stock
Centrus Energy Corp. Class A Common Stock
Levi Strauss & Co Class A Common Stock
Level One Bancorp Inc. Common Stock
Level One Bancorp Inc. Depositary Shares Each Representing a 1/100th Interest in a Share of 7.50% Non-Cumulative Perpetual Preferred Stock Series B
Lexaria Bioscience Corp. Common Stock
Lexaria Bioscience Corp. Warrant
China Life Insurance Company Limited American Depositary Shares
Lument Finance Trust Inc. Common Stock
Lefteris Acquisition Corp. Class A Common Stock
Lefteris Acquisition Corp. Unit
Lefteris Acquisition Corp. Warrant
Littelfuse Inc. Common Stock
Lifevantage Corporation Common Stock (Delaware)
Lazard Growth Acquisition Corp. I Units
Lion Group Holding Ltd. American Depositary Share
Lion Group Holding Ltd. Warrant
Lazard Global Total Return and Income Fund Common Stock
LGI Homes Inc. Common Stock
LGL Group Inc. (The) Common Stock
Ligand Pharmaceuticals Incorporated Common Stock
Longeveron Inc. Class A Common Stock
Laboratory Corporation of America Holdings Common Stock
LHC Group Common Stock
Lucira Health Inc. Common Stock
L3Harris Technologies Inc. Common Stock
Li Auto Inc. American Depositary Shares
aTyr Pharma Inc. Common Stock
Lennox International Inc. Common Stock
Liberty Latin America Ltd. Class A Common Stock
Liberty Latin America Ltd. Class C Common Stock
Linde plc Ordinary Share
Lincoln Educational Services Corporation Common Stock
Lindblad Expeditions Holdings Inc. Common Stock
Linx S.A. American Depositary Shares each representing one common share
LiqTech International Inc. Common Stock
LightInTheBox Holding Co. Ltd. American Depositary Shares each representing 2 ordinary shares
Lumentum Holdings Inc. Common Stock
Emles @Home ETF
Live Ventures Incorporated Common Stock
LIV Capital Acquisition Corp. Class A Ordinary Shares
LIV Capital Acquisition Corp. Unit
LIV Capital Acquisition Corp. Warrant
LivaNova PLC Ordinary Shares
LiveXLive Media Inc. Common Stock
Lixte Biotechnology Holdings Inc. Common Stock
Lixte Biotechnology Holdings Inc. Warrants
LIZHI INC. American Depositary Shares
LightJump Acquisition Corporation Unit
La Jolla Pharmaceutical Company Common Stock
Luokung Technology Corp Ordinary Shares
Lakeland Financial Corporation Common Stock
LKQ Corporation Common Stock
Lumber Liquidators Holdings Inc Common Stock
Lianluo Smart Limited Class A Common Stock
Limelight Networks Inc. Common Stock
Eli Lilly and Company Common Stock
Liberty Media Acquisition Corporation Unit
LMF Acquisition Opportunities Inc. Unit
LeMaitre Vascular Inc. Common Stock
Limbach Holdings Inc. Common Stock
LM Funding America Inc. Common Stock
Lemonade Inc. Common Stock
Liminal BioSciences Inc. Common Shares
Limoneira Co Common Stock
Luminex Corporation Common Stock
LMP Automotive Holdings Inc. Common Stock
Landmark Infrastructure Partners LP Common Units
Landmark Infrastructure Partners LP 7% Series C Fltg/Fxd Perpetual Conv Preferred Stock
Landmark Infrastructure Partners LP Perpetual Preferred Units Series B 7.90%
Landmark Infrastructure Partners LP 8.00% Series A Cumulative Redeemable Perpetual Preferred Units
Limestone Bancorp Inc. Common Stock
Lockheed Martin Corporation Common Stock
Lincoln National Corporation Common Stock
Brasilagro Brazilian Agric Real Estate Co Sponsored ADR (Brazil)
Landec Corporation Common Stock (DE)
L&amp;F Acquisition Corp. Class A Ordinary Shares
Cheniere Energy Inc. Common Stock
Lindsay Corporation Common Stock
LENSAR Inc. Common Stock
Alliant Energy Corporation Common Stock
Lantheus Holdings Inc. Common Stock
Longevity Acquisition Corporation Ordinary Shares
Longevity Acquisition Corporation Right
Longevity Acquisition Corporation Warrant
Manhattan Bridge Capital Inc
Live Oak Bancshares Inc. Common Stock
El Pollo Loco Holdings Inc. Common Stock
Comstock Mining Inc. Common Stock
LogicBio Therapeutics Inc. Common Stock
Logitech International S.A. Ordinary Shares
Live Oak Acquisition Corp. II Class A Common Stock
Loma Negra Compania Industrial Argentina Sociedad Anonima ADS
Loop Industries Inc. Common Stock
Grand Canyon Education Inc. Common Stock
Loral Space and Communications Inc. Common Stock
CarLotz Inc. Class A Common Stock
CarLotz Inc. Warrant
Spark Networks Inc. American Depositary Shares (each representing one-tenth of an Ordinary Share)
The Lovesac Company Common Stock
Lowe's Companies Inc. Common Stock
Lipocine Inc. Common Stock
Dorian LPG Ltd. Common Stock
Laredo Petroleum Inc. Common Stock
LG Display Co Ltd AMERICAN DEPOSITORY SHARES
LPL Financial Holdings Inc. Common Stock
Open Lending Corporation Class A Common Stock
LivePerson Inc. Common Stock
LightPath Technologies Inc. Class A Common Stock
Leap Therapeutics Inc. Common Stock
Louisiana-Pacific Corporation Common Stock
Liquidia Corporation Common Stock
Liquidity Services Inc. Common Stock
Lam Research Corporation Common Stock
Larimar Therapeutics Inc. Common Stock
Stride Inc. Common Stock
LifeSci Acquisition II Corp. Common Stock
Lake Shore Bancorp Inc. Common Stock
Lattice Semiconductor Corporation Common Stock
Landsea Homes Corporation Common Stock
Landsea Homes Corporation Warrant
Laird Superfood Inc. Common Stock
Life Storage Inc. Common Stock
Lightspeed POS Inc. Subordinate Voting Shares
Landstar System Inc. Common Stock
Liberty Media Corporation Series A Liberty SiriusXM Common Stock
Liberty Media Corporation Series B Liberty SiriusXM Common Stock
Liberty Media Corporation Series C Liberty SiriusXM Common Stock
Lightbridge Corporation Common Stock
LTC Properties Inc. Common Stock
Livent Corporation Common Stock
Lantern Pharma Inc. Common Stock
Liberty TripAdvisor Holdings Inc. Series A Common Stock
Liberty TripAdvisor Holdings Inc. Series B Common Stock
Lantronix Inc. Common Stock
Lufax Holding Ltd American Depositary Shares two of which representing one Ordinary Share
Luby's Inc. Common Stock
lululemon athletica inc. Common Stock
Lumen Technologies Inc. Common Stock
Lumos Pharma Inc. Common Stock
Luna Innovations Incorporated Common Stock
Pulmonx Corporation Common Stock
Southwest Airlines Company Common Stock
Lux Health Tech Acquisition Corp. Class A Common Stock
Lux Health Tech Acquisition Corp. Units
Lux Health Tech Acquisition Corp. Warrants
Emles Trust Emles Luxury Goods ETF
Las Vegas Sands Corp. Common Stock
Lamb Weston Holdings Inc. Common Stock 
Locust Walk Acquisition Corp. Unit
Lifeway Foods Inc. Common Stock
LexinFintech Holdings Ltd. American Depositary Shares
Lixiang Education Holding Co. Ltd. American Depositary Shares
Luxfer Holdings PLC Ordinary Shares
Lexington Realty Trust Common Stock
Lexington Realty Trust  Preferred Conv. Series C
Lexicon Pharmaceuticals Inc. Common Stock
LSB Industries Inc. Common Stock
LyondellBasell Industries NV Ordinary Shares Class A (Netherlands)
2ndVote Life Neutral Plus ETF
Lyft Inc. Class A Common Stock
Lloyds Banking Group Plc American Depositary Shares
Dragon Victory International Limited Ordinary Shares
Lyra Therapeutics Inc. Common Stock
LSI Industries Inc. Common Stock
Live Nation Entertainment Inc. Common Stock
La-Z-Boy Incorporated Common Stock
Macy's Inc Common Stock
Mastercard Incorporated Common Stock
Mid-America Apartment Communities Inc. Common Stock
Mid-America Apartment Communities Inc. 8.50% Series I Cumulative Redeemable Preferred Stock
Montes Archimedes Acquisition Corp. Class A Common Stock
Montes Archimedes Acquisition Corp. Unit
Montes Archimedes Acquisition Corp. Warrant
Macerich Company (The) Common Stock
Moringa Acquisition Corp Units
Merrimack Pharmaceuticals Inc. Common Stock
Mallard Acquisition Corp. Common stock
Mallard Acquisition Corp. Unit
Mallard Acquisition Corp. Warrant
MAG Silver Corporation Ordinary Shares
Magal Security Systems Ltd. Ordinary Shares
Main Street Capital Corporation Common Stock
ManpowerGroup Common Stock
Manhattan Associates Inc. Common Stock
ManTech International Corporation Common Stock $0.01 Par Value
Manchester United Ltd. Class A Ordinary Shares
Marriott International Class A Common Stock
Marathon Patent Group Inc. Common Stock
Remark Holdings Inc. Common Stock
Marine Petroleum Trust Units of Beneficial Interest
Masco Corporation Common Stock
Masimo Corporation Common Stock
908 Devices Inc. Common Stock
Mattel Inc. Common Stock
Matthews International Corporation Class A Common Stock
Matson Inc. Common Stock
Pioneer Municipal High Income Advantage Trust Common Shares of Beneficial Interest
MediaAlpha Inc. Class A Common Stock
Maxeon Solar Technologies Ltd. Ordinary Shares
Maxar Technologies Inc.
J. W. Mays Inc. Common Stock
VanEck Vectors Moody's Analytics BBB Corporate Bond ETF
Middlefield Banc Corp. Common Stock
MBIA Inc. Common Stock
Marrone Bio Innovations Inc. Common Stock
Merchants Bancorp Common Stock
Merchants Bancorp Depositary Shares Each Representing a 1/40th Interest in a Share of Series B  Fixed-to-Floating Rate
Merchants Bancorp 7.00% Fixed-to-Floating Rate Series A Non-Cumulative Perpetual Preferred Stock
Mustang Bio Inc. Common Stock
SPDR Nuveen Municipal Bond ETF
Medallion Bank Fixed-to-Floating Rate Non-Cumulative Perpetual Preferred Stock Series F
Microbot Medical Inc. Common Stock
Moleculin Biotech Inc. Common Stock
Mobile TeleSystems PJSC
Malibu Boats Inc. Class A Common Stock
Mercantile Bank Corporation Common Stock
Moelis & Company Class A Common Stock
Blackrock MuniYield California Quality Fund Inc. Common Stock
Mountain Crest Acquisition Corp. II Unit
Metropolitan Bank Holding Corp. Common Stock
Macatawa Bank Corporation Common Stock
MetroCity Bankshares Inc. Common Stock
McDonald's Corporation Common Stock
Contango Oil & Gas Company Common Stock (TX)
McAfee Corp. Class A Common Stock
MasterCraft Boat Holdings Inc. Common Stock
Microchip Technology Incorporated Common Stock
Marchex Inc. Class B Common Stock
Barings Corporate Investors Common Stock
McKesson Corporation Common Stock
Merida Merger Corp. I Common Stock
Merida Merger Corp. I Warrant
Madison Covered Call & Equity Strategy Fund Common Stock
Moody's Corporation Common Stock
MFS Charter Income Trust Common Stock
Seres Therapeutics Inc. Common Stock
Monarch Casino & Resort Inc. Common Stock
Marcus Corporation (The) Common Stock
Mercury General Corporation Common Stock
Mednax Inc. Common Stock
MongoDB Inc. Class A Common Stock
M.D.C. Holdings Inc. Common Stock
MDC Partners Inc. CL A Subordinate Voting Shares
Madrigal Pharmaceuticals Inc. Common Stock
Medigus Ltd. American Depositary Shares
Medigus Ltd. Series C Warrant
Mediaco Holding Inc. Class A Common Stock 
MDJM LTD Ordinary Share
Medallia Inc. Common Stock
Medley LLC 7.25% Notes due 2024
Medley LLC 6.875% Senior Notes due 2026
Medley Management Inc. Class A Common Stock
Mondelez International Inc. Class A Common Stock
Medicenna Therapeutics Corp. Common Shares
Meredith Corporation Common Stock
Medalist Diversified REIT Inc. Common Stock
Medalist Diversified REIT Inc. Series A Cumulative Redeemable Preferred Stock
Allscripts Healthcare Solutions Inc. Common Stock
Medtronic plc. Ordinary Shares
MDU Resources Group Inc. Common Stock (Holding Company)
MedAvail Holdings Inc. Common Stock
MediWound Ltd. Ordinary Shares
Midwest Holding Inc. Common Stock
MiMedx Group Inc Common Stock
Mayville Engineering Company Inc. Common Stock
MEDIFAST INC Common Stock
Medpace Holdings Inc. Common Stock
Trxade Group Inc. Common Stock
Montrose Environmental Group Inc. Common Stock
Methode Electronics Inc. Common Stock
MEI Pharma Inc. Common Stock
MercadoLibre Inc. Common Stock
Blackrock MuniEnhanced Fund Inc Common Stock
Methanex Corporation Common Stock
Bank of America Corporation Income Capital Obligation Notes initially due December 15 2066
Mercer International Inc. Common Stock
Mesa Air Group Inc. Common Stock
Mesoblast Limited American Depositary Shares
MetLife Inc. Common Stock
MetLife Inc. Preferred Series A Floating Rate
MetLife Inc. Depositary shares each representing a 1/1000th interest in a share of the Issuera??s 5.625% Non-Cumulative Preferred Stock Series E.
MetLife Inc. Depositary Shares each representing a 1/1000th interest in a share of 4.75% Non-Cumulative Preferred Stock Series F
Ramaco Resources Inc. Common Stock
Meten EdtechX Education Group Ltd. Ordinary Shares
Meten EdtechX Education Group Ltd. Warrant
MFA Financial Inc.
MFA Financial Inc. Preferred Series B
MFA Financial Inc. 6.50% Series C Fixed-to-Floating Rate Cumulative Redeemable Preferred Stock
Manulife Financial Corporation Common Stock
Macquarie First Trust Global Common Stock
Mizuho Financial Group Inc. Sponosred ADR (Japan)
Micro Focus Intl PLC ADS each representing One Ord Sh
Mercurity Fintech Holding Inc. ADS
Medallion Financial Corp. Common Stock
Medallion Financial Corp. 9.000% Notes due 2021
Blackrock MuniHoldings Investment Quality Fund Common Shares of Beneficial Interest
MFS Municipal Income Trust Common Stock
Motley Fool Small-Cap Growth ETF
Mackinac Financial Corporation Common Stock
Blackrock MuniYield Investment Quality Fund Common Shares of Beneficial Interest
MFS Special Value Trust Common Stock
Mistras Group Inc Common Stock
Magna International Inc. Common Stock
MGE Energy Inc
MFS Government Markets Income Trust Common Stock
Moneygram International Inc. Common Stock
Magic Software Enterprises Ltd. Ordinary Shares
Magellan Health Inc. Common Stock
MGM Resorts International Common Stock
Magnite Inc. Common Stock
MacroGenics Inc. Common Stock
MGM Growth Properties LLC Class A common shares representing limited liability company interests
MGP Ingredients Inc.
Affiliated Managers Group Inc. 5.875% Junior Subordinated Notes due 2059
Affiliated Managers Group Inc. 4.750% Junior Subordinated Notes due 2060
McGrath RentCorp Common Stock
Magenta Therapeutics Inc. Common Stock
MeiraGTx Holdings plc Ordinary Shares
Macquarie Global Infrastructure Total Return Fund Inc. Common Stock
Magnolia Oil & Gas Corporation Class A Common Stock
Magyar Bancorp Inc. Common Stock
Maiden Holdings Ltd. Pref Shs Ser A (Bermuda)
Maiden Holdings North America Ltd. 7.125% Non-Cumulative Preference Shares Series C
Maiden Holdings Ltd. 6.700% Non-Cumulative Preference Shares Series D
Blackrock MuniHoldings Fund Inc. Common Stock
BlackRock Massachusetts Tax-Exempt Trust
Western Asset Municipal High Income Fund Inc. Common Stock
Mastech Digital Inc Common Stock
Pioneer Municipal High Income Trust Common Shares of Beneficial Interest
Mohawk Industries Inc. Common Stock
Maiden Holdings Ltd. 6.625% Notes due 2046
Maiden Holdings Ltd.
Blackrock MuniHoldings New York Quality Fund Inc. Common Stock
Maiden Holdings North America Ltd. 7.75% Notes due 2043
M/I Homes Inc. Common Stock
Macquarie Infrastructure Corporation Common Stock
MICT Inc. Common Stock
Middleby Corporation (The) Common Stock
Cohen & Steers MLP Income and Energy Opportunity Fund Inc. Common Stock
VanEck Vectors Moody's Analytics IG Corporate Bond ETF
The Michaels Companies Inc. Common Stock
Metromile Inc. Common Stock
Metromile Inc. Warrant 
Mimecast Limited Ordinary Shares
MFS Intermediate Income Trust Common Stock
MIND Technology Inc. Common Stock (DE)
MIND Technology Inc. Series A 9.00% Series A Cumulative Preferred Stock (DE)
Mirum Pharmaceuticals Inc. Common Stock
Milestone Pharmaceuticals Inc. Common Shares
Mitek Systems Inc. Common Stock
Stealth BioTherapeutics Corp. ADS
AG Mortgage Investment Trust Inc. Common Stock
AG Mortgage Investment Trust Inc. 8.25% Preferred Series A
AG Mortgage Investment Trust Inc. Preferred Series B
AG Mortgage Investment Trust Inc. 8.00% Series C Fixed-to-Floating Rate Cumulative Redeemable Preferred Stock $0.01 par value per share
MiX Telematics Limited American Depositary Shares each representing 25 Ordinary Shares
Blackrock MuniYield Michigan Quality Fund Inc. Common Stock
McCormick & Company Incorporated Common Stock
Molecular Data Inc. American Depositary Shares
Monaker Group Inc. Common Stock
Markel Corporation Common Stock
MKS Instruments Inc. Common Stock
MarketAxess Holdings Inc. Common Stock
Mesa Laboratories Inc. Common Stock
Malacca Straits Acquisition Company Limited Class A Ordinary Shares
Malacca Straits Acquisition Company Limited Units
Malacca Straits Acquisition Company Limited Warrants
Melco Resorts & Entertainment Limited American Depositary Shares
Herman Miller Inc. Common Stock
Mueller Industries Inc. Common Stock
Martin Marietta Materials Inc. Common Stock
Millendo Therapeutics Inc. Common Stock
Maui Land & Pineapple Company Inc. Common Stock
Miller Industries Inc. Common Stock
Milestone Scientific Inc. Common Stock
Malvern Bancorp Inc. Common Stock
MMA Capital Holdings Inc. Common Stock
Marsh & McLennan Companies Inc. Common Stock
MainStay MacKay DefinedTerm Municipal Opportunities Fund
Marcus & Millichap Inc. Common Stock
Martin Midstream Partners L.P. Limited Partnership
3M Company Common Stock
Magellan Midstream Partners L.P. Limited Partnership
Maximus Inc. Common Stock
Merit Medical Systems Inc. Common Stock
MFS Multimarket Income Trust Common Stock
Western Asset Managed Municipals Fund Inc. Common Stock
Maverix Metals Inc. Common Shares
MakeMyTrip Limited Ordinary Shares
Manning & Napier Inc. Class A Common Stock
MIND C.T.I. Ltd. Ordinary Shares
MannKind Corporation Common Stock
Medicinova Inc Common Stock
Western Asset Municipal Partners Fund Inc. Common Stock
Monopar Therapeutics Inc. Common Stock
Monmouth Real Estate Investment Corporation Class A Common Stock
Monmouth Real Estate Investment Corporation 6.125% Series C Cumulative Redeemable Preferred Stock
Brigham Minerals Inc. Class A Common Stock
Monro Inc. Common Stock
MainStreet Bancshares Inc. Common Stock
MainStreet Bancshares Inc. Depositary Shares
MINISO Group Holding Limited American Depositary Shares each representing four Class A Ordinary Shares
Monster Beverage Corporation
Montauk Renewables Inc. Common Stock
Manitex International Inc. Common Stock
Altria Group Inc.
Modine Manufacturing Company Common Stock
Model N Inc. Common Stock
ModivCare Inc. Common Stock
MidWestOne Financial Gp Common Stock
Mogo Inc. Common Shares
MOGU Inc. American Depositary Shares (each  representing 25 Class A Ordinary Shares)
Molina Healthcare Inc Common Stock
ECMOHO Limited American Depositary Shares
Momo Inc. American Depositary Shares
Monument Circle Acquisition Corp. Unit
MorphoSys AG American Depositary Shares
Morphic Holding Inc. Common Stock
Morningstar Inc. Common Stock
Mosaic Company (The) Common Stock
MoSys Inc. Common Stock
Motion Acquisition Corp. Class A Common Stock
Motion Acquisition Corp. Unit
Motion Acquisition Corp. Warrants to purchase one Class A common
Motus GI Holdings Inc. Common Stock
Motive Capital Corp Class A Ordinary Shares
Movado Group Inc. Common Stock
Moxian Inc. Common Stock
MP Materials Corp. Common Stock
Blackrock MuniYield Pennsylvania Quality Fund Common Stock
Motorcar Parts  of America Inc. Common Stock
Mid Penn Bancorp Common Stock
Marathon Petroleum Corporation Common Stock
MultiPlan Corporation Class A Common Stock
MPLX LP Common Units Representing Limited Partner Interests
Barings Participation Investors Common Stock
Medical Properties Trust Inc. common stock
Monolithic Power Systems Inc. Common Stock
Marine Products Corporation Common Stock
Blackrock MuniYield Quality Fund II Inc. Common Stock
Blackrock MuniYield Quality Fund Inc. Common Stock
Marquee Raine Acquisition Corp. Class A Ordinary Shares
Marquee Raine Acquisition Corp. Unit
Marquee Raine Acquisition Corp. Warrant
Everspin Technologies Inc. Common Stock
Meridian Corporation Common Stock
MRC Global Inc. Common Stock
Monroe Capital Corporation Common Stock
Mercury Systems Inc Common Stock
Mereo BioPharma Group plc American Depositary Shares
Marin Software Incorporated Common Stock
Merck & Company Inc. Common Stock (new)
Marker Therapeutics Inc. Common Stock
Marlin Business Services Corp. Common Stock
MEDIROM Healthcare Technologies Inc. American Depositary Share
Moderna Inc. Common Stock
Marinus Pharmaceuticals Inc. Common Stock
Marathon Oil Corporation Common Stock
Agility Shares Managed Risk ETF
Mersana Therapeutics Inc. Common Stock
Marten Transport Ltd. Common Stock
Mirati Therapeutics Inc. Common Stock
Merus N.V. Common Shares
Maravai LifeSciences Holdings Inc. Class A Common Stock
Marvell Technology Group Ltd. Common Stock
Morgan Stanley Common Stock
Morgan Stanley Dep Shs repstg 1/1000 Pfd Ser A
Morgan Stanley DEPOSITARY SHARES REP 1/1000TH SHARES FIXED/FLTG PREFERRED STOCK SERIES E
Morgan Stanley Dep Shs Rpstg 1/1000th Int Prd Ser F Fxd to Flag
Morgan Stanley Depository Shares Representing 1/1000th Preferred Series 1 Fixed to Floating Non (Cum)
Morgan Stanley Depositary Shares each representing 1/1000th of a share of Fixed-to-Floating Rate Non-Cumulative Preferred Stock  Series K
Morgan Stanley Depositary Shares each representing 1/1000th of a share of 4.875% Non-Cumulative Preferred Stock Series L
MSA Safety Incorporated Common Stock
Medicus Sciences Acquisition Corp. Unit
Mesabi Trust Common Stock
Midland States Bancorp Inc. Common Stock
Studio City International Holdings Limited American depositary shares each representing four  Class A ordinary shares
MSCI Inc Common Stock
Morgan Stanley Emerging Markets Debt Fund Inc. Common Stock
Middlesex Water Company Common Stock
Microsoft Corporation Common Stock
Madison Square Garden Entertainment Corp. Class A Common Stock 
Motorsport Games Inc. Class A Common Stock
MSG Networks Inc. Common Stock
Madison Square Garden Sports Corp. Class A Common Stock (New)
Motorola Solutions Inc. Common Stock
MSC Industrial Direct Company Inc. Common Stock
Emerson Radio Corporation Common Stock
MISONIX Inc. Common Stock (DE)
Datto Holding Corp. Common Stock
LHA Market State Tactical Beta ETF
MicroStrategy Incorporated Common Stock Class A
Mid-Southern Bancorp Inc. Common Stock
LHA Market State Alpha Seeker ETF
Arcelor Mittal NY Registry Shares NEW
Metalla Royalty & Streaming Ltd. Common Shares
MedTech Acquisition Corporation Class A Common Stock
MedTech Acquisition Corporation Unit
MedTech Acquisition Corporation Warrant
M&T Bank Corporation Common Stock
MTBC Inc. Common Stock
MTBC Inc. 11% Series A Cumulative Redeemable Perpetual Preferred Stock
MMTec Inc. Common Shares
Match Group Inc. Common Stock
ArcelorMittal 5.50% Mandatorily Convertible Subordinated Notes due 2023
Metacrine Inc. Common Stock
Mettler-Toledo International Inc. Common Stock
Matador Resources Company Common Stock
Molecular Templates Inc. Common Stock
Mannatech Incorporated Common Stock
MGIC Investment Corporation Common Stock
Meritage Homes Corporation Common Stock
Mechel PAO American Depositary Shares (Each rep. 1 common shares)
Mechel PAO American Depositary Shares (each representing one-half of a Preferred Share)
Materialise NV American Depositary Shares
Vail Resorts Inc. Common Stock
Matinas Biopharma Holdings Inc. Common Stock
Meritor Inc. Common Stock
Midatech Pharma PLC American Depositary Shs
Mesa Royalty Trust Common Stock
Materion Corporation
Matrix Service Company Common Stock
MTS Systems Corporation Common Stock
MACOM Technology Solutions Holdings Inc. Common Stock
MER Telemanagement Solutions Ltd. Common Shares
Western Asset Municipal Defined Opportunity Trust Inc Common Stock
Manitowoc Company Inc. (The) Common Stock
Minerals Technologies Inc. Common Stock
MasTec Inc. Common Stock
Micron Technology Inc. Common Stock
Blackrock MuniAssets Fund Inc Common Stock
Blackrock MuniHoldings California Quality Fund Inc.  Common Stock
Mudrick Capital Acquisition Corporation II Class A Common Stock
Mudrick Capital Acquisition Corporation II Unit
Mudrick Capital Acquisition Corporation II Warrant
Blackrock MuniHoldings Quality Fund II Inc. Common Stock
Mitsubishi UFJ Financial Group Inc. Common Stock
Blackrock MuniHoldings Fund II Inc. Common Stock
Blackrock Muni Intermediate Duration Fund Inc Common Stock
Blackrock MuniHoldings New Jersey Quality Fund Inc. Common Stock
Murphy Oil Corporation Common Stock
Blackrock MuniHoldings Quality Fund Inc Common Stock
Murphy USA Inc. Common Stock
McEwen Mining Inc. Common Stock
MVB Financial Corp. Common Stock
Blackrock MuniVest Fund Inc. Common Stock
MicroVision Inc. Common Stock
MV Oil Trust Units of Beneficial Interests
Blackrock MuniVest Fund II Inc.  Common Stock
MUELLER WATER PRODUCTS Common Stock
Mohawk Group Holdings Inc. Common Stock
MagnaChip Semiconductor Corporation Depositary Shares each representing one share of common stock
Mexco Energy Corporation Common Stock
Mexico Equity and Income Fund Inc. (The) Common Stock
Mexico Fund Inc. (The) Common Stock
Maxim Integrated Products Inc. Common Stock
MaxLinear Inc. Common Stock
Blackrock MuniYield California Fund Inc. Common Stock
Blackrock MuniYield Fund Inc.  Common Stock
Myers Industries Inc. Common Stock
Blackrock MuniYield Investment Fund Common Stock
First Western Financial Inc. Common Stock
Myriad Genetics Inc. Common Stock
Blackrock MuniYield Quality Fund III Inc Common Stock
Blackrock MuniYield New Jersey Fund Inc Common Stock
Blackrock MuniYield New York Quality Fund Inc.Common Stock
Myomo Inc. Common Stock
Myovant Sciences Ltd. Common Shares
MYR Group Inc. Common Stock
My Size Inc. Common Stock
Urban Tea Inc. Ordinary Shares
MYT Netherlands Parent B.V. American Depositary Shares each representing one Ordinary Share
Blackrock MuniYield Arizona Fund Inc. Common Stock
North Atlantic Acquisition Corporation Unit
Nuveen California Quality Municipal Income Fund
Nuveen Quality Municipal Income Fund Common Stock
Natural Alternatives International Inc. Common Stock
Northern Dynasty Minerals Ltd. Common Stock
Naked Brand Group Limited Ordinary Shares
Nuveen New York Quality Municipal Income Fund Common Stock
NanoVibronix Inc. Common Stock
Innovator Nasdaq-100 Power Buffer ETF - April
Inari Medical Inc. Common Stock
Nordic American Tankers Limited Common Stock
Nathan's Famous Inc. Common Stock
National Instruments Corporation Common Stock
Nature's Sunshine Products Inc. Common Stock
Navistar International Corporation Common Stock
Navistar International Corporation Preferred Stock
Navidea Biopharmaceuticals Inc. Common Stock
Navient Corporation Common Stock
Nuveen Arizona Quality Municipal Income Fund Common Stock
New Beginnings Acquisition Corp. Common Stock
Newborn Acquisition Corp. Ordinary Shares
Newborn Acquisition Corp. Right
Newborn Acquisition Corp. Unit
Newborn Acquisition Corp. Warrant
Nuveen Taxable Municipal Income Fund Common Shares of Beneficial Interest
NewAge Inc. Common Stock
Neuberger Berman Municipal Fund Inc. Common Stock
National Bank Holdings Corporation Common Stock
Neurocrine Biosciences Inc. Common Stock
Noble Midstream Partners LP Common Units Representing Limited Partner Interests
Northeast Bank Common Stock
Neuberger Berman New York Municipal Fund Inc. Common Stock
Nabors Industries Ltd.
Nabors Industries Ltd. 6.00% Mandatory Convertible Preferred Shares Series A
Nabriva Therapeutics plc Ordinary Shares Ireland
NeuBase Therapeutics Inc.  Common Stock
NBT Bancorp Inc. Common Stock
Nanobiotix S.A. American Depositary Shares
Neuberger Berman California Municipal Fund Inc Common Stock
NovaBay Pharmaceuticals Inc. Common Stock
NACCO Industries Inc. Common Stock
Nuveen California Municipal Value Fund Inc. Common Stock
Nuveen California Municipal Value Fund 2 Common Shares of Beneficial Interest
Nicolet Bankshares Inc. Common Stock
Norwegian Cruise Line Holdings Ltd. Ordinary Shares
National CineMedia Inc. Common Stock
NuCana plc American Depositary Share
nCino Inc. Common Stock
NCR Corporation Common Stock
NCS Multistage Holdings Inc. Common Stock
The9 Limited American Depository Shares
Virtus AllianzGI Convertible & Income Fund Common Shares of Beneficial Interest
Virtus AllianzGI Convertible & Income Fund 5.625% Series A Cumulative Preferred Shares
Virtus AllianzGI Convertible & Income Fund II Common Shares of Beneficial Interest
Virtus AllianzGI Convertible & Income Fund II 5.50% Series A Cumulative Preferred Shares
Nasdaq Inc. Common Stock
Noodles & Company Class A Common Stock
Nuveen Dynamic Municipal Opportunities Fund Common Shares of Beneficial Interest
Tortoise Energy Independence Fund Inc. Common Stock
ENDRA Life Sciences Inc. Common Stock
ENDRA Life Sciences Inc. Warrants
Nordson Corporation Common Stock
Nuveen AMT-Free Quality Municipal Income Fund Common Shares of Beneficial Interest Par Value $.01
Nebula Caravel Acquisition Corp. Class A Common Stock
Nebula Caravel Acquisition Corp. Unit
Nebula Caravel Acquisition Corp. Warrant
NextEra Energy Inc. Common Stock
NextEra Energy Inc. Series K Junior Subordinated Debentures due June 1 2076
NextEra Energy Inc. Series N Junior Subordinated Debentures due March 1 2079
NextEra Energy Inc. 4.872% Corporate Units
NextEra Energy Inc. 5.279% Corporate Units
NextEra Energy Inc. 6.219% Corporate Units
Newmont Corporation
New England Realty Associates Limited Partnership Class A Depositary Receipts Evidencing Units of Limited Partnership
NeoGenomics Inc. Common Stock
Neogen Corporation Common Stock
Neonode Inc. Common Stock
Neos Therapeutics Inc. Common Stock
NextEra Energy Partners LP Common Units representing limited partner interests
Nephros Inc. Common Stock
Neptune Wellness Solutions Inc. Ordinary Shares
Minerva Neurosciences Inc Common Stock
Nuverra Environmental Solutions Inc. Common Stock
National Energy Services Reunited Corp. Ordinary Shares
National Energy Services Reunited Corp. Warrant
Cloudflare Inc. Class A Common Stock
Net Element Inc. Common Stock
Eneti Inc. Common Stock
NewMarket Corp Common Stock
Nuveen Enhanced Municipal Value Fund Common Shares of Beneficial Interest
Puxin Limited American Depositary Shares each representing two Ordinary Shares
Newater Technology Inc. Ordinary Shares
New Relic Inc. Common Stock
Newtek Business Services Corp. Common Stock (Maryland)
Newtek Business Services Corp. 6.25% Notes Due 2023
Newtek Business Services Corp. 5.75% Notes due 2024
Newtek Business Services Corp. 5.50% Notes Due 2026
NexTier Oilfield Solutions Inc. Common Stock
Nexa Resources S.A. Common Shares
NexImmune Inc. Common Stock
NextDecade Corporation Common Stock
Northfield Bancorp Inc. Common Stock (Delaware)
New Fortress Energy Inc. Class A Common Stock
National Fuel Gas Company Common Stock
New Frontier Health Corporation Ordinary Shares
Virtus Dividend Interest & Premium Strategy Fund Common Shares of Beneficial Interest
Netflix Inc. Common Stock
Novagold Resources Inc.
Northern Genesis Acquisition Corp. Common Stock
NextGen Acquisition Corporation Class A Ordinary Shares
NextGen Acquisition Corporation Units
NextGen Acquisition Corporation Warrants
New Gold Inc.
National Grid Transco PLC National Grid PLC (NEW) American Depositary Shares
NGL ENERGY PARTNERS LP Common Units representing Limited Partner Interests
NGL ENERGY PARTNERS LP 9.00% Class B Fixed-to-Floating Rate Cumulative Redeemable Perpetual Preferred Units representing limited partnership interests
NGL ENERGY PARTNERS LP 9.625% Class C Fixed-to-Floating Rate Cumulative  Redeemable Perpetual Preferred Units representing  limited partner interests
NGM Biopharmaceuticals Inc. Common Stock
NeoGames S.A. Ordinary Shares
Natural Gas Services Group Inc. Common Stock
Natural Grocers by Vitamin Cottage Inc. Common Stock
Ingevity Corporation Common Stock 
NantHealth Inc. Common Stock
Nuveen Municipal 2021 Target Term Fund Fund
National HealthCare Corporation Common Stock
NexPoint Strategic Opportunities Fund
NexPoint Strategic Opportunities Fund 5.50% Series A Cumulative Preferred Shares
National Health Investors Inc. Common Stock
NewHold Investment Corp. Class A Common Stock
NewHold Investment Corp. Unit
NewHold Investment Corp. Warrant
National Holdings Corporation Common Stock
National Holdings Corporation Warrants
Neuberger Berman High Yield Strategies Fund
Natural Health Trends Corp. Common Stock
NiSource Inc Common Stock
NiSource Inc Depositary Shares representing 1/1000th ownership interest in a share of 6.50% Series B Preferred Stock and 1/1000th ownership interest in a share of Series B-1 Preferred Stock
NICE Ltd American Depositary Shares
Nicholas Financial Inc. Common Stock
Nuveen Intermediate Duration Municipal Term Fund Common Shares of Beneficial Interest
Virtus AllianzGI Equity & Convertible Income Fund Common Shares of Beneficial Interest
Nuveen Select Maturities Municipal Fund Common Stock
Nine Energy Service Inc. Common Stock
NIO Inc. American depositary shares each  representing one Class A ordinary share
Nuveenn Intermediate Duration Quality Municipal Term Fund Common Shares of Beneficial Interest
NiSun International Enterprise Development Group Co. Ltd. Class A Common Shares
Niu Technologies American Depositary Shares
NewJersey Resources Corporation Common Stock
Innovator Nasdaq-100 Power Buffer ETF - July
Nuveen New Jersey Municipal Value Fund Common Shares of Beneficial Interest
NantKwest Inc. Common Stock
Nike Inc. Common Stock
Nuveen Georgia Quality Municipal Income Fund 
Nikola Corporation Common Stock
National Bankshares Inc. Common Stock
Nektar Therapeutics  Common Stock
Nkarta Inc. Common Stock
Nuveen California AMT-Free Quality Municipal Income Fund
NL Industries Inc. Common Stock
NortonLifeLock Inc. Common Stock
Nautilus Inc. Common Stock
Nielsen N.V. Ordinary Shares
NLS Pharmaceutics Ltd. Ordinary Shares
NLS Pharmaceutics Ltd. Warrant
Neoleukin Therapeutics Inc. Common Stock
Annaly Capital Management Inc Common Stock
Annaly Capital Management Inc 6.95% Series F
Annaly Capital Management Inc 6.50% Series G Fixed-to-Floating Rate Cumulative Redeemable Preferred Stock
Annaly Capital Management Inc 6.750% Series I Fixed-to-Floating Rate Cumulative Redeemable Preferred Stock
Navios Maritime Holdings Inc. Common Stock
Navios Maritime Holdings Inc. Sponsored ADR Representing 1/100th Perpetual Preferred Series G (Marshall Islands)
Navios Maritime Holdings Inc. Sponsored ADR Representing 1/100th Perp. Preferred Series H%
Navios Maritime Containers L.P. Common Units
Nuveen Municipal Credit Opportunities Fund Common Shares
New Mountain Finance Corporation Common Stock
New Mountain Finance Corporation 5.75% Notes due 2023
Nuveen Municipal Income Fund Inc. Common Stock
NMI Holdings Inc. Class A Common Stock
Niagara Mohawk Holdings Inc. Preferred Stock
Niagara Mohawk Holdings Inc. Preferred Stock
Neuberger Berman MLP and Energy Income Fund Inc. Common Stock
Navios Maritime Partners LP Common Units Representing Limited Partner Interests
North Mountain Merger Corp. Class A Common Stock
North Mountain Merger Corp. Unit
North Mountain Merger Corp. Warrant
Nomura Holdings Inc ADR American Depositary Shares
Nemaura Medical Inc. Common Stock
Newmark Group Inc. Class A Common Stock
Nuveen Minnesota Quality Municipal Income Fund 
Nuveen Massachusetts Quality Municipal Income Fund Common Stock
9 Meters Biopharma Inc. Common Stock
Nuveen Maryland Quality Municipal Income Fund Common Stock
Nuveen Municipal High Income Opportunity Fund Common Stock $0.01 par value per share
Navios Maritime Acquisition Corporation Common stock
NN Inc. Common Stock
Nano Dimension Ltd. American Depositary Shares
Nelnet Inc. Common Stock
National Retail Properties Common Stock
National Retail Properties Depositary Shares each representing a 1/100th interest in a share of 5.20% Series F Cumulative Redeemable Preferred Stock
NANO-X IMAGING LTD Ordinary Shares
NanoViricides Inc. Common Stock
Nuveen New York Municipal Value Fund Inc. Common Stock
North American Construction Group Ltd. Common Shares (no par)
Natural Order Acquisition Corp. Common Stock
Natural Order Acquisition Corp. Unit
Natural Order Acquisition Corp. Warrant
Noah Holdings Limited
Northrop Grumman Corporation Common Stock
NI Holdings Inc. Common Stock
Northern Oil and Gas Inc. Common Stock
Nokia Corporation Sponsored American Depositary Shares
Nuveen Missouri Quality Municipal Income Fund 
Nomad Foods Limited Ordinary Shares
NOV Inc. Common Stock
Sunnova Energy International Inc. Common Stock
Novan Inc. Common Stock
Novanta Inc. Common Stock
ServiceNow Inc. Common Stock
Neenah Inc. Common Stock
New Providence Acquisition Corp. Class A Common Stock
New Providence Acquisition Corp. Unit
New Providence Acquisition Corp. Warrant
National Presto Industries Inc. Common Stock
Nuveen Pennsylvania Municipal Value Fund Common Shares of Beneficial Interest
EnPro Industries Inc
NeoPhotonics Corporation Common Stock
Nuveen Virginia Quality Municipal Income Fund Common Stock
Nuveen Pennsylvania Quality Municipal Income Fund Common Stock
Newpark Resources Inc. Common Stock
Noble Rock Acquisition Corporation Unit
NeuroBo Pharmaceuticals Inc. Common Stock
National Research Corporation Common Stock
NexPoint Real Estate Finance Inc. Common Stock
NexPoint Real Estate Finance Inc. 8.50% Series A Cumulative Redeemable Preferred Stock
NRG Energy Inc. Common Stock
PIMCO Energy and Tactical Credit Opportunities Fund Common Shares of Beneficial Interest
Northrim BanCorp Inc Common Stock
Nurix Therapeutics Inc. Common stock
Nuveen New York AMT-Free Quality Municipal Income Fund 
Neuberger Berman Real Estate Securities Income Fund Inc. Neuberger Berman Real Estate Securities Income Fund Inc.
Natural Resource Partners LP Limited Partnership
North European Oil Royality Trust Common Stock
National Rural Utilities Cooperative Finance Corporation 5.500% Subordinated Notes due 2064 (Subordinated Deferrable Interest Notes)
New Residential Investment Corp. Common Stock
New Residential Investment Corp. 7.50% Series A Fixed-to-Floating Rate Cumulative Redeemable Preferred Stock
New Residential Investment Corp. 7.125% Series B Fixed-to-Floating Rate Cumulative Redeemable Preferred Stock
New Residential Investment Corp. 6.375% Series C Fixed-to-Floating Rate Cumulative Redeemable Preferred Stock
Nustar Energy L.P.  Common Units
Nustar Energy L.P. 8.50% Series A Fixed-to-Floating Rate Cumulative Redeemable Perpetual Preferred Units
Nustar Energy L.P. 7.625% Series B Fixed-to-Floating Rate Cumulative Redeemable Perpetual Preferred Units representing limited partner interests
Nustar Energy L.P. 9.00% Series C Fixed-to-Floating Rate Cumulative Redeemable Perpetual Preferred Units
National Storage Affiliates Trust Common Shares of Beneficial Interest
National Storage Affiliates Trust 6.000% Series A Cumulative Redeemable Preferred Shares of Beneficial Interest (Liquidation Preference $25.00 per share)
Norfolk Southern Corporation Common Stock
Nesco Holdings Inc. Common Stock
National Security Group Inc. Common Stock
NavSight Holdings Inc. Class A Common Stock
Insight Enterprises Inc. Common Stock
Nuveen Senior Income Fund Common Stock
Insperity Inc. Common Stock
InspireMD Inc. Common Stock
NuStar Logistics L.P. 7.625% Fixed-to-Floating Rate Subordinated Notes due 2043
NAPCO Security Technologies Inc. Common Stock
Northern Star Investment Corp. II Class A Common stock
NanoString Technologies Inc. Common Stock
Nortech Systems Incorporated Common Stock
NetApp Inc. Common Stock
Bank of N.T. Butterfield & Son Limited (The) Voting Ordinary Shares
Natura &Co Holding S.A. American Depositary Shares 
NetScout Systems Inc. Common Stock
Intec Pharma Ltd. Ordinary Shares
NetEase Inc. American Depositary Shares
Tortoise Midstream Energy Fund Inc. Common Stock
NETGEAR Inc. Common Stock
Northern Technologies International Corporation Common Stock
Network-1 Technologies Inc. Common Stock
Intellia Therapeutics Inc. Common Stock
NTN Buzztime Inc. Common Stock
Nutanix Inc. Class A Common Stock
Nam Tai Property Inc. Common Stock
Nutrien Ltd. Common Shares
Natera Inc. Common Stock
Northern Trust Corporation Common Stock
Northern Trust Corporation Depositary Shares Each Representing a 1/1000th Interest in a Share of Series E Non-Cumulative Perpetual Preferred Stock
NetSTREIT Corp. Common Stock
Natus Medical Incorporated Common Stock
NetSol Technologies Inc. Common  Stock
Natuzzi S.p.A.
Nuance Communications Inc. Common Stock
Nucor Corporation Common Stock
Nuveen Ohio Quality Municipal Income Fund Common Stock
NeuroMetrix Inc. Common Stock
Nu Skin Enterprises Inc. Common Stock
Nuveen Municipal Value Fund Inc. Common Stock
NuVasive Inc. Common Stock
Nuvation Bio Inc. Class A Common Stock
Nuveen AMT-Free Municipal Value Fund
NuZee Inc. Common Stock
Novavax Inc. Common Stock
Neovasc Inc. Common Shares
NovoCure Limited Ordinary Shares
NVIDIA Corporation Common Stock
NVE Corporation Common Stock
NV5 Global Inc. Common Stock
Nova Lifestyle Inc. Common Stock
Nuveen AMT-Free Municipal Credit Income Fund 
Navigator Holdings Ltd. Ordinary Shares (Marshall Islands)
InVivo Therapeutics Holdings Corp Common Stock
Nova Measuring Instruments Ltd. Ordinary Shares
TrueShares Structured Outcome (November) ETF
Novo Nordisk A/S Common Stock
NVR Inc. Common Stock
Nevro Corp. Common Stock
Novartis AG Common Stock
New Vista Acquisition Corp Unit
Envista Holdings Corporation Common Stock
nVent Electric plc Ordinary Shares 
Invitae Corporation Common Stock
Northwest Bancshares Inc. Common Stock
NorthWestern Corporation Common Stock
Norwood Financial Corp. Common Stock
NatWest Group plc American Depositary Shares
New Home Company Inc. (The) Common Stock
Newell Brands Inc. Common Stock
National Western Life Group Inc. Class A Common Stock
Northwest Natural Holding Company Common Stock
Northwest Pipe Company Common Stock
News Corporation Class B Common Stock
News Corporation Class A Common Stock
Quanex Building Products Corporation Common Stock
Nuveen California Select Tax-Free Income Portfolio Common Stock
Nexgen Energy Ltd. Common Shares
NextGen Healthcare Inc. Common Stock
Nuveen New Jersey Qualified Municipal Fund 
Nuveen New York Select Tax-Free Income Portfolio Common Stock
Nuveen Select Tax Free Income Portfolio Common Stock
NXP Semiconductors N.V. Common Stock
Nuveen Select Tax Free Income Portfolio II Common Stock
Nuveen Select Tax Free Income Portfolio III Common Stock
NexPoint Residential Trust Inc. Common Stock
Nexstar Media Group Inc. Class A Common Stock
NextCure Inc. Common Stock
Nxt-ID Inc. Common Stock
New York City REIT Inc. Class A Common Stock
New York Community Bancorp Inc. Common Stock
New York Community Bancorp Inc. Depositary shares each representing a 1/40th interest in a share of Fixed-to-Floating Rate Series A Noncumulative Perpetual Preferred Stock
New York Community Bancorp Inc. New York Community Capital Tr V (BONUSES)
New York Mortgage Trust Inc. Common Stock
New York Mortgage Trust Inc. 7.875% Series E Fixed-to-Floating Rate Cumulative Redeemable Preferred Stock
New York Mortgage Trust Inc. 8.00% Series D Fixed-to-Floating Rate Cumulative Redeemable Preferred Stock
New York Mortgage Trust Inc. 7.875% Series C Cumulative Redeemable Preferred Stock
New York Mortgage Trust Inc. 7.75% Series B Cumulative Redeemable Preferred Stock
Nymox Pharmaceutical Corporation Common Stock (Bahamas)
New York Times Company (The) Common Stock
Nuveen New York Municipal Value Fund 2 Common Shares of Beneficial Interest
Nuveen Municipal Credit Income Fund 
Realty Income Corporation Common Stock
Oaktree Acquisition Corp. II Class A Ordinary Shares
Oaktree Capital Group LLC 6.625% Series A Preferred units
Oaktree Capital Group LLC 6.550% Series B Preferred Units
Oasis Petroleum Inc. Common Stock
Optibase Ltd. Ordinary Shares
Ocean Bio-Chem Inc. Common Stock
Oblong Inc. Common Stock
Obalon Therapeutics Inc. Common Stock
Origin Bancorp Inc. Common Stock
ObsEva SA Ordinary Shares
Owens Corning Inc Common Stock New
Omnichannel Acquisition Corp. Class A Common Stock
OCA Acquisition Corp. Unit
Optical Cable Corporation Common Stock
OFS Credit Company Inc. Common Stock
OFS Credit Company Inc. 6.875% Series A Term Preferred Stock
Ortho Clinical Diagnostics plc Ordinary Shares
OceanFirst Financial Corp. Common Stock
OceanFirst Financial Corp. Depositary Shares
OneConnect Financial Technology Co. Ltd. American Depositary Shares each representing three ordinary shares
Oriental Culture Holding LTD Ordinary Shares
Ocugen Inc. Common Stock
Ocwen Financial Corporation NEW Common Stock
Oaktree Strategic Income Corporation Common Stock
Oaktree Specialty Lending Corporation Common Stock
TrueShares Structured Outcome (October) ETF
Ocular Therapeutix Inc. Common Stock
Ocuphire Pharma Inc. Common Stock
OncoCyte Corporation Common Stock
Oil-Dri Corporation Of America Common Stock
Old Dominion Freight Line Inc. Common Stock
The ODP Corporation Common Stock
Odonate Therapeutics Inc. Common Stock
Orion Engineered Carbons S.A Common Shares
Orbital Energy Group Inc. Common Stock
One Equity Partners Open Water I Corp. Unit
Orion Energy Systems Inc. Common Stock
Corporate Office Properties Trust Common Stock
Oconee Federal Financial Corp. Common Stock
OFG Bancorp Common Stock
OFG Bancorp Preferred Stock
OFG Bancorp 7.0% Non Cumulative Monthly Income Preferred Stock Series B
OFG Bancorp 7.125% Non-Cumulative Perpetual Preferred Stock. Series D
Orthofix Medical Inc. Common Stock (DE)
Omega Flex Inc. Common Stock
OFS Capital Corporation Common Stock
OFS Capital Corporation 6.25% Notes Due 2023
OFS Capital Corporation 5.95% Notes due 2026
OFS Capital Corporation 6.375% Notes due 2025
OFS Capital Corporation 6.50% Notes due 2025
OGE Energy Corp Common Stock
Oragenics Inc. Common Stock
Organigram Holdings Inc. Common Shares
ONE Gas Inc. Common Stock
Omega Healthcare Investors Inc. Common Stock
O-I Glass Inc. Common Stock
Invesco Municipal Income Opportunities Trust Common Stock
Oceaneering International Inc. Common Stock
O2Micro International Limited American Depositary Shares
Oil States International Inc. Common Stock
ONEOK Inc. Common Stock
Okta Inc. Class A Common Stock
The OLB Group Inc. Common Stock
Universal Display Corporation Common Stock
Ollie's Bargain Outlet Holdings Inc. Common Stock
Olema Pharmaceuticals Inc. Common Stock
Olin Corporation Common Stock
One Liberty Properties Inc. Common Stock
Outset Medical Inc. Common Stock
Grupo Aeroportuario del Centro Norte S.A.B. de C.V. ADS
Omnicom Group Inc. Common Stock
Omnicell Inc. Common Stock ($0.001 par value)
Omega Alpha SPAC Class A Ordinary Shares
Omeros Corporation Common Stock
Odyssey Marine Exploration Inc. Common Stock
OneMain Holdings Inc. Common Stock
Owens & Minor Inc. Common Stock
Oasis Midstream Partners LP Common Units Representing Limited Partner Interests
ON Semiconductor Corporation Common Stock
Old National Bancorp Common Stock
Oncorus Inc. Common Stock
OncoSec Medical Incorporated Common Stock
Oncternal Therapeutics Inc. Common Stock
Oncolytics Biotech Inc. Common Shares
Ondas Holdings Inc. Common Stock
OneSmart International Education Group Limited ADS
1Life Healthcare Inc. Common Stock
OneWater Marine Inc. Class A Common Stock
ON24 Inc. Common Stock
Onto Innovation Inc. Common Stock
Onconova Therapeutics Inc. Common Stock
Onconova Therapeutics Inc. Warrants
Organovo Holdings Inc. Common Stock
Ooma Inc. Common Stock
OP Bancorp Common Stock
Option Care Health Inc. Common Stock
Opendoor Technologies Inc Common Stock
Opendoor Technologies Inc Warrants expiring 12/18/2025
OpGen Inc. Common Stock
OptimumBank Holdings Inc. Common Stock
Office Properties Income Trust Common Shares of Beneficial Interest
Office Properties Income Trust 5.875% Senior Notes due 2046
Office Properties Income Trust 6.375% Senior Notes due 2050
OPKO Health Inc. Common Stock
Opiant Pharmaceuticals Inc. Common Stock
Old Point Financial Corporation Common Stock
RiverNorth/DoubleLine Strategic Opportunity Fund Inc. Common Stock
RiverNorth/DoubleLine Strategic Opportunity Fund Inc. 4.375% Series A Cumulative Preferred Stock
Opera Limited American Depositary Shares
Oportun Financial Corporation Common Stock
OptimizeRx Corporation Common Stock
Opthea Limited American Depositary Shares
OptiNose Inc. Common Stock
Ocean Power Technologies Inc. Common Stock
Oppenheimer Holdings Inc. Class A Common Stock (DE)
Osisko Gold Royalties Ltd Common Shares
Ormat Technologies Inc. Common Stock
Orange
ORBCOMM Inc. Common Stock
Orchid Island Capital Inc. Common Stock
Owl Rock Capital Corporation Common Stock
Oracle Corporation Common Stock
Organogenesis Holdings Inc. Class A Common Stock
Orgenesis Inc. Common Stock
Old Republic International Corporation Common Stock
Oric Pharmaceuticals Inc. Common Stock
Orla Mining Ltd. Common Shares
O'Reilly Automotive Inc. Common Stock
Oramed Pharmaceuticals Inc. Common Stock
Orion Group Holdings Inc. Common
Orphazyme A/S American Depositary Shares
Orrstown Financial Services Inc Common Stock
Orchard Therapeutics plc American Depositary Shares
Old Second Bancorp Inc. Common Stock
Overseas Shipholding Group Inc. Class A Common Stock
Oak Street Health Inc. Common Stock
OSI Systems Inc. Common Stock (DE)
Oshkosh Corporation (Holding Company)Common Stock
Osmotica Pharmaceuticals plc Ordinary Shares
Ossen Innovation Co. Ltd. American Depositary Shares
OneSpan Inc. Common Stock
One Stop Systems Inc. Common Stock
Overstock.com Inc. Common Stock
Oyster Enterprises Acquisition Corp. Unit
OraSure Technologies Inc. Common Stock
OneSpaWorld Holdings Limited Common Shares
Otelco Inc. Class A Common Stock
Open Text Corporation Common Shares
Otonomy Inc. Common Stock
Otis Worldwide Corporation Common Stock 
Outlook Therapeutics Inc. Common Stock
Outlook Therapeutics Inc. Series A Warrant Expiring 02/18/2022
OTR Acquisition Corp. Class A Common Stock
OTR Acquisition Corp. Unit
OTR Acquisition Corp. Warrant
Ontrak Inc. Common Stock
Ontrak Inc. 9.50% Series A Cumulative Perpetual Preferred Stock
Otter Tail Corporation Common Stock
OUTFRONT Media Inc. Common Stock
Ohio Valley Banc Corp. Common Stock
Ovid Therapeutics Inc. Common Stock
Oak Valley Bancorp (CA) Common Stock
Ovintiv Inc. (DE)
Oxbridge Re Holdings Limited Ordinary Shares
Oxbridge Re Holdings Limited Warrant expiring 3/26/2024
Oxford Immunotec Global PLC Ordinary Shares
Oxford Lane Capital Corp. Common Stock
Oxford Lane Capital Corp. 6.75% Series 2024 Term Preferred Stock
Oxford Lane Capital Corp. Term Preferred Shares 7.50% Series 2023
Oxford Lane Capital Corp. 6.25% Series 2027 Term Preferred Shares
Oxford Industries Inc. Common Stock
Oxford Square Capital Corp. Common Stock
Oxford Square Capital Corp. 6.50% Notes due 2024
Oxford Square Capital Corp. 6.25% Notes due 2026
Occidental Petroleum Corporation Common Stock
Oyster Point Pharma Inc. Common Stock
Bank OZK Common Stock
Ozon Holdings PLC American Depositary Shares each ADS representing one ordinary share
Plains All American Pipeline L.P. Common Units representing Limited Partner Interests
Pan American Silver Corp. Common Stock
Grupo Aeroportuario Del Pacifico S.A. B. de C.V. Grupo Aeroportuario Del Pacifico S.A. de C.V. (each representing 10 Series B shares)
Pacific Biosciences of California Inc. Common Stock
TPG Pace Tech Opportunities Corp. Class A Ordinary Shares
Ranpak Holdings Corp Class A Common Stock
PacWest Bancorp Common Stock
Pioneer Merger Corp. Unit
PAE Incorporated Class A Common Stock
PAE Incorporated Warrants
Penske Automotive Group Inc. Common Stock
Plains GP Holdings L.P. Class A Units representing Limited Partner Interests
PagSeguro Digital Ltd. Class A Common Shares
Phibro Animal Health Corporation Class A Common Stock
Western Asset Investment Grade Income Fund Inc.
Petra Acquisition Inc. Common Stock
Petra Acquisition Inc. Units
Petra Acquisition Inc. Warrant
Pampa Energia S.A. Pampa Energia S.A.
Pandion Therapeutics Inc. Common Stock
Pangaea Logistics Solutions Ltd. Common Shares
Palo Alto Networks Inc. Common Stock
Provident Acquisition Corp. Units
PAR Technology Corporation Common Stock
Par Pacific Holdings Inc.  Common Stock
Passage Bio Inc. Common Stock
Patriot Transportation Holding Inc. Common Stock
Patrick Industries Inc. Common Stock
PAVmed Inc. Common Stock
PAVmed Inc. Warrant
PAVmed Inc. Series Z Warrant
Patria Investments Limited Class A Common Shares
Paya Holdings Inc. Class A Common Stock
Paya Holdings Inc. Warrant
Paycom Software Inc. Common Stock
Paysign Inc. Common Stock
Paychex Inc. Common Stock
Prosperity Bancshares Inc. Common Stock
Pembina Pipeline Corp. Ordinary Shares (Canada)
Prospect Capital Corporation 6.875% Notes due 2029
People's United Financial Inc. Common Stock
People's United Financial Inc. Perpetual Preferred Series A Fixed-to-floating Rate
PBF Energy Inc. Class A Common Stock
Pioneer Bancorp Inc. Common Stock
PBF Logistics LP Common Units representing limited partner interests
Prestige Consumer Healthcare Inc. Common Stock
Pathfinder Bancorp Inc. Common Stock (MD)
Pitney Bowes Inc. Common Stock
Pitney Bowes Inc 6.70% Notes Due 2043
Prudential Bancorp Inc. Common Stock
Panbela Therapeutics Inc. Common Stock
Potbelly Corporation Common Stock
Petroleo Brasileiro S.A.- Petrobras Common Stock
Permian Basin Royalty Trust Common Stock
Powerbridge Technologies Co. Ltd. Ordinary Shares
Prospect Capital Corporation 6.25% Notes due 2028
Puma Biotechnology Inc Common Stock
PACCAR Inc. Common Stock
PCB Bancorp Common Stock
High Income Securities Fund Common Stock
Pacific Gas & Electric Co. Common Stock
Pacific Gas & Electric Co. 6% Preferred Stock
Pacific Gas & Electric Co. 5 1/2% Preferred Stock
Pacific Gas & Electric Co. 5% 1st Preferred Stock
Pacific Gas & Electric Co. 5% 1st  Red. Preferred Stock
Pacific Gas & Electric Co. 4.80% 1st Preferred Stock
Pacific Gas & Electric Co. Equity Unit
PotlatchDeltic Corporation Common Stock
PIMCO Dynamic Credit and Mortgage Income Fund Common Shares of Beneficial Interest
Pimco California Municipal Income Fund II Common Shares of Beneficial Interest
PCM Fund Inc. Common Stock
Pimco Corporate & Income Strategy Fund Common Stock
Points International Ltd. Common Shares
Periphas Capital Partnering Corporation Class A Common Stock
PIMCO California Municipal Income Fund Common Stock
Pacira BioSciences Inc. Common Stock
Processa Pharmaceuticals Inc. Common Stock
PCSB Financial Corporation Common Stock
PCTEL Inc. Common Stock
Paylocity Holding Corporation Common Stock
Vaxcyte Inc. Common Stock
Park City Group Inc. Common Stock
Pure Cycle Corporation Common Stock
PagerDuty Inc. Common Stock
Peridot Acquisition Corp. Class A Ordinary Shares
PDC Energy Inc. Common Stock (Delaware)
Patterson Companies Inc. Common Stock
Pinduoduo Inc. American Depositary Shares
Pro-Dex Inc. Common Stock
PDF Solutions Inc. Common Stock
PIMCO Dynamic Income Fund Common Stock
PDL Community Bancorp Common Stock
Piedmont Office Realty Trust Inc. Class A Common Stock
PIMCO Dynamic Income Opportunities Fund Common Shares of Beneficial Interest
Precision Drilling Corporation Common Stock
PDS Biotechnology Corporation Common Stock
John Hancock Premium Dividend Fund
Healthpeak Properties Inc. Common Stock
Pebblebrook Hotel Trust Common Shares of Beneficial Interest
Pebblebrook Hotel Trust 6.50% Series C Cumulative Redeemable Preferred Shares of Beneficial Interest
Pebblebrook Hotel Trust 6.375% Series D Cumulative Redeemable Preferred Shares of Beneficial Interest
Pebblebrook Hotel Trust 6.375% Series E Cumulative Redeemable Preferred Shares of Beneficial Interest
Pebblebrook Hotel Trust 6.3% Series F Cumulative Redeemable Preferred Shares of Beneficial Interest
Peoples Bancorp of North Carolina Inc. Common Stock
Peoples Bancorp Inc. Common Stock
Pedevco Corp. Common Stock
Public Service Enterprise Group Incorporated Common Stock
Pegasystems Inc. Common Stock
Pennsylvania Real Estate Investment Trust Common Stock
Pennsylvania Real Estate Investment Trust Cumulative Redeemable Perpetual Preferred Shares Series B
Pennsylvania Real Estate Investment Trust 7.20% Series C Cumulative Redeemable Perpetual Preferred Shares
Pennsylvania Real Estate Investment Trust 6.875% Series D Cumulative Redeemable Perpetual Preferred Shares
Penumbra Inc. Common Stock
Penn National Gaming Inc. Common Stock
Adams Natural Resources Fund Inc. Common Stock
PepsiCo Inc. Common Stock
Perion Network Ltd. Ordinary Shares
Perma-Fix Environmental Services Inc. Common Stock
PetIQ Inc. Class A Common Stock
PetMed Express Inc. Common Stock
TDH Holdings Inc. Common Shares
Preferred Bank Common Stock
Premier Financial Bancorp Inc. Common Stock
Premier Financial Corp. Common Stock
Flaherty & Crumrine Preferred and Income Fund Incorporated
Pathfinder Acquisition Corporation Unit
Pfizer Inc. Common Stock
Principal Financial Group Inc Common Stock
Performance Food Group Company Common Stock
Prudential Financial Inc. 4.125% Junior Subordinated Notes due 2060
Professional Holding Corp. Class A Common stock
Profire Energy Inc. Common Stock
P & F Industries Inc. Class A Common Stock
Peoples Financial Services Corp. Common Stock
PIMCO Income Strategy Fund Shares of Beneficial Interest
PennantPark Floating Rate Capital Ltd. Common Stock
Performant Financial Corporation Common Stock
PIMCO Income Strategy Fund II
Flaherty & Crumrine Preferred and Income Opportunity Fund Incorporated
Proofpoint Inc. Common Stock
Provident Financial Services Inc Common Stock
PennyMac Financial Services Inc. Common Stock
PFSweb Inc. Common Stock
PhenixFIN Corporation Common Stock
PhenixFIN Corporation 6.125% Senior Notes due 2023
Procter & Gamble Company (The) Common Stock
Peapack-Gladstone Financial Corporation Common Stock
Precigen Inc. Common Stock
Progyny Inc. Common Stock
Pimco Global Stocksplus & Income Fund Pimco Global StocksPlus & Income Fund Common Shares of Beneficial Interest
Progressive Corporation (The) Common Stock
Paramount Group Inc. Common Stock
Progress Acquisition Corp. Units
PGT Innovations Inc.
Principal Real Estate Income Fund Common Shares of Beneficial Interest
Parker-Hannifin Corporation Common Stock
Pharming Group N.V. ADS each representing 10 ordinary shares
PhaseBio Pharmaceuticals Inc. Common Stock
Phathom Pharmaceuticals Inc. Common Stock
Puhui Wealth Investment Management Co. Ltd. Ordinary Shares
Pioneer Floating Rate Trust Pioneer Floating Rate Trust Shares of Beneficial Interest
Koninklijke Philips N.V. NY Registry Shares
BiomX Inc. COmmon Stock
PLDT Inc. Sponsored ADR
Population Health Investment Co. Inc. Class A Ordinary Share
Population Health Investment Co. Inc. Unit
Population Health Investment Co. Inc. Warrant
Phio Pharmaceuticals Corp. Common Stock
Phio Pharmaceuticals Corp. Warrants expiring 12/21/2021
Pimco High Income Fund Pimco High Income Fund
PulteGroup Inc. Common Stock
Phreesia Inc. Common Stock
Pioneer High Income Trust Common Shares of Beneficial Interest
Phunware Inc. Common Stock
Phunware Inc. Warrants
Pharvaris N.V. Ordinary Shares
PHX Minerals Inc. Common Stock
Impinj Inc. Common Stock
Prime Impact Acquisition I Class A Ordinary Shares
PICO Holdings Inc. Common Stock (DE)
Polaris Inc. Common Stock
Putnam Master Intermediate Income Trust Common Stock
Premier Inc. Class A Common Stock
Alpine Income Property Trust Inc. Common Stock
Ping Identity Holding Corp. Common Stock
Pinterest Inc. Class A Common Stock
Pine Island Acquisition Corp. Class A Common Stock
Piper Sandler Companies Common Stock
Pieris Pharmaceuticals Inc. Common Stock
ShiftPixy Inc. Common Stock
PJT Partners Inc. Class A Common Stock
Park Hotels & Resorts Inc. Common Stock 
Parke Bancorp Inc. Common Stock
Park Aerospace Corp. Common Stock
Packaging Corporation of America Common Stock
PerkinElmer Inc. Common Stock
Pimco Income Opportunity Fund Common Shares of Beneficial Interest
Park-Ohio Holdings Corp. Common Stock
POSCO Common Stock
Photronics Inc. Common Stock
Planet Green Holdings Corp. Common Stock
Anaplan Inc. Common Stock
Dave & Buster's Entertainment Inc. Common Stock
Plumas Bancorp
PLBY Group Inc. Common Stock
Children's Place Inc. (The) Common Stock
Prologis Inc. Common Stock
Platinum Group Metals Ltd. Ordinary Shares (Canada)
China Xiangtai Food Co. Ltd. Ordinary Shares
Piedmont Lithium Limited American Depositary Receipts
Polymet Mining Corporation Ordinary Shares (Canada)
Palomar Holdings Inc. Common stock
Planet Fitness Inc. Common Stock
Douglas Dynamics Inc. Common Stock
Preformed Line Products Company Common Stock
Pliant Therapeutics Inc. Common Stock
Pulse Biosciences Inc Common Stock (DE)
Plantronics Inc. Common Stock
Playtika Holding Corp. Common Stock
Palantir Technologies Inc. Class A Common Stock
Plug Power Inc. Common Stock
ePlus inc. Common Stock
Protalix BioTherapeutics Inc. (DE) Common Stock
PLx Pharma Inc. Common Stock
Plexus Corp. Common Stock
Playa Hotels & Resorts N.V. Ordinary Shares
Plymouth Industrial REIT Inc. Common Stock
Plymouth Industrial REIT Inc. 7.50% Series A Cumulative Redeemable Preferred Stock
Philip Morris International Inc Common Stock
Pacific Mercantile Bancorp Common Stock
Psychemedics Corporation
Pingtan Marine Enterprise Ltd.
PIMCO Municipal Income Fund Common Stock
Priveterra Acquisition Corp. Units
Pimco Municipal Income Fund II Common Shares of Beneficial Interest
Putnam Managed Municipal Income Trust Common Stock
Putnam Municipal Opportunities Trust Common Stock
PennyMac Mortgage Investment Trust Common Shares of Beneficial Interest
PennyMac Mortgage Investment Trust 8.125% Series A Fixed-to-Floating Rate Cumulative Redeemable Preferred Shares of Beneficial Interest
PennyMac Mortgage Investment Trust 8.00% Series B Fixed-to-Floating Rate Cumulative Redeemable Preferred Shares of Beneficial Interest
PMV Consumer Acquisition Corp. Class A Common Stock
PMV Pharmaceuticals Inc. Common Stock
PIMCO Municipal Income Fund III Common Shares of Beneficial Interest
Patriot National Bancorp Inc. Common Stock
PNC Financial Services Group Inc. (The) Common Stock
PNC Financial Services Group Inc. (The) Depositary Shares Representing 1/4000th Perpetual Preferred Series P
PIMCO New York Municipal Income Fund Common Stock
Pinnacle Financial Partners Inc. Common Stock
Pinnacle Financial Partners Inc. Depositary shares of Pinnacle Financial Partners Inc. each representing a 1/40th Interest in a share of its 6.75% Fixed-Rate Non-Cumulative Perpetual Preferred Stock Series B
Pimco New York Municipal Income Fund II Common Shares of Beneficial Interest
PNM Resources Inc. (Holding Co.) Common Stock
PennantPark Investment Corporation Common Stock
PennantPark Investment Corporation 5.50% Notes Due 2024
Pentair plc. Ordinary Share
PrimeEnergy Resources Corporation Common Stock
The Pennant Group Inc. Common Stock 
Pinnacle West Capital Corporation Common Stock
Predictive Oncology Inc. Common Stock
Insulet Corporation Common Stock
Polar Power Inc. Common Stock
Pool Corporation Common Stock
Portland General Electric Co Common Stock
Poshmark Inc. Class A Common Stock
Post Holdings Inc. Common Stock
Power Integrations Inc. Common Stock
Powell Industries Inc. Common Stock
Powered Brands Units
AMMO Inc. Common Stock
Pacific Premier Bancorp Inc
Purple Biotech Ltd. American Depositary Shares
Pilgrim's Pride Corporation Common Stock
PPD Inc. Common Stock
PPG Industries Inc. Common Stock
Poema Global Holdings Corp. Unit
Perma-Pipe International Holdings Inc. Common Stock
PPL Corporation Common Stock
Voya Prime Rate Trust Shares of Beneficial Interest
Pioneer Power Solutions Inc. Common Stock
Putnam Premier Income Trust Common Stock
Perpetua Resources Corp. Common Shares
PPL Capital Funding Inc. 2013 Series B Junior Subordinated Notes due 2073
PQ Group Holdings Inc. Common Stock
ProAssurance Corporation Common Stock
PRA Group Inc. Common Stock
PRA Health Sciences Inc. Common Stock
Praxis Precision Medicines Inc. Common Stock
Porch Group Inc. Common Stock
Porch Group Inc. Warrant
Perdoceo Education Corporation Common Stock
PartnerRe Ltd. 6.50% Series G Cumulative Redeemable Preferred Shares $1.00 par value
PartnerRe Ltd. 7.25% Series H Cumulative Redeemable Preferred Shares $1.00 par value
PartnerRe Ltd. 5.875% Series I Non-Cumulative Redeemable Preferred Shares $1.00 par value
Perficient Inc. Common Stock
PainReform Ltd. Ordinary Shares
PROG Holdings Inc. Common Stock
Perrigo Company plc Ordinary Shares
Progress Software Corporation Common Stock (DE)
PRGX Global Inc. Common Stock
Primerica Inc. Common Stock
Priority Income Fund Inc. 6.375% Series A Term Preferred Stock due 2025
Priority Income Fund Inc. 6.25% Series B Term Preferred Stock due 2023  par value $0.01 per share
Priority Income Fund Inc. 6.625% Series C Term Preferred Stock due 2024 par value $0.01 per share
Priority Income Fund Inc. 6.375% Series E Preferred Stock Due 2024
Priority Income Fund Inc. 6.625% Series F Term Preferred Stock due 2027
Primoris Services Corporation Common Stock
Park National Corporation Common Stock
Proto Labs Inc. Common stock
Prelude Therapeutics Incorporated Common Stock
Primo Water Corporation Common Stock
PROS Holdings Inc. Common Stock
Profound Medical Corp. Common Stock
Progenity Inc. Common Stock
ProSight Global Inc. Common Stock
Provident Financial Holdings Inc. Common Stock
CC Neuberger Principal Holdings II Class A Ordinary Shares
ProPhase Labs Inc. Common Stock (DE)
Purple Innovation Inc. Common Stock
Precipio Inc.  Common Stock
ProQR Therapeutics N.V. Ordinary Shares
Prudential Financial Inc. 5.625% Junior Subordinated Notes due 2058
Perspecta Inc. Common Stock 
Prospector Capital Corp. Unit
PermRock Royalty Trust Trust Units
Prothena Corporation plc Ordinary Shares
PureTech Health plc American Depositary Shares
Priority Technology Holdings Inc. Common Stock
Paratek Pharmaceuticals Inc. Common Stock
CarParts.com Inc. Common Stock
Party City Holdco Inc. Common Stock
Prudential Financial Inc. Common Stock
Provention Bio Inc. Common Stock
Pluralsight Inc. Class A Common Stock
Public Storage Common Stock
Public Storage Depositary Shares Each Representing 1/1000 of a 5.125% Cumulative Preferred Share of Beneficial Interest Series C
Public Storage Depositary Shares Each Representing 1/1000 of a 4.95% Cumulative Preferred Share of Beneficial Interest Series D
Public Storage Depositary Shares Each Representing 1/1000 of a 4.90% Cumulative Preferred Share of Beneficial Interest Series E
Public Storage Depositary Shares Each Representing 1/1000 of a 5.15% Cumulative Preferred Share of Beneficial Interest Series F par value $0.01 per share
Public Storage Depositary Shares Each Representing 1/1000 of a 5.05% Cumulative Preferred Share of Beneficial Interest Series G
Public Storage Depositary Shares Each Representing 1/1000 of a  5.60% Cumulative Preferred  Share of Beneficial Interest Series H
Public Storage Depositary Shares Each Representing 1/1000 of a 4.875% Cumulative Preferred Share of Beneficial Interest Series I par value $0.01 per share
Public Storage Depositary Shares Each Representing 1/1000 of a 4.700% Cumulative Preferred Share of Beneficial Interest Series J par value $0.01 per share
Public Storage Depositary Shares Each Representing 1/1000 of a 4.75% Cumulative Preferred Share of Beneficial Interest Series K
Public Storage Depositary Shares Each Representing 1/1000 of a 4.625% Cumulative Preferred Share of Beneficial Interest Series L par value $0.01 per share
Public Storage Depositary Shares Each Representing 1/1000 of a 4.125% Cumulative Preferred Share of Beneficial Interest Series M
Public Storage Depositary Shares Each Representing 1/1000 of a 3.875% Cumulative Preferred Share of Beneficial Interest Series N
Public Storage Depositary Shares Each Representing 1/1000 of a 3.900% Cumulative Preferred Share of Beneficial Interest Series O
Property Solutions Acquisition Corp. Common Stock
Property Solutions Acquisition Corp. Unit
Property Solutions Acquisition Corp. Warrant
PS Business Parks Inc. Common Stock
PS Business Parks Inc. Depositary Shares Each Representing 1/1000 of a Share of 5.20% Cumulative Preferred Stock Series W
PS Business Parks Inc. Depositary Shares Each Representing 1/1000 of a Share of 5.25% Cumulative Preferred Stock Series X
PS Business Parks Inc. 5.20% Cumulative Preferred Stock Series Y
PS Business Parks Inc. Depositary Shares Each Representing 1/1000 of a Share of 4.875% Cumulative Preferred Stock Series Z  par value $0.01 per share
Pacer Swan SOS Conservative (December) ETF
Prospect Capital Corporation Common Stock
Cohen & Steers Select Preferred and Income Fund Inc. Common Stock
Pacer Funds ETF
Pacer Swan SOS Fund of Funds ETF
Performance Shipping Inc. Common Shares
Pacer Swan SOS Moderate (December) ETF
PriceSmart Inc. Common Stock
Parsons Corporation Common Stock
Personalis Inc. Common Stock
Pearson Plc Common Stock
Pure Storage Inc. Class A Common Stock
Pershing Square Tontine Holdings Ltd. Class A Common Stock
Pluristem Therapeutics Inc. Common Stock
Postal Realty Trust Inc. Class A Common Stock
PLUS THERAPEUTICS Inc. Common Stock 
Poseida Therapeutics Inc. Common Stock
Phillips 66 Common Stock
Phillips 66 Partners LP Common Units representing limited partner interest in the Partnership
Pintec Technology Holdings Limited American Depositary Shares
Cohen & Steers Tax-Advantaged Preferred Securities and Income Fund Common Shares of Beneficial Interest
PTC Inc. Common Stock
PTC Therapeutics Inc. Common Stock
PolarityTE Inc. Common Stock
Patterson-UTI Energy Inc. Common Stock
Protagonist Therapeutics Inc. Common Stock
PropTech Investment Corporation II Class A Common Stock
PropTech Investment Corporation II Unit
PropTech Investment Corporation II Warrant
PTK Acquisition Corp. Common Stock
Portman Ridge Finance Corporation Common Stock
Palatin Technologies Inc. Common Stock
Partner Communications Company Ltd. American Depositary Shares
Peloton Interactive Inc. Class A Common Stock
Petros Pharmaceuticals Inc. Common Stock
PetroChina Company Limited Common Stock
Partners Bancorp Common Stock
P.A.M. Transportation Services Inc. Common Stock
Protective Insurance Corporation Class A Common Stock
Protective Insurance Corporation Class B Common Stock
Pactiv Evergreen Inc. Common stock
Pimco Corporate & Income Opportunity Fund
PubMatic Inc. Class A Common Stock
Goal Acquisitions Corp. Unit
Prudential Public Limited Company Common Stock
Prudential Public Limited Company 6.75% Perpetual Subordinated Captial Security
Prudential Public Limited Company 6.50% Perpetual Subordinated Capital Securities Exchangeable at the Issuer's Option Into Non-Cumulative Dollar Denominated Preference Shares
Pulmatrix Inc. Common Stock
ProPetro Holding Corp. Common Stock
Puyi Inc. American Depository Shares
Penn Virginia Corporation Common Stock
Provident Bancorp Inc. (MD) Common Stock
Pretium Resources Inc. Ordinary Shares (Canada)
PVH Corp. Common Stock
Permianville Royalty Trust Trust Units 
Power REIT (MD) Common Stock
Power REIT 7.75% Series A Cumulative Perpetual Preferred Stock
PowerFleet Inc. Common Stock
Penns Woods Bancorp Inc. Common Stock
Quanta Services Inc. Common Stock
Pioneer Natural Resources Company Common Stock
Pixelworks Inc.  Common Stock
Pyxis Tankers Inc. Common Stock
Pyxis Tankers Inc. 7.75% Series A Cumulative Convertible Preferred Shares
Pyxis Tankers Inc. Warrant
PIMCO New York Municipal Income Fund III Common Shares of Beneficial Interest
PolyPid Ltd. Ordinary Shares
PayPal Holdings Inc. Common Stock
Merrill Lynch Depositor Inc PPlus Tr Ser RRD-1 Tr Ctf Cl A
PPlus Tr GSC-2 Tr Ctf Fltg Rate
PIMCO California Municipal Income Fund III Common Shares of Beneficial Interest
Paramount Gold Nevada Corp. Common Stock
Pzena Investment Management Inc Class A Common Stock
Papa John's International Inc. Common Stock
QAD Inc. Class A Common Stock
QAD Inc. Class B Common Stock
QUALCOMM Incorporated Common Stock
American Century ETF Trust American Century Quality Convertible Securities ETF
QCR Holdings Inc. Common Stock
Qudian Inc. American Depositary Shares each representing one Class A Ordinary Share
FT Cboe Vest Growth-100 Buffer ETF - December
Quidel Corporation Common Stock
Qell Acquisition Corp. Class A Ordinary Shares
Qell Acquisition Corp. Unit
Qell Acquisition Corp. Warrant
QEP Resources Inc. Common Stock
360 DigiTech Inc. American Depositary Shares
Qiagen N.V. Common Shares 
Quhuo Limited American Depository Shares
QIWI plc American Depositary Shares
Q&K International Group Limited American Depositary Shares
Qualigen Therapeutics Inc. Common Stock
Qilian International Holding Group Ltd. Ordinary Shares
Qualys Inc. Common Stock
Quantum Corporation Common Stock
QuinStreet Inc. Common Stock
American Century ETF Trust American Century Quality Preferred ETF
Nuveen NASDAQ 100 Dynamic Overwrite Fund Shares of Beneficial Interest
Quest Resource Holding Corporation Common Stock
Qurate Retail Inc. Series A Common Stock 
Qurate Retail Inc. Series B Common Stock 
Qurate Retail Inc. 8.0% Fixed Rate Cumulative Redeemable Preferred Stock
Qorvo Inc. Common Stock
QuantumScape Corporation Class A Common Stock
Restaurant Brands International Inc. Common Shares
Quotient Limited Ordinary Shares
Quanterix Corporation Common Stock
QTS Realty Trust Inc. Class A Common Stock
QTS Realty Trust Inc. 7.125% Series A Cumulative Redeemable Perpetual Preferred Stock
QTS Realty Trust Inc. 6.50% Series B Cumulative Convertible Perpetual Preferred Stock
Qutoutiao Inc. American Depositary Shares
Q2 Holdings Inc. Common Stock
Quad Graphics Inc Class A Common Stock
QuickLogic Corporation Common Stock
Qumu Corporation Common Stock
Quotient Technology Inc. Common Stock
uniQure N.V. Ordinary Shares
QVC Inc. 6.250% Senior Secured Notes due 2068
QVC Inc. 6.375% Senior Secured Notes due 2067
Ryder System Inc. Common Stock
Brookfield Real Assets Income Fund Inc. Common Stock
Revolution Acceleration Acquisition Corp Class A Common Stock
Revolution Acceleration Acquisition Corp Unit
Revolution Acceleration Acquisition Corp Warrant
Cloopen Group Holding Limited American Depositary Shares each representing two Class A Ordinary Shares
Therapeutics Acquisition Corp. Class A Common Stock
Ferrari N.V. Common Shares
Rite Aid Corporation Common Stock
RADA Electronic Industries Ltd. Ordinary Shares
Radius Global Infrastructure Inc. Class A Common Stock
FreightCar America Inc. Common Stock
LiveRamp Holdings Inc. Common Stock
Rand Capital Corporation Common Stock
RAPT Therapeutics Inc. Common Stock
Ultragenyx Pharmaceutical Inc. Common Stock
Rave Restaurant Group Inc. Common Stock
Raven Industries Inc. Common Stock
Ritchie Bros. Auctioneers Incorporated Common Stock
RedBall Acquisition Corp. Class A Ordinary Shares
RBB Bancorp Common Stock
Ribbon Communications Inc. Common Stock
Regal Beloit Corporation Common Stock
Republic Bancorp Inc. Class A Common Stock
Rubicon Technology Inc. Common Stock
Rhinebeck Bancorp Inc. Common Stock
Reliant Bancorp Inc. Common Stock
Ready Capital Corproation Common Stock
Ready Capital Corporation 7.00% Convertible Senior Notes due 2023
Ready Capital Corporation 6.20% Senior Notes due 2026
Ready Capital Corporation 5.75% Senior Notes due 2026
Avita Therapeutics Inc. Common Stock
RENN Fund Inc Common Stock
Recharge Acquisition Corp. Class A Common Stock
Recharge Acquisition Corp. Unit
Recharge Acquisition Corp. Warrant
Rogers Communication Inc. Common Stock
Rent-A-Center Inc. Common Stock
Rocket Pharmaceuticals Inc. Common Stock
Rocky Brands Inc. Common Stock
D/B/A Royal Caribbean Cruises Ltd. Common Stock
Rosecliff Acquisition Corp I Unit
R1 RCM Inc. Common Stock
RCM Technologies Inc. Common Stock
Recon Technology Ltd. Ordinary Shares
Ready Capital Corporation 6.50% Senior Notes due 2021
PIMCO Strategic Income Fund Inc.
Arcus Biosciences Inc. Common Stock
Radcom Ltd. Ordinary Shares
Rareview Dynamic Fixed Income ETF
Redfin Corporation Common Stock
Redhill Biopharma Ltd. American Depositary Shares
Reading International Inc Class A Common Stock
Reading International Inc Class B Common Stock
Radian Group Inc. Common Stock
RadNet Inc. Common Stock
Royal Dutch Shell PLC
Radius Health Inc. Common Stock
Red Violet Inc. Common Stock 
Radware Ltd. Ordinary Shares
Dr. Reddy's Laboratories Ltd Common Stock
Everest Re Group Ltd. Common Stock
The RealReal Inc. Common Stock
Emles Real Estate Credit ETF
RISE Education Cayman Ltd American Depositary Shares
Reeds Inc. Common Stock
Research Frontiers Incorporated Common Stock
Regency Centers Corporation Common Stock
Renewable Energy Group Inc. Common Stock
Regeneron Pharmaceuticals Inc. Common Stock
Ring Energy Inc. Common Stock
Rekor Systems Inc. Common Stock
Reliance Global Group Inc. Common Stock
Reliance Global Group Inc. Series A Warrants
Richardson Electronics Ltd. Common Stock
RELX PLC PLC American Depositary Shares (Each representing One Ordinary Share)
Renren Inc. American Depositary Shares each representing fifteen Class A ordinary shares
Recro Pharma Inc. Common Stock
Replimune Group Inc. Common Stock
RPC Inc. Common Stock
Resonant Inc. Common Stock
Reata Pharmaceuticals Inc. Class A Common Stock
ReTo Eco-Solutions Inc. Common Shares
Revlon Inc. New Common Stock
REV Group Inc. Common Stock
REX American Resources Corporation
Rexford Industrial Realty Inc. Common Stock
Rexford Industrial Realty Inc. 5.875% Series A Cumulative Redeemable Preferred Stock
Rexford Industrial Realty Inc. 5.875% Series B Cumulative Redeemable Preferred Stock
Rexford Industrial Realty Inc. 5.625% Series C Cumulative Redeemable Preferred Stock par value $0.01 per share
Reynolds Consumer Products Inc. Common Stock
Resideo Technologies Inc. Common Stock 
Regions Financial Corporation Common Stock
Regions Financial Corporation Depositary Shares Representing 1/40th Perpetual Preferred Series A
Regions Financial Corporation Depositary Shares Representing 1/40th Perpetual Preferred Series B
Regions Financial Corporation Depositary Shares each Representing a 1/40th Interest in a  Share of 5.700% Fixed-to-Floating Rate Non-Cumulative  Perpetual Preferred Stock Series C
Cohen & Steers Total Return Realty Fund Inc. Common Stock
RF Industries Ltd. Common Stock
Rafael Holdings Inc. Class B Common Stock
RiverNorth Flexible Municipal Income Fund Inc. Common Stock
Resolute Forest Products Inc. Common Stock
Reinsurance Group of America Incorporated Common Stock
RGC Resources Inc. Common Stock
Repligen Corporation Common Stock
Royal Gold Inc. Common Stock
Regulus Therapeutics Inc. Common Stock
REGENXBIO Inc. Common Stock
Resources Connection Inc. Common Stock
Sturm Ruger & Company Inc. Common Stock
Regis Corporation Common Stock
Royce Global Value Trust Inc. Common Stock
RH Common Stock
Regional Health Properties Inc. Common Stock
Regional Health Properties Inc. 10.875% Series A Cumulative Redeemable Preferred Stock
Robert Half International Inc. Common Stock
Ryman Hospitality Properties Inc. (REIT)
RiceBran Technologies Common Stock
Rice Acquisition Corp. Class A Common Stock
RCI Hospitality Holdings Inc. Common Stock
Lordstown Motors Corp. Class A Common Stock
Transocean Ltd (Switzerland) Common Stock
Rigel Pharmaceuticals Inc. Common Stock
B. Riley Financial Inc. Common Stock
B. Riley Financial Inc. 7.25% Senior Notes due 2027
B. Riley Financial Inc. 7.375% Senior Notes due 2023
B. Riley Financial Inc. 6.875% Senior Notes due 2023
B. Riley Financial Inc. Depositary Shares each representing 1/1000th in a share of 7.375% Series B Cumulative Perpetual Preferred Stock par value $0.0001
B. Riley Financial Inc. 6.375% Senior Notes due 2025
B. Riley Financial Inc. 6.50% Senior Notes Due 2026
B. Riley Financial Inc. 6.75% Senior Notes due 2024
B. Riley Financial Inc. Depositary Shares each representing a 1/1000th fractional interest in a share of Series A Cumulative Perpetual Preferred Stock
B. Riley Financial Inc. 6.00% Senior Notes Due 2028
B. Riley Financial Inc. 7.50% Senior Notes Due 2027
Rio Tinto Plc Common Stock
Riot Blockchain Inc.  Common Stock 
RiverNorth Opportunities Fund Inc. Common Stock
Riverview Financial Corporation Common Stock
Raymond James Financial Inc. Common Stock
Arcadia Biosciences Inc. Common Stock
Rocket Companies Inc. Class A Common Stock
Ralph Lauren Corporation Common Stock
Relay Therapeutics Inc. Common Stock
Radiant Logistics Inc. Common Stock
Realogy Holdings Corp. Common Stock
Red Lions Hotels Corporation Common Stock
RLI Corp. Common Stock (DE)
RLJ Lodging Trust Common Shares of Beneficial Interest $0.01 par value
RLJ Lodging Trust $1.95 Series A Cumulative Convertible  Preferred Shares
Relmada Therapeutics Inc. Common Stock
RLX Technology Inc. American Depositary Shares each representing the right to receive one (1) Class A ordinary share
Regional Management Corp. Common Stock
RE/MAX Holdings Inc. Class A Common Stock
Richmond Mutual Bancorporation Inc. Common Stock
RumbleOn Inc. Class B Common Stock
Rambus Inc. Common Stock
Rocky Mountain Chocolate Factory Inc. Common Stock
ResMed Inc. Common Stock
Ra Medical Systems Inc. Common Stock
RMG Acquisition Corp. II Class A Ordinary Shares
RMG Acquisition Corp. II Unit
RMG Acquisition Corp. II Warrant
RMG Acquisition Corp. III Unit
RiverNorth Opportunistic Municipal Income Fund Inc. Common Stock
RiverNorth Managed Duration Municipal Income Fund Inc. Common Stock
Rimini Street Inc. (DE) Common Stock
Romeo Power Inc. Class A Common Stock
RiverNorth Specialty Finance Corporation 5.875% 
The RMR Group Inc. Class A Common Stock
RMR Mortgage Trust Common Stock
Royce Micro-Cap Trust Inc. Common Stock
Rockwell Medical Inc. (DE) Common Stock
Avidity Biosciences Inc. Common Stock
Randolph Bancorp Inc. Common Stock
RigNet Inc. Common Stock
RingCentral Inc. Class A Common Stock
Ranger Energy Services Inc. Class A Common Stock
Renalytix AI plc American Depositary Shares
Cohen & Steers REIT and Preferred and Income Fund Inc. Common Shares
RenaissanceRe Holdings Ltd. Common Stock
RenaissanceRe Holdings Ltd. 5.375% Series E Preference Shares
RenaissanceRe Holdings Ltd. Depositary Shares each Representing a 1/1000th Interest in a 5.750% Series F Preference Share
Renasant Corporation Common Stock
RealNetworks Inc. Common Stock
Construction Partners Inc. Class A Common Stock
Roth CH Acquisition II Co. Common Stock
Roth CH Acquisition II Co. Unit
Roth CH Acquisition II Co. Warrant
Roth CH Acquisition I Co. Common Stock
Roth CH Acquisition I Co. Unit
Roth CH Acquisition I Co. Warrant
Gibraltar Industries Inc. Common Stock
Rogers Corporation Common Stock
Retail Opportunity Investments Corp. Common Stock (MD)
Rockwell Automation Inc. Common Stock
Roku Inc. Class A Common Stock
Rollins Inc. Common Stock
RBC Bearings Incorporated Common Stock
Strategy Shares Newfound/ReSolve Robust Momentum ETF
Root Inc. Class A Common Stock
Roper Technologies Inc. Common Stock
Ross Stores Inc. Common Stock
RealPage Inc. Common Stock
Retail Properties of America Inc. Class A Common Stock
Repay Holdings Corporation Class A Common Stock
Rapid7 Inc. Common Stock
Replay Acquisition Corp. Ordinary Shares
RPM International Inc. Common Stock
Royalty Pharma plc Class A Ordinary Shares 
RPT Realty Common Stock
RPT Realty 7.25% 
Repare Therapeutics Inc. Common Shares
Cohen & Steers Quality Income Realty Fund Inc Common Shares
Red River Bancshares Inc. Common Stock
Range Resources Corporation Common Stock
R.R. Donnelley & Sons Company Common Stock
Red Robin Gourmet Burgers Inc. Common Stock
Red Rock Resorts Inc. Class A Common Stock
Reliance Steel & Aluminum Co. Common Stock (DE)
RiverNorth Specialty Finance Corporation
Republic Services Inc. Common Stock
Rush Street Interactive Inc. Class A Common Stock
Research Solutions Inc Common Stock
Rodgers Silicon Valley Acquisition Corp. Common Stock
Rodgers Silicon Valley Acquisition Corp. Unit
Rodgers Silicon Valley Acquisition Corp. Warrant
Rareview Tax Advantaged Income ETF
Rattler Midstream LP Common Units
Reinvent Technology Partners Class A Ordinary Shares
Reinvent Technology Partners Z Class A Ordinary Shares
Raytheon Technologies Corporation Common Stock
Rubius Therapeutics Inc. Common Stock
Ruhnn Holding Limited American Depositary Shares
Sunrun Inc. Common Stock
Rush Enterprises Inc. Common Stock Cl A
Rush Enterprises Inc. Class B
Ruth's Hospitality Group Inc. Common Stock
Retail Value Inc. Common Stock 
Revolve Group Inc. Class A Common Stock
Revolution Medicines Inc. Common Stock
Revance Therapeutics Inc. Common Stock
Retractable Technologies Inc. Common Stock
Reviva Pharmaceuticals Holdings Inc. Common Stock 
Reviva Pharmaceuticals Holdings Inc. Warrants
Riverview Bancorp Inc Common Stock
Royce Value Trust Inc. Common Stock
ReWalk Robotics Ltd. Ordinary Shares
Redwood Trust Inc. Common Stock
Rexnord Corporation Common Stock
Rackspace Technology Inc. Common Stock
Royal Bank Of Canada Common Stock
Royal Bank Of Canada 6.750% Fixed Rate/Floating Rate Noncumulative First Preferred Shares Series C-2
Ryanair Holdings plc American Depositary Shares
Rayonier Advanced Materials Inc. Common Stock
RYB Education Inc. American depositary shares each representing one Class A ordinary share
Ryerson Holding Corporation Common Stock
Rayonier Inc. REIT Common Stock
Rhythm Pharmaceuticals Inc. Common Stock
Reinsurance Group of America Incorporated 6.20% Fixed-to-Floating Rate Subordinated Debentures due 2042
Reinsurance Group of America Incorporated 5.75% Fixed-To-Floating Rate Subordinated Debentures due 2056
Rezolute Inc. Common Stock
Seabridge Gold Inc. Ordinary Shares (Canada)
Sabre Corporation Common Stock
Sabre Corporation 6.50% Series A Mandatory Convertible Preferred Stock
Sachem Capital Corp. 6.875% Notes due 2024
Sachem Capital Corp. Common Shares
Saratoga Investment Corp 6.25% Notes due 2023
Safehold Inc. Common Stock
Sanderson Farms Inc. Common Stock
Safety Insurance Group Inc. Common Stock
Sage Therapeutics Inc. Common Stock
Sonic Automotive Inc. Common Stock
Saia Inc. Common Stock
SCIENCE APPLICATIONS INTERNATIONAL CORPORATION Common Stock
Software Acquisition Group Inc. II Class A Common Stock
Software Acquisition Group Inc. II Unit
Software Acquisition Group Inc. II Warrant
SailPoint Technologies Holdings Inc. Common Stock
Saratoga Investment Corp 7.25% Notes due 2025
Salisbury Bancorp Inc. Common Stock
Salem Media Group Inc. Class A Common Stock
Boston Beer Company Inc. (The) Common Stock
Silvercrest Asset Management Group Inc. Class A Common Stock
Banco Santander S.A. Sponsored ADR (Spain)
Sana Biotechnology Inc. Common Stock
Sandstorm Gold Ltd. Ordinary Shares (Canada)
Sanmina Corporation Common Stock
S&W Seed Company Common Stock (NV)
SAP  SE ADS
Saratoga Investment Corp New
Sandy Spring Bancorp Inc. Common Stock
EchoStar  Corporation Common Stock
Cassava Sciences Inc. Common Stock
Spirit Airlines Inc. Common Stock
Safe Bulkers Inc Common Stock ($0.001 par value)
Safe Bulkers Inc Cumulative Redeemable Perpetual Preferred Series C (Marshall Islands)
Safe Bulkers Inc Perpetual Preferred Series D (Marshall Islands)
SBA Communications Corporation Class A Common Stock
Scorpio Tankers Inc. 7.00% Senior Notes due 2025
Strongbridge Biopharma plc Ordinary Shares
Seacoast Banking Corporation of Florida Common Stock
Switchback Energy Acquisition Corporation Class A Common Stock
SB Financial Group Inc. Common Stock
Sandbridge Acquisition Corporation Class A Common Stock
Sinclair Broadcast Group Inc. Class A Common Stock
Sally Beauty Holdings Inc. (Name to be changed from Sally Holdings Inc.) Common Stock
Western Asset Intermediate Muni Fund Inc Common Stock
Star Bulk Carriers Corp. Common Shares
Star Bulk Carriers Corp. 8.30% Senior Notes due 2022
Signature Bank Common Stock
Signature Bank Depositary shares each representing a 1/40th ownership interest in a share of 5.000% Noncumulative Perpetual Series A Preferred Stock
SilverBow Resorces Inc. Common Stock
Sabine Royalty Trust Common Stock
Sabra Health Care REIT Inc. Common Stock
Companhia de saneamento Basico Do Estado De Sao Paulo - Sabesp American Depositary Shares (Each repstg 250 Common Shares)
Southside Bancshares Inc. Common Stock
D/B/A Sibanye-Stillwater Limited ADS
Sterling Bancorp Inc. Common Stock
Silverback Therapeutics Inc. Common Stock
Starbucks Corporation Common Stock
Santander Consumer USA Holdings Inc. Common Stock
Sachem Capital Corp. 7.125% Notes due 2024
Sachem Capital Corp. 7.75% Notes due 2025
Southern Copper Corporation Common Stock
LMP Capital and Income Fund Inc. Common Stock
SCE Trust II Trust Preferred Securities
SCE Trust III Fixed/Floating Rate Trust Preference Securities
Southern California Edison Company 5.375% Fixed-to-Floating Rate Trust Preference Securities
Southern California Edison Company 5.45% Fixed-to-Floating Rate Trust Preference Securities
SCE TRUST VI
Scholastic Corporation Common Stock
Schnitzer Steel Industries Inc. Class A Common Stock
Charles Schwab Corporation (The) Common Stock
The Charles Schwab Corporation Depositary Shares each representing 1/40th interest in a share of 6% Non-Cumulative Perpetual Preferred Stock Series C
The Charles Schwab Corporation Depositary Shares each representing 1/40th interest in a share of 5.95% Non-Cumulative Perpetual Preferred Stock Series D
Service Corporation International Common Stock
Socket Mobile Inc. Common Stock
Stepan Company Common Stock
Broadscale Acquisition Corp. Units
Stellus Capital Investment Corporation Common Stock
ScION Tech Growth I Class A Ordinary Shares
ScION Tech Growth I Unit
ScION Tech Growth I Warrant
ScION Tech Growth II Units
comScore Inc. Common Stock
SC Health Corporation Class A Ordinary Shares
scPharmaceuticals Inc. Common Stock
SciPlay Corporation Class A Common Stock
Scopus BioPharma Inc. Common Stock
Steelcase Inc. Common Stock
ScanSource Inc. Common Stock
Sculptor Capital Management Inc. Class A Common Stock
Shoe Carnival Inc. Common Stock
SCVX Corp. Class A Ordinary Shares
SecureWorks Corp. Class A Common Stock
L.S. Starrett Company (The) Common Stock
SCYNEXIS Inc. Common Stock
SandRidge Energy Inc. Common Stock
Sustainable Development Acquisition I Corp. Unit
SmileDirectClub Inc. Class A Common Stock
Schrodinger Inc. Common Stock
Global Internet of People Inc. Ordinary Shares
PGIM Short Duration High Yield Opportunities Fund Common Shares
Superior Drilling Products Inc. Common Stock
Sea Limited American Depositary Shares each representing one Class A Ordinary Share
SeaChange International Inc. Common Stock
Sports Entertainment Acquisition Corp. Class A Common Stock
SeaWorld Entertainment Inc. Common Stock
Seaboard Corporation Common Stock
Secoo Holding Limited ADR
SolarEdge Technologies Inc. Common Stock
Sealed Air Corporation Common Stock
Origin Agritech Limited Common Stock
Seelos Therapeutics Inc. Common Stock
Seer Inc. Class A Common Stock
SEI Investments Company Common Stock
Selecta Biosciences Inc. Common Stock
Global Self Storage Inc. Common Stock
Select Medical Holdings Corporation Common Stock
Seneca Foods Corp. Class A Common Stock
Seneca Foods Corp. Class B Common Stock
Senseonics Holdings Inc. Common Stock
Listed Funds Trust TrueShares Structured Outcome (September) ETF
Sesen Bio Inc. Common Stock
Stifel Financial Corporation Common Stock
Stifel Financial Corporation Depositary Shares each representing a 1/1000th interest in a share of 6.25% Non-Cumulative Preferred Stock Series A
Stifel Financial Corporation Depositary Shares Each Representing 1/1000th  Interest in a Share of 6.25% Non-Cumulative  Preferred Stock Series B
Stifel Financial Corporation Depositary Shares Each Representing 1/1000th Interest in a Share of 6.125% Non Cumulative Preferred Stock Series C
Stifel Financial Corporation 5.20% Senior Notes due 2047
Sound Financial Bancorp Inc. Common Stock
ServisFirst Bancshares Inc. Common Stock
Safeguard Scientifics Inc. New Common Stock
Safe-T Group Ltd. American Depositary Share
Stitch Fix Inc. Class A Common Stock
SFL Corporation Ltd
Sprouts Farmers Market Inc. Common Stock
Simmons First National Corporation Class A Common Stock
Southern First Bancshares Inc. Common Stock
Shift Technologies Inc. Class A Common Stock
Osprey Technology Acquisition Corp. Class A Common Stock
Fang Holdings Limited American Depositary Shares (Each representing Four Class A Ordinary Shares HK$1.00 par value)
Sirius International Insurance Group Ltd. Common Share
Saga Communications Inc. Class A Common Stock (FL)
Seaport Global Acquisition Corp. Class A Common Stock
Seaport Global Acquisition Corp. Unit
Seaport Global Acquisition Corp. Warrant
SG Blocks Inc. Common Stock
Superior Group of Companies Inc. Common Stock
Seagen Inc. Common Stock
Signify Health Inc. Class A Common Stock
SMART Global Holdings Inc. Ordinary Shares
Sigma Labs Inc. Common Stock
Sigma Labs Inc. Warrant
SigmaTron International Inc. Common Stock
Sangamo Therapeutics Inc. Common Stock
Scientific Games Corp Common Stock
SGOCO Group Ltd Ordinary Shares (Cayman Islands)
SPAR Group Inc. Common Stock
Surgery Partners Inc. Common Stock
Sigilon Therapeutics Inc. Common Stock
Star Group L.P. Common Stock
SCP & CO Healthcare Acquisition Company Unit
Shake Shack Inc. Class A Common Stock
Shore Bancshares Inc Common Stock
Sotera Health Company Common Stock
Shenandoah Telecommunications Co Common Stock
Shinhan Financial Group Co Ltd American Depositary Shares
SINOPEC Shangai Petrochemical Company Ltd. Common Stock
Seanergy Maritime Holdings Corp Common Stock
Seanergy Maritime Holdings Corp Class A Warrants
Seanergy Maritime Holdings Corp Class B Warrant
Shoals Technologies Group Inc. Class A Common Stock
Shell Midstream Partners L.P. Common Units representing Limited Partner Interests
Sunstone Hotel Investors Inc. Sunstone Hotel Investors Inc. Common Shares
Sunstone Hotel Investors Inc. 6.950% Series E Cumulative Redeemable Preferred Stock
Sunstone Hotel Investors Inc. 6.450% Series F Cumulative Redeemable Preferred Stock
Steven Madden Ltd. Common Stock
Shopify Inc. Class A Subordinate Voting Shares
SharpSpring Inc. Common Stock
Sherwin-Williams Company (The) Common Stock
The Shyft Group Inc. Common Stock
Silvergate Capital Corporation Class A Common Stock
SI-BONE Inc. Common Stock
Select Interior Concepts Inc. Class A Common Stock
Companhia Siderurgica Nacional S.A. Common Stock
Siebert Financial Corp. Common Stock
Sientra Inc. Common Stock
SIFCO Industries Inc. Common Stock
Sify Technologies Limited American Depositary Shares
Signet Jewelers Limited Common Shares
SIGA Technologies Inc. Common Stock
Selective Insurance Group Inc. Common Stock
Selective Insurance Group Inc. Depositary Shares each representing a 1/1000th interest in a share of 4.60% Non-Cumulative Preferred Stock Series B
Sprott Inc. Common Shares
Silicom Ltd Ordinary Shares
Silk Road Medical Inc. Common Stock
SilverCrest Metals Inc. Common Shares
Grupo Simec S.A.B. de C.V. American Depositary Shares
Silicon Motion Technology Corporation American Depositary Shares
SINA Corporation Ordinary Shares
Sino-Global Shipping America Ltd. Common Stock
SiNtx Technologies Inc. Common Stock
Sio Gene Therapies Inc. Common Stock
Sirius XM Holdings Inc. Common Stock
SITE Centers Corp. Common Stock
SITE Centers Corp. 6.375% Class A Preferred Shares
SITE Centers Corp. DEPOSITARY SH REPSTG 1/20TH PDF CL K % (United States)
SiteOne Landscape Supply Inc. Common Stock
SiTime Corporation Common Stock
SVB Financial Group Common Stock
SVB Financial Group Depositary Shs each representing a 1/40th interest in a share of 5.25% Fixed-Rate Non-Cumulative Perpetual Preferred Stock Series A
Six Flags Entertainment Corporation New Common Stock
Scienjoy Holding Corporation Ordinary Shares
South Jersey Industries Inc. Common Stock
South Jersey Industries Inc. 5.625% Junior Subordinated Notes due 2079
South Jersey Industries Inc. Corporate Units
J.M. Smucker Company (The) New Common Stock
Shaw Communications Inc. Common Stock
San Juan Basin Royalty Trust Common Stock
SJW Group Common Stock (DE)
Skillz Inc. Class A Common Stock
SK Telecom Co. Ltd. Common Stock
Tanger Factory Outlet Centers Inc. Common Stock
Skechers U.S.A. Inc. Common Stock
Skyline Champion Corporation Common Stock
SkyWest Inc. Common Stock
Silicon Laboratories Inc. Common Stock
Schlumberger N.V. Common Stock
U.S. Silica Holdings Inc. Common Stock
Silver Crest Acquisition Corporation Unit
Select Bancorp Inc. Common Stock
Solid Biosciences Inc. Common Stock
Sun Life Financial Inc. Common Stock
SL Green Realty Corp Common Stock
SL Green Realty Corporation Preferred Series I
Super League Gaming Inc. Common Stock
Sol-Gel Technologies Ltd. Ordinary Shares
Silgan Holdings Inc. Common Stock
SLM Corporation Common Stock
SLM Corporation Floating Rate Non-Cumulative Preferred Stock Series B
Silence Therapeutics Plc American Depository Share
Soleno Therapeutics Inc. Common Stock
Simulations Plus Inc. Common Stock
SelectQuote Inc. Common Stock
Solar Capital Ltd. Common Stock
Salarius Pharmaceuticals Inc. Common Stock
SELLAS Life Sciences Group Inc. Common Stock
SM Energy Company Common Stock
Smartsheet Inc. Class A Common Stock
Southern Missouri Bancorp Inc. Common Stock
SmartFinancial Inc. Common Stock
Super Micro Computer Inc. Common Stock
Sharps Compliance Corp. Common Stock
Sumitomo Mitsui Financial Group Inc Unsponsored American Depositary Shares (Japan)
Scotts Miracle-Gro Company (The) Common Stock
SEACOR Marine Holdings Inc. Common Stock 
Smith-Midland Corporation Common Stock
Schmitt Industries Inc. Common Stock
Summit Midstream Partners LP Common Units Representing Limited Partner Interests
Salient Midstream Common Shares of Beneficial Interest
Summit Financial Group Inc. Common Stock
Summit Therapeutics Inc. Common Stock 
Standard Motor Products Inc. Common Stock
The Simply Good Foods Company Common Stock
Smith Micro Software Inc. Common Stock
Semtech Corporation Common Stock
Sanara MedTech Inc. Common Stock
Sierra Metals Inc. Common Stock
SMTC Corporation Common Stock
Snap-On Incorporated Common Stock
Snap Inc. Class A Common Stock
Sleep Number Corporation Common Stock
Seneca Biopharma Inc. Common Stock
Synchronoss Technologies Inc. Common Stock
Smart Sand Inc. Common Stock
Sundance Energy Inc. Common Stock 
Sundial Growers Inc. Common Shares
Schneider National Inc. Common Stock
Syndax Pharmaceuticals Inc. Common Stock
Sony Corporation Common Stock
SenesTech Inc. Common Stock
StoneX Group Inc. Common Stock
Security National Financial Corporation Class A Common Stock
Soligenix Inc. Common Stock
Soligenix Inc. Warrant
Sanchez Midstream Partners LP Common Stock
Smith & Nephew SNATS Inc. Common Stock
Sonoma Pharmaceuticals Inc. Common Stock
Snowflake Inc. Class A Common Stock
China Petroleum & Chemical Corporation Common Stock
Tortoise Acquisition Corp. II Class A Ordinary Shares
Synopsys Inc. Common Stock
New Senior Investment Group Inc. Common Stock
Senior Connect Acquisition Corp. I Class A Common Stock
Senior Connect Acquisition Corp. I Unit
Senior Connect Acquisition Corp. I Warrant
Sensei Biotherapeutics Inc. Common Stock
Sunesis Pharmaceuticals Inc. Common Stock
Synovus Financial Corp. Common Stock
Synovus Financial Corp. Fixed-to-Floating Rate Non-Cumulative Perpetual Preferred Stock Series D Liquation Preference $25.00 per Share
Synovus Financial Corp. 5.875% Fixed-Rate Reset Non-Cumulative Perpetual Preferred Stock Series E
Synnex Corporation Common Stock
Sanofi ADR
Southern Company (The) Common Stock
Sustainable Opportunities Acquisition Corp. Class A Ordinary Shares
Sogou Inc. American Depositary Shares each representing one Class A Ordinary Share
Sotherly Hotels Inc. Common Stock
Sotherly Hotels Inc. 8.0% Series B Cumulative Redeemable Perpetual Preferred Stock
Sotherly Hotels Inc. 8.25% Series D Cumulative Redeemable Perpetual Preferred Stock
Sotherly Hotels Inc. 7.875% Series C Cumulative Redeemable Perpetual Preferred Stock
Sohu.com Limited American Depositary Shares
Solaris Oilfield Infrastructure Inc. Class A Common Stock
Southern Company (The) Series 2016A 5.25% Junior Subordinated Notes due October 1 2076
Southern Company (The) Series 2017B 5.25% Junior Subordinated Notes due December 1 2077
Southern Company (The) Series 2020A 4.95% Junior Subordinated Notes due January 30 2080
Southern Company (The) Series 2020C 4.20% Junior Subordinated Notes due October 15 2060
Renesola Ltd. American Depsitary Shares (Each representing 10 shares)
Southern Company (The) 2019 Series A Corporate Units
Electrameccanica Vehicles Corp. Ltd. Common Stock
Electrameccanica Vehicles Corp. Ltd. Warrants
Soliton Inc. Common Stock
Sonoco Products Company Common Stock
Southern National Bancorp of Virginia Inc. Common Stock
Sonim Technologies Inc. Common Stock
Sonnet BioTherapeutics Holdings Inc. Common Stock
Sonos Inc. Common Stock
Source Capital Inc. Common Stock
SOS Limited American Depositary Shares
SP Plus Corporation Common Stock
Spectrum Brands Holdings Inc. Common Stock
SuperCom Ltd. Ordinary Shares (Israel)
Virgin Galactic Holdings Inc. Common Stock
Special Opportunities Fund Inc Common Stock
Special Opportunities Fund Inc. 3.50% Convertible Preferred Stock Series B
South Plains Financial Inc. Common Stock
Jaws Spitfire Acquisition Corporation Class A Ordinary Shares
Simon Property Group Inc. Common Stock
Simon Property Group Inc. Simon Property Group 8 3/8% Series J Cumulative Redeemable Preferred Stock
S&P Global Inc. Common Stock
Suburban Propane Partners L.P. Common Stock
SPI Energy Co. Ltd. Ordinary Shares
Spark Energy Inc. Class A Common Stock
Spark Energy Inc. 8.75% Series A Fixed-to-Floating Rate Cumulative Redeemable Perpetual Preferred Stock
Splunk Inc. Common Stock
Steel Partners Holdings LP LTD PARTNERSHIP UNIT
Steel Partners Holdings LP 6.0% Series A Preferred Units no par value
SeaSpine Holdings Corporation Common Stock
Sapiens International Corporation N.V. Common Shares (Cayman Islands)
Supernova Partners Acquisition Company Inc. Class A Common Stock
Spok Holdings Inc. Common Stock
Spotify Technology S.A. Ordinary Shares
Spectrum Pharmaceuticals Inc.Common Stock
Spirit Aerosystems Holdings Inc. Common Stock
Spruce Biosciences Inc. Common Stock
Spero Therapeutics Inc. Common Stock
Spartan Acquisition Corp. II Class A Common Stock
Support.com Inc. Common Stock
SPS Commerce Inc. Common Stock
Sprout Social Inc Class A Common Stock
SportsTek Acquisition Corp. Unit
SpartanNash Company Common Stock
Sportsman's Warehouse Holdings Inc. Common Stock
SunPower Corporation Common Stock
SPX Corporation Common Stock
Nuveen S&P 500 Dynamic Overwrite Fund
Square Inc. Class A Common Stock
Sequential Brands Group Inc. Common Stock
Presidio Property Trust Inc. Class A Common Stock
Sociedad Quimica y Minera S.A. Common Stock
Sequans Communications S.A. American Depositary Shares
SQZ Biotechnologies Company Common Stock
Spire Inc. Common Stock
Spire Inc. Depositary Shares each representing a 1/1000th interest in a share of 5.90% Series A Cumulative Redeemable Perpetual Preferred Stock
Stable Road Acquisition Corp. Class A Common Stock
Stable Road Acquisition Corp. Unit
Stable Road Acquisition Corp. Warrant
SRAX Inc. Class A Common Stock
Spirit Realty Capital Inc. Common Stock
Spirit Realty Capital Inc. 6.000% Series A Cumulative Redeemable Preferred Stock
1st Source Corporation Common Stock
Stericycle Inc. Common Stock
Surmodics Inc. Common Stock
Sempra Energy Common Stock
Sempra Energy 6.75% Mandatory Convertible Preferred Stock Series B
Sempra Energy 5.750% Junior Subordinated Notes due 2079
ServiceSource International Inc. Common Stock
Seritage Growth Properties Class A Common Stock
Seritage Growth Properties 7.00% Series A Cumulative Redeemable Preferred Shares of Beneficial Interest
Surgalign Holdings Inc. Common Stock
Stoneridge Inc. Common Stock
Scully Royalty Ltd.
Sprague Resources LP Common Units representing Limited Partner Interests
Sorrento Therapeutics Inc.  Common Stock
Sarepta Therapeutics Inc. Common Stock (DE)
Sierra Oncology Inc. Common Stock
Scholar Rock Holding Corporation Common Stock
Sarissa Capital Acquisition Corp. Class A Ordinary Shares
Sarissa Capital Acquisition Corp. Unit
Sarissa Capital Acquisition Corp. Warrants
StarTek Inc. Common Stock
Sensus Healthcare Inc. Common Stock
Cushing MLP & Infrastructure Total Return Fund
Science Strategic Acquisition Corp. Alpha Unit
South State Corporation Common Stock
Summit State Bank Common Stock
Simpson Manufacturing Company Inc. Common Stock
Strata Skin Sciences Inc. Common Stock
Sasol Ltd. American Depositary Shares
SS&C Technologies Holdings Inc. Common Stock
SilverSun Technologies Inc. Common Stock
E.W. Scripps Company (The) Class A Common Stock
Silver Spike Acquisition Corp. Class A Ordinary Shares
Silver Spike Acquisition Corp. Units
Silver Spike Acquisition Corp. Warrants
SSR Mining Inc. Common Stock
SuRo Capital Corp. Common Stock
ShotSpotter Inc. Common Stock
Shutterstock Inc. Common Stock
SunLink Health Systems Inc. Common Stock
Stratasys Ltd. Ordinary Shares (Israel)
Sensata Technologies Holding plc Ordinary Shares
STAAR Surgical Company Common Stock
Staffing 360 Solutions Inc. Common Stock (DE)
Stag Industrial Inc. Common Stock
Stag Industrial Inc. 6.875% Series C Cumulative Redeemable Preferred Stock
iStar Inc. Common Stock
iStar Inc. Series D Cumulative Redeemable Preferred Stock
iStar Inc. Series G Cumulative Redeemable Preferred Stock
iStar Inc. Series I Cumulative Redeemable Preferred Stock
Extended Stay America Inc. Paired Shares
S&T Bancorp Inc. Common Stock
Stewart Information Services Corporation Common Stock
Steel Connect Inc. Common Stock
STERIS plc (Ireland) Ordinary Shares
StepStone Group Inc. Class A Common Stock
State Auto Financial Corporation Common Stock
Sunlands Technology Group American Depositary Shares representing Class A ordinary shares
Northern Star Acquisition Corp. Class A Common Stock
Neuronetics Inc. Common Stock
Columbia Seligman Premium Technology Growth Fund Inc
SunOpta Inc. Common Stock
The ONE Group Hospitality Inc. Common Stock
Sterling Bancorp
Sterling Bancorp Depositary Shares each representing ownership of a 1/40th interest in a share of 6.50% Non-Cumulative Perpetual Preferred Stock Series A
Stellantis N.V. Common Shares
Steel Dynamics Inc.
STMicroelectronics N.V. Common Stock
Stamps.com Inc.  Common Stock ($0.001 Par Value)
Stantec Inc Common Stock
Standard AVB Financial Corp. Common Stock
StoneCo Ltd. Class A Common Shares
Scorpio Tankers Inc. Common Shares
Stoke Therapeutics Inc. Common Stock
StoneMor Inc. Common Stock
STORE Capital Corporation Common Stock
Star Peak Energy Transition Corp. Class A Common Stock
Strategic Education Inc. Common Stock
Sterling Construction Company Inc Common Stock
Streamline Health Solutions Inc. Common Stock
Sutro Biopharma Inc. Common Stock
Star Equity Holdings Inc. Common Stock
Star Equity Holdings Inc. Series A Cumulative Perpetual Preferred Stock
Stratus Properties Inc. Common Stock
STRATTEC SECURITY CORPORATION Common Stock
Satsuma Pharmaceuticals Inc. Common Stock
State Street Corporation Common Stock
State Street Corporation Depositary Shares representing 1/4000th Perpetual Preferred Series D
State Street Corporation Depositary shares each representing a 1/4000th ownership interest in a share of Fixed-to-Floating Rate Non-Cumulative
Shattuck Labs Inc. Common Stock
STARWOOD PROPERTY TRUST INC. Starwood Property Trust Inc.
ACON S2 Acquisition Corp. Class A Ordinary Shares
ACON S2 Acquisition Corp. Unit
ACON S2 Acquisition Corp. Warrant
Seagate Technology PLC Ordinary Shares (Ireland)
Spirit of Texas Bancshares Inc. Common Stock
Stereotaxis Inc. Common Stock
Constellation Brands Inc. Common Stock
Constellation Brands Inc
Suncor Energy  Inc. Common Stock
Sun Communities Inc. Common Stock
SmartETFs Sustainable Energy II ETF
Summit Materials Inc. Class A Common Stock
Sumo Logic Inc. Common Stock
Summer Infant Inc. Common Stock
Sunoco LP Common Units representing limited partner interests
Solar Senior Capital Ltd. Common Stock
Sunworks Inc. Common Stock
Superior Industries International Inc. Common Stock (DE)
Supernus Pharmaceuticals Inc. Common Stock
Grupo Supervielle S.A. American Depositary Shares each Representing five Class B shares
Surface Oncology Inc. Common Stock
Suzano S.A. American Depositary Shares (each representing One Ordinary Share)
Spring Valley Acquisition Corp. Class A Ordinary Share
Starboard Value Acquisition Corp. Class A Common Stock
Starboard Value Acquisition Corp. Unit
Starboard Value Acquisition Corp. Warrant
iShares US Small Cap Value Factor ETF
Severn Bancorp Inc
Service Properties Trust Common Stock
SVF Investment Corp. Class A Ordinary Shares
SVF Investment Corp. Unit
SVF Investment Corp. Warrant
Silvercorp Metals Inc. Common Shares
SVMK Inc. Common Stock
Seven Oaks Acquisition Corp. Class A Common Stock
Seven Oaks Acquisition Corp. Unit
Seven Oaks Acquisition Corp. Warrant
Savara Inc. Common Stock
Spring Valley Acquisition Corp. Unit
Spring Valley Acquisition Corp. Warrant
Servotronics Inc. Common Stock
Firsthand Technology Value Fund Inc. Common Stock
ShockWave Medical Inc. Common Stock
Smith & Wesson Brands Inc. Common Stock
Switch Inc. Class A Common Stock
Athlon Acquisition Corp. Unit
SolarWinds Corporation Common Stock
Sierra Wireless Inc. Common Stock
Stanley Black & Decker Inc. Common Stock
SWK Holdings Corporation Common Stock
Skyworks Solutions Inc. Common Stock
Schweitzer-Mauduit International Inc. Common Stock
Southwestern Energy Company Common Stock
Stanley Black & Decker Inc. Corporate Unit
SpringWorks Therapeutics Inc. Common Stock
Southwest Gas Holdings Inc. Common Stock (DE)
Swiss Helvetia Fund Inc. (The) Common Stock
SunCoke Energy Inc. Common Stock
Standex International Corporation Common Stock
Sensient Technologies Corporation Common Stock
China SXT Pharmaceuticals Inc. Ordinary Shares
So-Young International Inc. American Depository Shares
Stock Yards Bancorp Inc. Common Stock
Synlogic Inc. Common Stock
Synchrony Financial Common Stock
Synchrony Financial Depositary Shares each Representing a 1/40th Interest in a Share of 5.625% Fixed Rate Non-Cumulative Perpetual Preferred Stock Series A
Stryker Corporation Common Stock
Sykes Enterprises Incorporated Common Stock
Synthetic Biologics Inc. Common Stock
Synaptics Incorporated Common Stock $0.001 Par Value
Synacor Inc. Common Stock
Syneos Health Inc. Class A Common Stock
Synalloy Corporation Common Stock
Sypris Solutions Inc. Common Stock
Syros Pharmaceuticals Inc. Common Stock
Siyata Mobile Inc. Common Shares
Siyata Mobile Inc. Warrant
Systemax Inc. Common Stock
Sysco Corporation Common Stock
Cushing NextGen Infrastructure Income Fund Common Shares of Beneficial Interest
AT&T Inc.
AT&T Inc. Depositary Shares each representing a 1/1000th interest in a share of 5.000% Perpetual Preferred Stock Series A
AT&T Inc. Depositary Shares each representing a 1/1000th interest in a share of 4.750% Perpetual Preferred Stock Series C
TravelCenters of America Inc. Common Stock
TransAlta Corporation Ordinary Shares
Trepont Acquisition Corp I Class A Ordinary Shares
Del Taco Restaurants Inc. Common Stock
TransAct Technologies Incorporated Common Stock
Trend Aggregation U.S. ETF
Taitron Components Incorporated Class A Common Stock
Takeda Pharmaceutical Company Limited American Depositary Shares (each representing 1/2 of a share of Common Stock)
TAL Education Group American Depositary Shares
Talos Energy Inc. Common Stock
Tantech Holdings Ltd. Common Stock
TravelCenters of America Inc. 8.25% Senior Notes due 2028
TravelCenters of America Inc. 8.00% Senior Notes due 2029
TravelCenters of America Inc. 8.00% Senior Notes due 2030
Taoping Inc. Ordinary Shares 
Molson Coors Beverage Company Class B Common Stock
Protara Therapeutics Inc.  Common Stock
Taro Pharmaceutical Industries Ltd. Ordinary Shares
Tarsus Pharmaceuticals Inc. Common Stock
Carrols Restaurant Group Inc. Common Stock
TAT Technologies Ltd. Ordinary Shares
Taylor Devices Inc. Common Stock
Thoma Bravo Advantage Class A Ordinary Shares
AT&T Inc. 5.350% Global Notes due 2066
The Bancorp Inc Common Stock
AT&T Inc. 5.625% Global Notes due 2067
Thunder Bridge Capital Partners III Inc. Units
TrueBlue Inc. Common Stock
Translate Bio Inc. Common Stock
Innovator 20  Year Treasury Bond 9 Buffer ETF - July
Triumph Bancorp Inc. Common Stock
Triumph Bancorp Inc. Depositary Shares Each Representing a 1/40th Interest in a Share of 7.125% Series C Fixed-Rate Non-Cumulative Perpetual Preferred Stock
ToughBuilt Industries Inc. Common Stock
ToughBuilt Industries Inc. Warrant
Territorial Bancorp Inc. Common Stock
Theravance Biopharma Inc. Ordinary Shares
TuanChe Limited American Depositary Shares
Tuatara Capital Acquisition Corporation Unit
Texas Capital Bancshares Inc. Common Stock
Texas Capital Bancshares Inc. 6.50% Subordinated Notes due 2042
Texas Capital Bancshares Inc. Non Cumulative Preferred Perpetual Stock Series A
TriCo Bancshares Common Stock
Tricida Inc. Common Stock
TCF Financial Corporation Common Stock
The Community Financial Corporation Common Stock
TCF Financial Corporation Depositary Shares representing 5.70% Series C Non-Cumulative Preferred Stock
Transcontinental Realty Investors Inc. Common Stock
Tactile Systems Technology Inc. Common Stock
Trip.com Group Limited American Depositary Shares
TRACON Pharmaceuticals Inc. Common Stock
TC PipeLines LP Common Units representing Limited Partner Interests
BlackRock TCP Capital Corp. Common Stock
TCR2 Therapeutics Inc. Common Stock
Container Store (The) Common Stock
Tucows Inc. Class A Common Stock
Toronto Dominion Bank (The) Common Stock
Telephone and Data Systems Inc. 5.875% Senior Notes due 2061
Trident Acquisitions Corp. Common Stock
Trident Acquisitions Corp. Units
Trident Acquisitions Corp. Warrants
Teradata Corporation Common Stock
Telephone and Data Systems Inc. 6.875% Senior Notes due 2059
Templeton Dragon Fund Inc. Common Stock
Transdigm Group Incorporated Transdigm Group Inc. Common Stock
Telephone and Data Systems Inc. Sr Nt
Telephone and Data Systems Inc. 7% Senior Notes due 2060
Teladoc Health Inc. Common Stock
Telephone and Data Systems Inc. Common Shares
Tidewater Inc. Common Stock
Teledyne Technologies Incorporated Common Stock
Tortoise Essential Assets Income Term Fund Common Shares of Beneficial Interest
Atlassian Corporation Plc Class A Ordinary Shares
Bio-Techne Corp Common Stock
Teck Resources Ltd Ordinary Shares
Tectonic Financial Inc. 9.00% Fixed-to-Floating Rate Series B Non-Cumulative Perpetual Preferred Stock
Tarena International Inc. American Depositary Shares
Telefonica SA Common Stock
Trend Aggregation ESG ETF
Templeton Emerging Markets Income Fund Inc. Common Stock
Tekkorp Digital Acquisition Corp. Class A Ordinary Shares
Tekkorp Digital Acquisition Corp. Unit
Tekkorp Digital Acquisition Corp. Warrant
TE Connectivity Ltd. New Switzerland Registered Shares
TELA Bio Inc. Common Stock
Tellurian Inc. Common Stock
Tenneco Inc. Class A Voting Common Stock
Tenable Holdings Inc. Common Stock
Tenax Therapeutics Inc. Common Stock
Telecom Argentina SA
Teradyne Inc. Common Stock
Terns Pharmaceuticals Inc. Common Stock
TESSCO Technologies Incorporated Common Stock
Teva Pharmaceutical Industries Limited American Depositary Shares
Terex Corporation Common Stock
Truist Financial Corporation Common Stock
Truist Financial Corporation Depositary Shares Representing 1/1000th Interest Series F Perpetual Preferred
Truist Financial Corporation Depositary Shares Series G
Truist Financial Corporation Series H 
Truist Financial Corporation Depositary Shares
Truist Financial Corporation Depositary Shares Each Representing a 1/1000th Interest in a Share of Series O Non-Cumulative Perpetual Preferred Stock
Truist Financial Corporation Depositary Shares each representing 1/1000th interest in a share of Series R Non-Cumulative Perpetual Preferred Stock
TFF Pharmaceuticals Inc. Common Stock
TFI International Inc. Common Shares
Innovator 20  Year Treasury Bond 5 Floor ETF - July
Terra Income Fund VI 7.00% Notes due 2026
TFS Financial Corporation Common Stock
Teleflex Incorporated Common Stock
Tredegar Corporation Common Stock
TransGlobe Energy Corporation Ordinary Shares (Canada)
Taseko Mines Ltd. Common Stock
Tengasco Inc. Common Stock
Textainer Group Holdings Limited Common Shares
Triumph Group Inc. Common Stock
Tecnoglass Inc. Ordinary Shares
TEGNA Inc
Teekay LNG Partners L.P.
Teekay LNG Partners L.P. 9.00% Series A Cumulative Redeemable Perpetual Preferred Units representing limited partner interests
Teekay LNG Partners L.P. 8.50% Series B Fixed-to-Floating Rate Cumulative Redeemable Perpetual Preferred Units representing limited partner interests
Transportadora de Gas del Sur SA TGS Common Stock
Target Corporation Common Stock
TG Therapeutics Inc. Common Stock
Target Hospitality Corp. Common Stock
Thunder Bridge Acquisition II Ltd. Class A Ordinary Shares
Thunder Bridge Acquisition II Ltd. Units
Thunder Bridge Acquisition II Ltd. Warrants
Tenet Healthcare Corporation Common Stock
Tuscan Holdings Corp. II Common Stock
Tuscan Holdings Corp. II Unit
Tuscan Holdings Corp. II Warrant
Tuscan Holdings Corp. Common Stock
Tuscan Holdings Corp. Unit
Tuscan Holdings Corp. Warrant
First Financial Corporation Indiana Common Stock
Hanover Insurance Group Inc
International Tower Hill Mines Ltd. Ordinary Shares (Canada)
Thimble Point Acquisition Corp. Unit
ThermoGenesis Holdings Inc. Common Stock
Thor Industries Inc. Common Stock
Tekla Healthcare Opportunies Fund Shares of Beneficial Interest
Thermon Group Holdings Inc. Common Stock
Gentherm Inc Common Stock
Thryv Holdings Inc. Common Stock
Treehouse Foods Inc. Common Stock
Theratechnologies Inc. Common Shares
Tekla World Healthcare Fund Shares of Beneficial Interest
Target Hospitality Corp. Warrant expiring 3/15/2024
Agility Shares Dynamic Tactical Income ETF
Trean Insurance Group Inc. Common Stock
Millicom International Cellular S.A. Common Stock
UP Fintech Holding Ltd American Depositary Share representing fifteen Class A Ordinary Shares
Interface Inc. Common Stock
TIM S.A. American Depositary Shares (Each representing 5 Common Shares) 
Tiga Acquisition Corp. Class A Ordinary Shares
Tiptree Inc. Common Stock
TIAN RUIXIANG Holdings Ltd Class A Ordinary Shares
Team Inc. Common Stock
Titan Machinery Inc. Common Stock
TELUS International (Cda) Inc. Subordinate Voting Shares
TJX Companies Inc. (The) Common Stock
Teekay Corporation Common Stock
Takung Art Co. Ltd. Common Stock
Turkcell Iletisim Hizmetleri AS Common Stock
Timken Company (The) Common Stock
Taiwan Liposome Company Ltd. American Depository Shares
Teligent Inc. Common Stock
Talis Biomedical Corporation Common Stock
PT Telekomunikasi Indonesia Tbk
SOC Telemed Inc. Class A Common Stock
SOC Telemed Inc. Warrants
Talend S.A. American Depositary Shares
Tilray Inc. Class 2 Common Stock 
Telos Corporation Common Stock
Tiziana Life Sciences plc American Depository Share
Tilly's Inc. Common Stock
Toyota Motor Corporation Common Stock
Main Thematic Innovation ETF
Timber Pharmaceuticals Inc. Common Stock
Titan Medical Inc. Ordinary Shares
TransMedics Group Inc. Common Stock
Tencent Music Entertainment Group American Depositary Shares each representing two Class A Ordinary Shares
Taylor Morrison Home Corporation Common Stock
Tastemaker Acquisition Corp. Unit
Thermo Fisher Scientific Inc Common Stock
Tompkins Financial Corporation Common Stock
Turmeric Acquisition Corp. Class A Ordinary Shares
Turmeric Acquisition Corp. Unit
Turmeric Acquisition Corp. Warrant
Trilogy Metals Inc. Common Stock
TimkenSteel Corporation Common Shares
Spartacus Acquisition Corporation Class A Common Stock
Spartacus Acquisition Corporation Unit
Spartacus Acquisition Corporation Warrant
T-Mobile US Inc. Common Stock
Terminix Global Holdings Inc. Common Stock
Tennant Company Common Stock
Tandem Diabetes Care Inc. Common Stock
TriNet Group Inc. Common Stock
Teekay Tankers Ltd.
Travel   Leisure Co. Common  Stock
Tsakos Energy Navigation Ltd Common Shares
Tsakos Energy Navigation Ltd 8.75% Series D Cumulative Redeemable Perpetual Preferred Shares
Tsakos Energy Navigation Ltd Series E Fixed-to-Floating Rate Cumulative Redeemable Perpetual Preferred Shares par value $1.00
Tsakos Energy Navigation Ltd Series F Fixed-to-Floating Rate Cumulative Redeemable Perpetual Preferred Shares par value $1.00
Tonix Pharmaceuticals Holding Corp. Common Stock
Toll Brothers Inc. Common Stock
TOMI Environmental Solutions Inc. Common Stock
TOP Ships Inc. Common Stock
Total SE
Tuniu Corporation American Depositary Shares
TowneBank Common Stock
Turning Point Brands Inc. Common Stock
Tutor Perini Corporation Common Stock
Tribune Publishing Company Common Stock
TPG Pace Beneficial Finance Corp. Class A Ordinary Shares
Tri Pointe Homes Inc. Common Stock
Trinity Place Holdings Inc. Common Stock
TPI Composites Inc. Common Stock
Texas Pacific Land Corporation Common Stock
Tapestry Inc. Common Stock
Third Point Reinsurance Ltd. Common Shares
Turning Point Therapeutics Inc. Common Stock
TriplePoint Venture Growth BDC Corp. Common Stock
TriplePoint Venture Growth BDC Corp. 5.75% Notes due 2022
Tempur Sealy International Inc. Common Stock
Tortoise Power and Energy Infrastructure Fund Inc Common Stock
Tootsie Roll Industries Inc. Common Stock
Tejon Ranch Co Common Stock
Torchlight Energy Resources Inc. Common Stock
Trebia Acquisition Corp. Class A Ordinary Shares
Trecora Resources Common Stock
LendingTree Inc. Common Stock
Trex Company Inc. Common Stock
Targa Resources Inc. Common Stock
Tabula Rasa HealthCare Inc. Common Stock
Thomson Reuters Corp Ordinary Shares
Trinity Biotech plc American Depositary Shares
Trillium Therapeutics Inc. Common Shares
Trinity Capital Inc. Common Stock
TripAdvisor Inc. Common Stock
Triterras Inc. Class A Ordinary Shares
Triterras Inc. Warrant
Trimble Inc. Common Stock
TORM plc Class A Common Stock
Trustmark Corporation Common Stock
Tremont Mortgage Trust Common Shares of Beneficial Interest
Trinity Industries Inc. Common Stock
Terreno Realty Corporation Common Stock
Transcat Inc. Common Stock
T. Rowe Price Group Inc. Common Stock
Tronox Holdings plc Ordinary Shares (UK)
TC Energy Corporation Common Stock
Turquoise Hill Resources Ltd. Ordinary Shares
TriMas Corporation Common Stock
TrustCo Bank Corp NY Common Stock
Trio-Tech International Common Stock
Triton International Limited Common Shares
Triton International Limited 8.50% Series A Cumulative Redeemable Perpetual  Preference Shares
Triton International Limited 8.00% Series B Cumulative Redeemable Perpetual Preference Shares
Triton International Limited 7.375% Series C Cumulative Redeemable Perpetual Preference Shares
Triton International Limited 6.875% Series D Cumulative Redeemable Perpetual Preference Shares
TPG RE Finance Trust Inc. Common Stock
TransUnion Common Stock
TrueCar Inc. Common Stock
Trupanion Inc. Common Stock
The Travelers Companies Inc. Common Stock
trivago N.V. American Depositary Shares
Trevi Therapeutics Inc. Common Stock
Trevena Inc. Common Stock
Tanzanian Gold Corporation Common Stock
TransEnterix Inc. Common Stock
Tenaris S.A. American Depositary Shares
Timberland Bancorp Inc. Common Stock
TriState Capital Holdings Inc. Common Stock
TriState Capital Holdings Inc. Dep Shs Rep 1/40th Int 6.75% Srs A Non-Cum Pfd Stock
TriState Capital Holdings Inc. Depositary Share representing a 1/40th Interest in a Share of 6.375% Fixed-to-Floating Rate Series B Non-Cumulative Perpetual Preferred Stock
Tractor Supply Company Common Stock
Trinseo S.A. Ordinary Shares
Tower Semiconductor Ltd. Ordinary Shares
Taysha Gene Therapies Inc. Common Stock
TCW Strategic Income Fund Inc. Common Stock
TS Innovation Acquisitions Corp. Class A Common Stock
TS Innovation Acquisitions Corp. Unit
TS Innovation Acquisitions Corp. Warrant
Tishman Speyer Innovation Corp. II Unit
Tesla Inc. Common Stock
Sixth Street Specialty Lending Inc. Common Stock
Taiwan Semiconductor Manufacturing Company Ltd.
Tyson Foods Inc. Common Stock
Innovator Triple Stacker ETF - October
Townsquare Media Inc. Class A Common Stock
TSR Inc. Common Stock
Trane Technologies plc
Toro Company (The) Common Stock
Tattooed Chef Inc Class A Common Stock
The Trade Desk Inc. Class A Common Stock
TTEC Holdings Inc. Common Stock
Tetra Tech Inc. Common Stock
TechTarget Inc. Common Stock
Tetra Technologies Inc. Common Stock
Tata Motors Ltd Tata Motors Limited
TTM Technologies Inc. Common Stock
Titan Pharmaceuticals Inc. Common Stock
T2 Biosystems Inc. Common Stock
Tortoise Pipeline & Energy Fund Inc. Common Stock
Take-Two Interactive Software Inc. Common Stock
Telus Corporation Ordinary Shares
Tufin Software Technologies Ltd. Ordinary Shares
Tupperware Brands Corporation Common Stock
180 Degree Capital Corp. Common Stock
Mammoth Energy Services Inc. Common Stock
Grupo Televisa S.A. Common Stock
Thayer Ventures Acquisition Corporation Class A Common Stock
Thayer Ventures Acquisition Corporation Units
Thayer Ventures Acquisition Corporation Warrant
Tennessee Valley Authority Common Stock
Tennessee Valley Authority
Travere Therapeutics Inc. Common Stock
Tivity Health Inc. Common Stock
Tradeweb Markets Inc. Class A Common Stock
TWC Tech Holdings II Corp. Class A Common Stock
TWC Tech Holdings II Corp. Unit
TWC Tech Holdings II Corp. Warrant
Titan International Inc. (DE) Common Stock
Twin Disc Incorporated Common Stock
Twilio Inc. Class A Common Stock
Taiwan Fund Inc. (The) Common Stock
Tailwind Acquisition Corp. Class A Common Stock
Hostess Brands Inc. Class A Common Stock
Hostess Brands Inc. Warrants
Two Harbors Investment Corp
Two Harbors Investments Corp 8.125% Series A Fixed-to-Floating Rate Cumulative Redeemable Preferred Stock ($25.00 liquidation preference per share)
Two Harbors Investments Corp 7.625% Series B Fixed-to-Floating Rate Cumulative Redeemable Preferred Stock
Two Harbors Investments Corp 7.25% Series C Fixed-to-Floating Rate Cumulative Redeemable Preferred Stock
Two Harbors Investments Corp 7.75% Series D Cumulative Redeemable Preferred Stock
Two Harbors Investments Corp 7.50% Series E Cumulative Redeemable Preferred Stock
2U Inc. Common Stock
Twist Bioscience Corporation Common Stock
Twitter Inc. Common Stock
Ternium S.A. Ternium S.A. American Depositary Shares (each representing ten shares USD1.00 par value)
10x Genomics Inc. Class A Common Stock
TherapeuticsMD Inc. Common Stock
Texas Instruments Incorporated Common Stock
Texas Roadhouse Inc. Common Stock
Textron Inc. Common Stock
Tri Continental Corporation Common Stock
Tri Continental Corporation Preferred Stock
Tortoise Energy Infrastructure Corporation Common Stock
Shineco Inc. Common Stock
Tyler Technologies Inc. Common Stock
Tyme Technologies Inc. Common Stock
Travelzoo Common Stock
TZP Strategies Acquisition Corp. Unit
Unity Software Inc. Common Stock
Under Armour Inc. Class C Common Stock
Under Armour Inc. Class A Common Stock
United Airlines Holdings Inc. Common Stock
United States Antimony Corporation Common Stock
CVR Partners LP Common Units representing Limited Partner Interests
AgEagle Aerial Systems Inc. Common Stock
Urstadt Biddle Properties Inc. Common Stock
United Bancorp Inc. Common Stock
Uber Technologies Inc. Common Stock
United Security Bancshares Common Stock
United Bancshares Inc. Common Stock
Urstadt Biddle Properties Inc. Common Stock
Urstadt Biddle Properties Inc. 6.250% Series H Cumulative Redeemable Preferred Stock
Urstadt Biddle Properties Inc. 5.875% Series K Cumulative Redeemable Preferred Stock
UBS Group AG Registered Ordinary Shares
United Bankshares Inc. Common Stock
Unity Biotechnology Inc. Common Stock
United Community Banks Inc. Common Stock
United Community Banks Inc. Depositary Shares each representing 1/1000th interest in a share of Series I Non-CumulativePreferred Stock
uCloudlink Group Inc. American Depositary Shares
Ultra Clean Holdings Inc. Common Stock
UDR Inc. Common Stock
Urban Edge Properties Common Shares of Beneficial Interest
Uranium Energy Corp. Common Stock
Universal Electronics Inc. Common Stock
Net 1 UEPS Technologies Inc. Common Stock
Unique Fabricating Inc. Common Stock
United Fire Group Inc. Common Stock
Unifi Inc. New Common Stock
UFP Industries Inc. Common Stock
UFP Technologies Inc. Common Stock
Domtar Corporation (NEW) Common Stock
United-Guardian Inc. Common Stock
UGI Corporation Common Stock
Ultrapar Participacoes S.A. (New) American Depositary Shares (Each representing one Common Share)
urban-gro Inc. Common Stock
Amerco Common Stock
Universal Health Services Inc. Common Stock
Universal Health Realty Income Trust Common Stock
Ubiquiti Inc. Common Stock
United Insurance Holdings Corp. Common Stock
Unisys Corporation New Common Stock
Ucommune International Ltd Ordinary Shares
Ucommune International Ltd Warrant expiring 11/17/2025
Unilever PLC Common Stock
Ultralife Corporation Common Stock
Universal Logistics Holdings Inc. Common Stock
Ulta Beauty Inc. Common Stock
UMB Financial Corporation Common Stock
United Microelectronics Corporation (NEW) Common Stock
UMH Properties Inc. Common Stock
UMH Properties Inc. 6.75% Series C Cumulative Redeemable Preferred Stock  Liquidation Preference $25 per share
UMH Properties Inc. 6.375% Series D Cumulative Redeemable Preferred Stock Liquidation Preference $25 per share
Umpqua Holdings Corporation Common Stock
Unico American Corporation Common Stock
Union Bankshares Inc. Common Stock
Unifirst Corporation Common Stock
United Natural Foods Inc. Common Stock
UnitedHealth Group Incorporated Common Stock (DE)
Uniti Group Inc. Common Stock
Unum Group Common Stock
Unum Group 6.250% Junior Subordinated Notes due 2058
Union Pacific Corporation Common Stock
Unity Bancorp Inc. Common Stock
Univar Solutions Inc. Common Stock
Urban One Inc. Class A Common Stock
Urban One Inc. Class D Common Stock
Upland Software Inc. Common Stock
United Parcel Service Inc. Common Stock
Upstart Holdings Inc. Common stock
Upwork Inc. Common Stock
Urban Outfitters Inc. Common Stock
Ur Energy Inc Common Shares (Canada)
UroGen Pharma Ltd. Ordinary Shares
United Rentals Inc. Common Stock
Urovant Sciences Ltd. Common Stock
Liberty All-Star Equity Fund Common Stock
USA Compression Partners LP Common Units Representing Limited Partner Interests
USA Truck Inc. Common Stock
Universal Stainless & Alloy Products Inc. Common Stock
Americas Gold and Silver Corporation Common Shares no par value
USA Technologies Inc. Common Stock
U.S. Gold Corp. Common Stock
U.S. Bancorp Common Stock
U.S. Bancorp Depositary Shares Each representing a 1/100th interest in a share of Series A Non-CumulativePerpetual Pfd Stock
U.S. Bancorp Depositary Shares repstg 1/1000th Pfd Ser B
U.S. Bancorp Depositary Shares Representing 1/1000th Interest in a Shares Series F
U.S. Bancorp Depositary Shares each representing a 1/1000th interest in a share of Series K Non-Cumulative Perpetual Preferred Stock
U.S. Bancorp Depositary Shares Each Representing a 1/1000th Interest in a Share of Series L Non-Cumulative Perpetual Preferred Stock
U.S. Bancorp Depositary Shares Each Representing a 1/1000th Interest in a Share of Series M Non-Cumulative Perpetual Preferred Stock
U.S. Concrete Inc. Common Stock
USD Partners LP Common Units representing limited partner interest
U.S. Energy Corp. Common Stock
US Foods Holding Corp. Common Stock
Usio Inc. Common Stock
United States Lime & Minerals Inc. Common Stock
United States Cellular Corporation Common Stock
USANA Health Sciences Inc. Common Stock
U.S. Physical Therapy Inc. Common Stock
U.S. Well Services Inc. Class A Common Stock
U.S. Well Services Inc. Warrants
U.S. Xpress Enterprises Inc. Class A Common Stock
Cohen & Steers Infrastructure Fund Inc Common Stock
Reaves Utility Income Fund Common Shares of Beneficial Interest
United Therapeutics Corporation Common Stock
Universal Technical Institute Inc Common Stock
UNITIL Corporation Common Stock
Utah Medical Products Inc. Common Stock
UTStarcom Holdings Corp.
Utz Brands Inc Class A Common Stock 
Universal Security Instruments Inc. Common Stock
Energy Fuels Inc Ordinary Shares (Canada)
UNIVERSAL INSURANCE HOLDINGS INC Common Stock
Univest Financial Corporation Common Stock
Universal Corporation Common Stock
UWM Holdings Corporation Class A Common Stock
Uxin Limited ADS
United States Cellular Corporation 6.95% Senior Notes due 2060
United States Cellular Corporation 7.25% Senior Notes due 2063
United States Cellular Corporation 7.25% Senior Notes due 2064
United States Cellular Corporation 6.250% Senior Notes due 2069
United States Cellular Corporation 5.500% Senior Notes due 2070
Visa Inc.
Marriott Vacations Worldwide Corporation Common Stock
Vector Acquisition Corporation Class A Common Stock
Vector Acquisition Corporation Unit
Vector Acquisition Corporation Warrant
VALE S.A.  American Depositary Shares Each Representing one common share
Value Line Inc. Common Stock
Vapotherm Inc. Common Stock
Varian Medical Systems Inc. Common Stock
Invesco Bond Fund Common Stock
Village Bank and Trust Financial Corp. Common Stock
VBI Vaccines Inc. New Common Stock (Canada)
Vascular Biogenics Ltd. Ordinary Shares
Veritex Holdings Inc. Common Stock
Visteon Corporation Common Stock
Vericel Corporation Common Stock
Delaware Investments Colorado Municipal Income Fund Inc  Common Stock
Vertical Capital Income Fund Common Shares of Beneficial Interest
Vickers Vantage Corp. I Unit
Vaccinex Inc. Common Stock
Vocera Communications Inc. Common Stock
Victory Capital Holdings Inc. Class A Common Stock
Invesco California Value Municipal Income Trust Common Stock
10X Capital Venture Acquisition Corp Class A Common Stock
10X Capital Venture Acquisition Corp Unit
10X Capital Venture Acquisition Corp Warrant
Veracyte Inc. Common Stock
Vectrus Inc. Common Stock
Veeco Instruments Inc. Common Stock
Vedanta Limited  American Depositary Shares (Each representing four equity shares)
Veeva Systems Inc. Class A Common Stock
Velocity Financial Inc. Common Stock
Venus Acquisition Corporation Units
VEON Ltd. ADS
VEREIT Inc. Common Stock
VEREIT Inc. 6.70% Series F Cumulative Redeemable Preferred Stock
Verb Technology Company Inc. Common Stock
Verb Technology Company Inc. Warrant
Veritone Inc. Common Stock
Venus Concept Inc. Common Stock
Veru Inc. Common Stock
Vertex Inc. Class A Common Stock
Vericity Inc. Common Stock
Vermilion Energy Inc. Common (Canada)
V.F. Corporation Common Stock
Village Farms International Inc. Common Shares
Delaware Investments National Municipal Income Fund Common Stock
Vonage Holdings Corp. Common Stock
VG Acquisition Corp. Class A Ordinary Shares
Virtus Global Multi-Sector Income Fund Common Shares of Beneficial Interest
Invesco Trust for Investment Grade Municipals Common Stock (DE)
Vector Group Ltd. Common Stock
Vista Gold Corp Common Stock
Viveon Health Acquisition Corp. Common Stock
VirnetX Holding Corp Common Stock
Valhi Inc. Common Stock
ViacomCBS Inc. Class B Common Stock
ViacomCBS Inc. Class A Common Stock
VIA optronics AG American Depositary Shares each representing one-fifth of an Ordinary Share
Viavi Solutions Inc. Common Stock
VICI Properties Inc. Common Stock
Vicor Corporation Common Stock
Viela Bio Inc. Common Stock
VPC Impact Acquisition Holdings Class A Ordinary Shares
VPC Impact Acquisition Holdings Unit
VPC Impact Acquisition Holdings Warrant
7GC & Co. Holdings Inc. Class A common stock
7GC & Co. Holdings Inc. Unit
7GC & Co. Holdings Inc. Warrant
Vincerx Pharma Inc. Common Stock
Vincerx Pharma Inc. Unit 
Vincerx Pharma Inc. Warrant
Gaucho Group Holdings Inc. Common Stock
Vinci Partners Investments Ltd. Class A Common Shares
Viomi Technology Co. Ltd American Depositary Shares
Vipshop Holdings Limited American Depositary Shares each representing two ordinary shares
Vir Biotechnology Inc. Common Stock
Virco Manufacturing Corporation Common Stock
Virios Therapeutics Inc. Common Stock
Pacer BioThreat Strategy ETF
Virtu Financial Inc. Class A Common Stock
Vislink Technologies Inc. Common Stock
Vista Oil & Gas S.A.B. de C.V. American Depositary Shares each representing one series A share with no par value
Vital Farms Inc. Common Stock
Telefonica Brasil S.A. American Depositary Shares (Each representing One Common Share)
Viveve Medical Inc. Common Stock
Meridian Bioscience Inc. Common Stock
voxeljet AG American Depositary Shares
Invesco Advantage Municipal Income Trust II Common Shares of Beneficial Interest (DE)
Invesco Municipal Trust Common Stock
Viking Therapeutics Inc. Common Stock
Viking Therapeutics Inc. Warrants
Velodyne Lidar Inc. Common Stock
Velodyne Lidar Inc. Warrants 
Village Super Market Inc. Class A Common Stock
Valero Energy Corporation Common Stock
Vallon Pharmaceuticals Inc. Common Stock
Controladora Vuela Compania de Aviacion S.A.B. de C.V. American Depositary Shares each representing ten (10) Ordinary Participation Certificates
Invesco High Income Trust II
Valley National Bancorp Common Stock
Valley National Bancorp 5.50% Fixed-to-Floating Rate Non-Cumulative Perpetual Preferred Stock Series B
Valley National Bancorp 6.25% Fixed-to-Floating Rate Non-Cumulative Perpetual Preferred Stock Series A
Vistas Media Acquisition Company Inc. Class A Common Stock
Vistas Media Acquisition Company Inc. Unit
Vistas Media Acquisition Company Inc. Warrant
Vision Marine Technologies Inc. Common Shares
Vulcan Materials Company (Holding Company) Common Stock
Viemed Healthcare Inc. Common Shares
Valmont Industries Inc. Common Stock
Delaware Investments Minnesota Municipal Income Fund II Inc. Common Stock
Invesco Municipal Opportunity Trust Common Stock
Vmware Inc. Common stock Class A
Vince Holding Corp. Common Stock
Vanda Pharmaceuticals Inc. Common Stock
Veoneer Inc. Common Stock 
21Vianet Group Inc. American Depositary Shares
Vornado Realty Trust Common Stock
Vornado Realty Trust Pfd S K
Vornado Realty Trust Pfd Ser L %
Vornado Realty Trust 5.25% Series M Cumulative Redeemable Preferred Shares of Beneficial Interest liquidation preference $25.00 per share no par value per share
Vornado Realty Trust 5.25% Series N Cumulative Redeemable Preferred Shares of Beneficial Interest liquidation preference $25.00 per share
Viper Energy Partners LP Common Unit
VolitionRX Limited Common Stock
Vontier Corporation Common Stock 
Venator Materials PLC Ordinary Shares
VOC Energy Trust Units of Beneficial Interest
Vodafone Group Plc American Depositary Shares
Volt Information Sciences Inc. Common Stock
Vor Biopharma Inc. Common Stock
Virtuoso Acquisition Corp. Unit
VOXX International Corporation Class A Common Stock
Voya Financial Inc. Common Stock
Voya Financial Inc. Depositary Shares each representing a 1/40th interest in a share of 5.35% Fixed-Rate Reset Non-Cumulative Preferred Stock Series B
Vishay Precision Group Inc. Common Stock
Invesco Pennsylvania Value Municipal Income Trust Common Stock (DE)
Vera Bradley Inc. Common Stock
ViewRay Inc. Common Stock
Verrica Pharmaceuticals Inc. Common Stock
Viridian Therapeutics Inc. Common Stock
Varex Imaging Corporation Common Stock
Vroom Inc. Common Stock
VerifyMe Inc. Common Stock
VerifyMe Inc. Warrant
Verona Pharma plc American Depositary Share
Varonis Systems Inc. Common Stock
Verint Systems Inc. Common Stock
Virpax Pharmaceuticals Inc. Common Stock
Verra Mobility Corporation Class A Common Stock
Verso Corporation Common Stock
Verisk Analytics Inc. Common Stock
VeriSign Inc. Common Stock
Vertiv Holdings LLC Class A Common Stock
Virtus Investment Partners Inc. Common Stock
Veritiv Corporation Common Stock
Vertex Pharmaceuticals Incorporated Common Stock
Versus Systems Inc. Common Shares
ViaSat Inc. Common Stock
VSE Corporation Common Stock
Vishay Intertechnology Inc. Common Stock
Vesper Healthcare Acquisition Corp. Class A Common Stock
Vesper Healthcare Acquisition Corp. Unit
Vesper Healthcare Acquisition Corp. Warrant
Versus Systems Inc. Class A Warrants
Vistra Corp. Common Stock
Vasta Platform Limited Class A Ordinary Shares
Verastem Inc. Common Stock
Vista Outdoor Inc. Common Stock
Invesco Credit Opportunities Fund Common Shares of Beneficial Interest
Ventoux CCM Acquisition Corp. Common Stock
Ventoux CCM Acquisition Corp. Right
Ventoux CCM Acquisition Corp. Unit
Ventoux CCM Acquisition Corp. Warrant
VistaGen Therapeutics Inc. Common Stock
VectoIQ Acquisition Corp. II Unit
Invesco Trust for Investment Grade New York Municipals Common Stock
Vertex Energy Inc Common Stock
Bristow Group Inc. Common Stock
Ventas Inc. Common Stock
Viatris Inc. Common Stock
Vitru Limited Common Shares
VirTra Inc. Common Stock
vTv Therapeutics Inc. Class A Common Stock
Vuzix Corporation Common Stock
Viad Corp Common Stock
Vivint Smart Home Inc. 
Vivos Therapeutics Inc. Common Stock
VivoPower International PLC Ordinary Shares
Invesco Senior Income Trust Common Stock (DE)
Valvoline Inc. Common Stock
Vaxart Inc Common Stock
Vy Global Growth Class A Ordinary Shares
Voyager Therapeutics Inc. Common Stock
VYNE Therapeutics Inc. Common Stock
Verizon Communications Inc. Common Stock
Wayfair Inc. Class A Common Stock
Westinghouse Air Brake Technologies Corporation Common Stock
Westamerica Bancorporation Common Stock
Washington Federal Inc. Common Stock
Washington Federal Inc. Depositary Shares
Wah Fu Education Group Limited Ordinary Shares
Western Alliance Bancorporation Common Stock (DE)
Western Alliance Bancorporation 6.25% Subordinated Debentures due 2056
Washington Trust Bancorp Inc. Common Stock
Waters Corporation Common Stock
Energous Corporation Common Stock
Weibo Corporation American Depositary Share
Walgreens Boots Alliance Inc. Common Stock
500.com Limited American Depositary Shares each representing 10 Class A shares
Westpac Banking Corporation Common Stock
Webster Financial Corporation Common Stock
Webster Financial Corporation Depositary Shares Each Representing 1/1000th Interest in a Share of 5.25% Series F Non-Cumulative Perpetual Preferred Stock
Welbilt Inc. Common Stock
WESCO International Inc. Common Stock
WESCO International Inc. Depositary Shares each representing 1/1000th interest in a share of Series A Fixed-Rate Reset Cumulative Perpetual Preferred Stock
Waste Connections Inc. Common Shares
Walker & Dunlop Inc Common Stock
Workday Inc. Class A Common Stock
Western Digital Corporation Common Stock
WD-40 Company Common Stock
Waddell & Reed Financial Inc. Common Stock
Western Asset Bond Fund Share of Beneficial Interest
WEC Energy Group Inc. Common Stock
Weidai Ltd. American depositary shares each  representing one (1) Class A ordinary share
Welltower Inc. Common Stock
Wendy's Company (The) Common Stock
Werner Enterprises Inc. Common Stock
Western Midstream Partners LP Common Units Representing Limited Partner Interests
WisdomTree Investments Inc. Common Stock
WEX Inc. common stock
Weyco Group Inc. Common Stock
Woori Financial Group Inc. American Depositary Shares (each representing three (3) shares of Common Stock)
Wells Fargo & Company Common Stock
Wells Fargo & Company Depositary Shares each representing a 1/1000th interest in a share of Non-Cumulative Perpetual Class A Preferred Stock Series AA
Wells Fargo & Company Depositary Shares each representing a 1/1000th interest in a share of Non-Cumulative Perpetual Class A Preferred Stock Series CC
Wells Fargo & Company Wells Fargo & Company 7.50% Non-Cumulative Perpetual Convertible Class A Preferred Stock Series L
Wells Fargo & Company Dep Shs Repstg 1/1000th Perp Pfd Cl A Ser N
Wells Fargo & Company Depositary Shares Representing 1/1000th Perpetual Preferred Class A Series O
Wells Fargo & Company Dep Shs Repstg 1/1000th Int Non Cum Perp Cl A Pfd (Ser P)
Wells Fargo & Company Depositary Shares Representing 1/1000th Interest Perpetual Preferred Class A Series Q Fixed to Floating
Wells Fargo & Company Dep Shs Repstg 1/1000th Int Perp Pfd Cl A (Ser R Fixed To Flltg)
Wells Fargo & Company Depositary Shares each representing a 1/1000th interest in a share of Non-Cumulative Perpetual Class A Preferred Stock Series W
Wells Fargo & Company Depositary Shares each representing a 1/1000th interest in a share of Non-Cumulative Perpetual Class A Preferred Stock Series X
Wells Fargo & Company Depositary Shares each representing a 1/1000th interest in a share of Non-Cumulative Perpetual Class A Preferred Stock Series Y
Wells Fargo & Company Depositary Shares each representing a 1/1000th interest in a share of Non-Cumulative Perpetual Class A Preferred Stock Series Z
West Fraser Timber Co. Ltd Common stock
Winnebago Industries Inc. Common Stock
Wyndham Hotels & Resorts Inc. Common Stock 
Cactus Inc. Class A Common Stock
WhiteHorse Finance Inc. Common Stock
WhiteHorse Finance Inc. 6.50% Notes due 2025
Westwood Holdings Group Inc Common Stock
Wilhelmina International Inc. Common Stock
Wheeler Real Estate Investment Trust Inc. Common Stock
Wheeler Real Estate Investment Trust Inc. Series D Cumulative Preferred Stock
Wheeler Real Estate Investment Trust Inc. Class B Preferred Stock
Whirlpool Corporation Common Stock
Western Asset Inflation-Linked Income Fund
Boingo Wireless Inc. Common Stock
G. Willi-Food International  Ltd. Ordinary Shares
WiMi Hologram Cloud Inc. American Depositary Share
Winmark Corporation Common Stock
Wingstop Inc. Common Stock
Windtree Therapeutics Inc. Common Stock
Encore Wire Corporation Common Stock
Summit Wireless Technologies Inc. Common Stock
ContextLogic Inc. Class A Common Stock
Wipro Limited Common Stock
Western Asset Inflation-Linked Opportunities & Income Fund
Wix.com Ltd. Ordinary Shares
Workiva Inc. Class A Common Stock
WISeKey International Holding AG American Depositary Shares
Workhorse Group Inc. Common Stock
Willdan Group Inc. Common Stock
Willis Lease Finance Corporation Common Stock
Westlake Chemical Corporation Common Stock
Westlake Chemical Partners LP Common Units representing limited partner interests
Whiting Petroleum Corporation Common Stock (New)
Willis Towers Watson Public Limited Company Ordinary Shares
Waste Management Inc. Common Stock
Williams Companies Inc. (The) Common Stock
Western Asset Mortgage Capital Corporation Common Stock
Warner Music Group Corp. Class A Common Stock
Weis Markets Inc. Common Stock
Advanced Drainage Systems Inc. Common Stock
Walmart Inc. Common Stock
Wabash National Corporation Common Stock
Western New England Bancorp Inc. Common Stock
WNS (Holdings) Limited Sponsored ADR (Jersey)
Wunong Net Technology Company Limited Ordinary Shares
Petco Health and Wellness Company Inc. Class A Common Stock
Worthington Industries Inc. Common Stock
Slack Technologies Inc. Class A Common Stock
SCWorx Corp. Common Stock
WideOpenWest Inc. Common Stock
W. P. Carey Inc. REIT
Foley Trasimene Acquisition Corp. Class A CommonStock
Washington Prime Group Inc. Common Stock
Washington Prime Group Inc. 7.5% Series H Cumulative Redeemable Preferred SBI
Washington Prime Group Inc. 6.875% Series I Cumulative Redeemable Preferred SBI
Wheaton Precious Metals Corp Common Shares (Canada)
WPP plc American Depositary Shares
Westport Fuel Systems Inc Common Shares
Wrap Technologies Inc. Common Stock
W.R. Berkley Corporation Common Stock
W.R. Berkley Corporation 5.900% Subordinated Debentures due 2056
W.R. Berkley Corporation 5.75% Subordinated Debentures due 2056
W.R. Berkley Corporation 5.70% Subordinated Debentures due 2058
W.R. Berkley Corporation 5.10% Subordinated Debentures due 2059
W.R. Berkley Corporation 4.25% Subordinated Debentures due 2060
W.R. Berkley Corporation
Washington Real Estate Investment Trust Common Stock
Weingarten Realty Investors Common Stock
Westrock Company Common Stock
World Acceptance Corporation Common Stock
Western Copper and Gold Corporation Common Stock
WesBanco Inc. Common Stock
WesBanco Inc. Depositary Shares Each Representing a 1/40th Interest in a Share of 6.75% Fixed-Rate Reset Non-Cumulative Perpetual Preferred Stock Series A
Waterstone Financial Inc. Common Stock (MD)
WillScot Mobile Mini Holdings Corp. Class A Common Stock
WSFS Financial Corporation Common Stock
Williams-Sonoma Inc. Common Stock (DE)
Watsco Inc. Common Stock
Watsco Inc.
Whitestone REIT Common Shares
West Pharmaceutical Services Inc. Common Stock
Wayside Technology Group Inc. Common Stock
West Bancorporation Common Stock
The Alkaline Water Company Inc. Common Stock
Wintrust Financial Corporation Common Stock
Wintrust Financial Corporation Fixed-to-Floating Rate Non-Cumulative Perpetual Preferred Stock Series D
Wintrust Financial Corporation Depositary Shares Each Representing a 1/1000th Interest in a Share of 6.875% Fixed-Rate Reset Non-Cumulative Perpetual Preferred Stock Series E
W&T Offshore Inc. Common Stock
White Mountains Insurance Group Ltd. Common Stock
Watford Holdings Ltd. Common Shares
Watford Holdings Ltd. 8.5% Cumulative Redeemable Preference Shares
Essential Utilities Inc. Common Stock
Waitr Holdings Inc. Common Stock
Essential Utilities Inc. 6.00% TEU
Watts Water Technologies Inc. Class A Common Stock
Wireless Telecom Group  Inc. Common Stock
Select Energy Services Inc. Class A Common Stock
Western Union Company (The) Common Stock
Esoterica NextG Economy ETF
Wave Life Sciences Ltd. Ordinary Shares
WVS Financial Corp. Common Stock
Willamette Valley Vineyards Inc. Common Stock
Willamette Valley Vineyards Inc. Series A Redeemable Preferred Stock
WW International Inc. Common Stock
Woodward Inc. Common Stock
World Wrestling Entertainment Inc. Class A Common Stock
Westwater Resources Inc. Common Stock
Wolverine World Wide Inc. Common Stock
Weyerhaeuser Company Common Stock
Wynn Resorts Limited Common stock
WidePoint Corporation Common Stock
United States Steel Corporation Common Stock
Beyond Air Inc. Common Stock
Xenetic Biosciences Inc. Common Stock
Xenetic Biosciences Inc. Warrants
XBiotech Inc. Common Stock
Exicure Inc. Common Stock
Franklin Exponential Data ETF
Cimarex Energy Co Common Stock
Xcel Energy Inc. Common Stock
Exela Technologies Inc. Common Stock
Xcel Brands Inc. Common Stock
Xenon Pharmaceuticals Inc. Common Shares
Intersect ENT Inc. Common Stock
Xeris Pharmaceuticals Inc. Common Stock
XAI Octagon Floating Rate & Alternative Income Term Trust Common Shares of Beneficial Interest
X4 Pharmaceuticals Inc. Common Stock
Exagen Inc. Common Stock
Xenia Hotels & Resorts Inc. Common Stock
Xinyuan Real Estate Co Ltd American Depositary Shares
iShares ESG Screened S&P Mid-Cap ETF
iShares ESG Screened S&P Small-Cap ETF
XL Fleet Corp. Class A Common Stock
Xilinx Inc. Common Stock
Acceleron Pharma Inc. Common Stock
Qualtrics International Inc. Class A Common Stock
Xencor Inc. Common Stock
Xunlei Limited American Depositary Receipts
Extraction Oil & Gas Inc. Common Stock
Exxon Mobil Corporation Common Stock
XOMA Corporation Common Stock
XOMA Corporation 8.625% Series A Cumulative Perpetual Preferred Stock
The ExOne Company Common Stock
XP Inc. Class A Common Stock
Power & Digital Infrastructure Acquisition Corp. Unit
XPEL Inc. Common Stock
Xperi Holding Corporation Common Stock
XPeng Inc. American depositary shares each representing two Class A ordinary shares
Solitario Zinc Corp. Common Stock
XPO Logistics Inc.
DPCM Capital Inc. Class A Common Stock
DENTSPLY SIRONA Inc. Common Stock
Xerox Holdings Corporation Common Stock
XpresSpa Group Inc. Common Stock
XTL Biopharmaceuticals Ltd. American Depositary Shares
Xtant Medical Holdings Inc. Common Stock
iShares ESG Screened S&P 500 ETF
22nd Century Group Inc. Common Stock
X Financial American Depositary Shares each representing six Class A Ordinary Shares
Xylem Inc. Common Stock New
Alleghany Corporation Common Stock
Yucaipa Acquisition Corporation Class A Ordinary Shares
Yalla Group Limited American Depositary Shares each representing one Class A Ordinary Share
cbdMD Inc. Common Stock
cbdMD Inc. 8.0% Series A Cumulative Convertible Preferred Stock
FT Cboe Vest International Equity Buffer ETF - December
Yellow Corporation Common Stock
Yelp Inc. Common Stock
YETI Holdings Inc. Common Stock
Yext Inc. Common Stock
MingZhu Logistics Holdings Limited Ordinary Shares
111 Inc. American Depositary Shares
Yunji Inc. American Depository Shares
Y-mAbs Therapeutics Inc. Common Stock
Yumanity Therapeutics Inc. Common Stock
Yandex N.V. Class A Ordinary Shares
York Water Company (The) Common Stock
YPF Sociedad Anonima Common Stock
17 Education & Technology Group Inc. American Depositary Shares
Yiren Digital Ltd. American Depositary Shares each representing two ordinary shares
Yellowstone Acquisition Company Class A Common Stock
Yellowstone Acquisition Company Units
Yellowstone Acquisition Company Warrants to purchase Class A common stock
Yatsen Holding Limited American Depositary Shares each representing four Class A ordinary shares
Yield10 Bioscience Inc. Common Stock
Yatra Online Inc. Ordinary Shares
Yum! Brands Inc.
Yum China Holdings Inc. Common Stock
Liquid Media Group Ltd. Common Shares
JOYY Inc. American Depositary Shares
Zillow Group Inc. Class C Capital Stock
ZAGG Inc Common Stock (Delaware)
Zimmer Biomet Holdings Inc. Common Stock
Zebra Technologies Corporation Class A Common Stock
Zhongchao Inc. Class A Ordinary Shares
Zedge Inc. Class B Common Stock 
Zealand Pharma A/S American Depositary Shares
Zendesk Inc. Common Stock
Olympic Steel Inc. Common Stock
Zillow Group Inc. Class A Common Stock
Zogenix Inc. Common Stock
Yunhong International Class A Ordinary Shares
Yunhong International Right
Yunhong International Unit
Yunhong International Warrant
ZoomInfo Technologies Inc. Class A Common Stock
ZIM Integrated Shipping Services Ltd. Ordinary Shares
Zions Bancorporation N.A. Common Stock
Zions Bancorporation 6.95% Fixed-to-Floating Rate Subordinated Notes
Zions Bancorporation N.A. Dep Shs Repstg 1/40th Int Sh Ser H Perp Pfd Stk
Zions Bancorporation N.A. Dep Shs Repstg 1/40th Perp Pfd Ser G
Zions Bancorporation N.A. Depositary Shares (Each representing 1/40th Interest in a Share of Series A Floating-Rate Non-Cumulative Perpetual Preferred Stock)
ZIOPHARM Oncology Inc Common Stock
Zix Corporation Common Stock
ZK International Group Co. Ltd Ordinary Share
Zai Lab Limited American Depositary Shares
Zoom Video Communications Inc. Class A Common Stock
Zynga Inc. Class A Common Stock
China Southern Airlines Company Limited Common Stock
Zanite Acquisition Corp. Class A Common Stock
Zanite Acquisition Corp. Unit
Zanite Acquisition Corp. Warrant
Zentalis Pharmaceuticals Inc. Common Stock
Zomedica Corp. Common Shares
Zscaler Inc. Common Stock
Zosano Pharma Corporation Common Stock
ZTO Express (Cayman) Inc. American Depositary Shares each representing one Class A ordinary share.
Virtus Total Return Fund Inc.
Zoetis Inc. Class A Common Stock
Zumiez Inc. Common Stock
Zuora Inc. Class A Common Stock
Zovio Inc. Common Stock
Z-Work Acquisition Corp. Units
Zymeworks Inc. Common Shares
Zynerba Pharmaceuticals Inc. Common Stock
Zynex Inc. Common Stock"""

indices = [0, 1, 2, 3, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 39, 40, 41, 42, 43, 44, 45, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 60, 63, 64, 65, 66, 67, 68, 69, 70, 71, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87, 88, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 106, 107, 108, 109, 110, 111, 112, 114, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 146, 147, 148, 149, 150, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 169, 170, 171, 174, 175, 176, 177, 178, 179, 180, 183, 185, 189, 190, 191, 192, 193, 194, 195, 196, 201, 202, 207, 211, 212, 213, 214, 215, 216, 217, 218, 221, 222, 223, 225, 229, 235, 237, 240, 241, 242, 243, 244, 245, 246, 248, 249, 250, 251, 252, 256, 259, 262, 263, 264, 265, 267, 268, 269, 270, 271, 274, 275, 276, 277, 278, 279, 281, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 301, 302, 303, 304, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 329, 330, 331, 332, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 364, 367, 368, 369, 370, 371, 372, 373, 374, 375, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 408, 409, 410, 411, 412, 413, 414, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 452, 453, 455, 456, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 469, 470, 471, 472, 475, 476, 477, 478, 481, 482, 483, 484, 485, 486, 489, 490, 491, 492, 494, 495, 496, 497, 498, 499, 500, 502, 504, 507, 508, 509, 510, 512, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 526, 527, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 544, 545, 546, 547, 548, 549, 550, 552, 553, 554, 555, 556, 557, 559, 560, 561, 562, 563, 564, 565, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 583, 584, 585, 586, 587, 588, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 624, 625, 626, 627, 628, 629, 630, 632, 633, 634, 635, 636, 637, 638, 639, 640, 642, 643, 644, 645, 646, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 661, 662, 663, 664, 665, 666, 667, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 680, 681, 682, 683, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 699, 700, 701, 702, 703, 704, 705, 706, 707, 717, 718, 719, 720, 721, 722, 724, 727, 728, 730, 731, 732, 733, 734, 735, 736, 738, 739, 740, 741, 742, 743, 744, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 764, 765, 767, 768, 769, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 789, 790, 793, 794, 795, 796, 797, 798, 799, 800, 801, 803, 804, 805, 806, 809, 810, 812, 813, 817, 820, 821, 822, 824, 825, 826, 828, 830, 831, 832, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 849, 850, 851, 852, 854, 855, 856, 857, 858, 859, 864, 865, 867, 870, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 886, 887, 888, 889, 890, 894, 895, 896, 897, 898, 900, 901, 902, 904, 905, 907, 908, 909, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 923, 924, 925, 927, 928, 929, 930, 932, 933, 934, 935, 936, 937, 938, 942, 943, 944, 947, 952, 953, 954, 955, 956, 957, 958, 960, 961, 963, 964, 965, 966, 967, 968, 970, 971, 972, 974, 975, 977, 978, 979, 980, 981, 982, 983, 984, 987, 988, 989, 990, 991, 992, 993, 996, 997, 998, 999, 1000, 1004, 1006, 1007, 1008, 1009, 1010, 1011, 1014, 1015, 1019, 1020, 1023, 1024, 1025, 1029, 1030, 1031, 1032, 1034, 1035, 1039, 1040, 1041, 1042, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1062, 1063, 1065, 1066, 1067, 1068, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1080, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1110, 1112, 1114, 1115, 1116, 1118, 1119, 1121, 1122, 1123, 1125, 1126, 1127, 1128, 1129, 1130, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192, 1193, 1195, 1196, 1197, 1198, 1199, 1200, 1201, 1202, 1203, 1204, 1206, 1207, 1208, 1209, 1210, 1211, 1212, 1213, 1214, 1215, 1216, 1217, 1218, 1219, 1220, 1221, 1222, 1223, 1224, 1225, 1226, 1227, 1228, 1229, 1230, 1231, 1233, 1234, 1235, 1236, 1237, 1238, 1241, 1242, 1243, 1244, 1245, 1246, 1247, 1248, 1249, 1250, 1252, 1253, 1254, 1255, 1258, 1259, 1260, 1261, 1262, 1263, 1264, 1265, 1266, 1267, 1268, 1269, 1270, 1271, 1272, 1273, 1274, 1275, 1276, 1278, 1279, 1280, 1281, 1283, 1284, 1286, 1287, 1288, 1289, 1290, 1293, 1294, 1295, 1296, 1299, 1300, 1301, 1302, 1303, 1305, 1314, 1315, 1317, 1319, 1321, 1322, 1323, 1324, 1325, 1326, 1327, 1328, 1329, 1330, 1331, 1334, 1335, 1336, 1337, 1338, 1339, 1340, 1341, 1342, 1344, 1345, 1346, 1347, 1348, 1349, 1353, 1354, 1355, 1356, 1359, 1360, 1362, 1363, 1366, 1367, 1368, 1369, 1370, 1375, 1376, 1377, 1379, 1380, 1381, 1382, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1392, 1395, 1396, 1401, 1402, 1403, 1405, 1406, 1408, 1409, 1410, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1436, 1437, 1438, 1439, 1440, 1442, 1447, 1449, 1450, 1451, 1452, 1453, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1486, 1487, 1489, 1490, 1491, 1492, 1493, 1498, 1499, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511, 1512, 1513, 1514, 1515, 1516, 1518, 1519, 1520, 1521, 1523, 1524, 1526, 1527, 1529, 1530, 1531, 1532, 1533, 1534, 1535, 1536, 1537, 1538, 1539, 1540, 1541, 1542, 1543, 1544, 1547, 1548, 1549, 1555, 1556, 1557, 1559, 1560, 1561, 1562, 1563, 1564, 1565, 1566, 1567, 1569, 1570, 1571, 1574, 1575, 1578, 1579, 1580, 1581, 1582, 1584, 1585, 1586, 1587, 1588, 1589, 1592, 1593, 1594, 1595, 1596, 1597, 1598, 1599, 1600, 1601, 1602, 1603, 1604, 1605, 1606, 1607, 1608, 1609, 1610, 1611, 1612, 1613, 1614, 1615, 1616, 1619, 1620, 1621, 1622, 1623, 1624, 1625, 1627, 1628, 1629, 1630, 1631, 1633, 1634, 1635, 1636, 1637, 1638, 1640, 1641, 1642, 1643, 1644, 1645, 1646, 1647, 1648, 1649, 1650, 1654, 1655, 1656, 1657, 1659, 1660, 1661, 1662, 1663, 1664, 1665, 1666, 1667, 1668, 1669, 1670, 1671, 1672, 1673, 1674, 1675, 1676, 1677, 1678, 1679, 1680, 1681, 1683, 1686, 1687, 1688, 1689, 1691, 1692, 1693, 1694, 1695, 1697, 1698, 1701, 1702, 1703, 1706, 1707, 1708, 1709, 1710, 1711, 1712, 1713, 1714, 1715, 1716, 1717, 1718, 1719, 1720, 1721, 1722, 1723, 1724, 1726, 1727, 1728, 1729, 1730, 1736, 1737, 1739, 1740, 1741, 1743, 1744, 1745, 1746, 1747, 1748, 1749, 1750, 1751, 1752, 1753, 1754, 1755, 1756, 1757, 1758, 1759, 1760, 1761, 1762, 1763, 1764, 1765, 1766, 1767, 1768, 1769, 1770, 1771, 1772, 1773, 1774, 1775, 1776, 1777, 1778, 1779, 1780, 1782, 1783, 1784, 1785, 1786, 1787, 1788, 1789, 1790, 1792, 1793, 1794, 1796, 1798, 1799, 1800, 1801, 1802, 1803, 1804, 1805, 1806, 1807, 1808, 1809, 1810, 1811, 1812, 1813, 1814, 1815, 1816, 1819, 1820, 1821, 1822, 1823, 1824, 1825, 1826, 1827, 1828, 1829, 1831, 1834, 1835, 1839, 1840, 1842, 1843, 1845, 1846, 1849, 1850, 1852, 1853, 1854, 1855, 1856, 1857, 1858, 1859, 1860, 1861, 1862, 1863, 1865, 1866, 1867, 1870, 1871, 1872, 1873, 1874, 1875, 1878, 1879, 1880, 1882, 1883, 1884, 1886, 1887, 1890, 1891, 1892, 1893, 1894, 1897, 1898, 1899, 1900, 1901, 1902, 1903, 1904, 1907, 1908, 1910, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922, 1925, 1926, 1931, 1932, 1933, 1934, 1935, 1936, 1938, 1940, 1941, 1942, 1943, 1944, 1945, 1947, 1948, 1949, 1950, 1951, 1953, 1954, 1955, 1957, 1958, 1959, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1975, 1976, 1978, 1979, 1980, 1981, 1983, 1984, 1988, 1993, 1994, 1996, 1997, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2010, 2011, 2012, 2014, 2016, 2020, 2025, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058, 2059, 2060, 2061, 2062, 2064, 2065, 2066, 2067, 2068, 2069, 2070, 2071, 2072, 2073, 2074, 2078, 2080, 2081, 2082, 2084, 2085, 2086, 2087, 2088, 2089, 2090, 2091, 2092, 2093, 2094, 2095, 2096, 2097, 2100, 2101, 2102, 2103, 2104, 2105, 2107, 2108, 2109, 2110, 2112, 2113, 2114, 2116, 2117, 2118, 2119, 2120, 2121, 2122, 2124, 2125, 2126, 2127, 2128, 2129, 2130, 2131, 2132, 2134, 2135, 2136, 2137, 2138, 2140, 2141, 2142, 2143, 2144, 2145, 2146, 2147, 2148, 2149, 2150, 2151, 2152, 2153, 2154, 2155, 2156, 2157, 2158, 2159, 2160, 2161, 2162, 2163, 2164, 2165, 2166, 2168, 2169, 2170, 2171, 2172, 2173, 2174, 2175, 2176, 2177, 2179, 2180, 2181, 2182, 2184, 2185, 2186, 2187, 2188, 2189, 2191, 2192, 2193, 2194, 2195, 2196, 2198, 2199, 2200, 2202, 2205, 2206, 2207, 2208, 2209, 2210, 2211, 2212, 2213, 2214, 2218, 2219, 2220, 2221, 2222, 2223, 2225, 2226, 2229, 2230, 2231, 2233, 2234, 2235, 2236, 2237, 2238, 2241, 2242, 2243, 2244, 2245, 2246, 2247, 2248, 2249, 2250, 2251, 2252, 2253, 2254, 2257, 2258, 2259, 2260, 2261, 2262, 2263, 2264, 2265, 2266, 2270, 2271, 2272, 2273, 2274, 2275, 2278, 2279, 2280, 2281, 2282, 2283, 2284, 2285, 2286, 2287, 2288, 2291, 2292, 2293, 2294, 2297, 2299, 2300, 2301, 2304, 2305, 2307, 2308, 2309, 2310, 2311, 2312, 2314, 2315, 2316, 2317, 2318, 2319, 2320, 2323, 2324, 2325, 2326, 2327, 2328, 2329, 2330, 2331, 2334, 2335, 2336, 2337, 2338, 2339, 2340, 2341, 2342, 2343, 2344, 2345, 2346, 2349, 2350, 2351, 2352, 2353, 2354, 2355, 2356, 2357, 2358, 2359, 2360, 2362, 2363, 2364, 2365, 2368, 2369, 2370, 2371, 2372, 2373, 2374, 2375, 2376, 2377, 2380, 2382, 2383, 2384, 2385, 2386, 2388, 2389, 2390, 2391, 2392, 2393, 2394, 2395, 2396, 2400, 2401, 2402, 2403, 2404, 2405, 2406, 2407, 2408, 2411, 2412, 2415, 2416, 2419, 2420, 2421, 2422, 2423, 2426, 2427, 2428, 2429, 2430, 2432, 2433, 2435, 2436, 2437, 2438, 2439, 2440, 2443, 2446, 2447, 2448, 2450, 2452, 2454, 2455, 2456, 2458, 2459, 2460, 2461, 2462, 2468, 2469, 2470, 2471, 2473, 2476, 2477, 2478, 2479, 2480, 2481, 2482, 2487, 2488, 2489, 2490, 2491, 2495, 2496, 2500, 2501, 2502, 2503, 2504, 2505, 2506, 2508, 2509, 2510, 2511, 2512, 2513, 2514, 2515, 2516, 2517, 2518, 2519, 2520, 2521, 2522, 2523, 2525, 2526, 2529, 2530, 2531, 2532, 2533, 2534, 2535, 2537, 2538, 2540, 2541, 2542, 2543, 2544, 2547, 2548, 2549, 2551, 2553, 2554, 2555, 2556, 2557, 2558, 2559, 2560, 2561, 2562, 2563, 2565, 2566, 2567, 2568, 2570, 2571, 2574, 2575, 2576, 2577, 2579, 2580, 2581, 2588, 2589, 2591, 2592, 2594, 2595, 2596, 2597, 2598, 2599, 2600, 2601, 2602, 2603, 2605, 2606, 2607, 2609, 2611, 2612, 2613, 2614, 2616, 2617, 2618, 2619, 2620, 2621, 2622, 2623, 2627, 2628, 2629, 2630, 2631, 2632, 2633, 2634, 2637, 2638, 2641, 2642, 2644, 2645, 2647, 2651, 2652, 2653, 2656, 2657, 2658, 2660, 2661, 2662, 2663, 2665, 2666, 2667, 2668, 2669, 2670, 2671, 2673, 2674, 2675, 2676, 2677, 2678, 2679, 2682, 2683, 2684, 2685, 2686, 2691, 2692, 2693, 2696, 2697, 2699, 2700, 2701, 2702, 2703, 2704, 2705, 2706, 2707, 2708, 2709, 2710, 2712, 2713, 2714, 2715, 2716, 2717, 2718, 2719, 2720, 2721, 2723, 2724, 2725, 2726, 2727, 2728, 2729, 2732, 2733, 2734, 2735, 2736, 2739, 2741, 2742, 2746, 2748, 2750, 2751, 2752, 2753, 2754, 2755, 2756, 2757, 2758, 2759, 2760, 2761, 2762, 2764, 2767, 2768, 2769, 2770, 2771, 2772, 2774, 2776, 2781, 2782, 2783, 2784, 2785, 2786, 2788, 2789, 2792, 2793, 2794, 2795, 2796, 2797, 2798, 2799, 2800, 2801, 2802, 2803, 2804, 2805, 2806, 2809, 2811, 2812, 2816, 2819, 2820, 2821, 2822, 2823, 2824, 2825, 2826, 2827, 2828, 2829, 2830, 2835, 2837, 2838, 2840, 2841, 2842, 2843, 2847, 2849, 2850, 2851, 2852, 2853, 2855, 2856, 2857, 2858, 2859, 2860, 2862, 2864, 2866, 2867, 2868, 2869, 2871, 2872, 2873, 2876, 2877, 2878, 2880, 2881, 2882, 2883, 2886, 2887, 2889, 2890, 2891, 2892, 2893, 2894, 2895, 2896, 2897, 2899, 2900, 2901, 2902, 2903, 2904, 2905, 2908, 2910, 2911, 2912, 2913, 2915, 2916, 2917, 2918, 2919, 2920, 2921, 2922, 2923, 2924, 2925, 2926, 2928, 2929, 2930, 2931, 2932, 2933, 2934, 2935, 2936, 2937, 2941, 2942, 2943, 2944, 2945, 2946, 2950, 2951, 2955, 2956, 2957, 2958, 2959, 2968, 2969, 2970, 2971, 2972, 2973, 2974, 2975, 2976, 2977, 2978, 2979, 2982, 2983, 2985, 2986, 2987, 2988, 2989, 2990, 2991, 2992, 2993, 2994, 2995, 2996, 2997, 2998, 2999, 3000, 3001, 3002, 3003, 3004, 3005, 3006, 3009, 3010, 3011, 3013, 3014, 3015, 3016, 3017, 3018, 3019, 3022, 3023, 3024, 3025, 3028, 3029, 3030, 3031, 3032, 3033, 3034, 3035, 3036, 3037, 3038, 3039, 3042, 3043, 3044, 3045, 3046, 3047, 3048, 3049, 3050, 3051, 3052, 3054, 3055, 3058, 3059, 3061, 3062, 3063, 3064, 3065, 3066, 3067, 3068, 3070, 3072, 3073, 3074, 3075, 3076, 3080, 3081, 3082, 3084, 3085, 3086, 3087, 3088, 3089, 3090, 3091, 3092, 3093, 3094, 3095, 3097, 3099, 3100, 3102, 3103, 3104, 3105, 3106, 3107, 3108, 3109, 3112, 3113, 3114, 3115, 3116, 3117, 3118, 3119, 3121, 3123, 3124, 3126, 3127, 3128, 3129, 3130, 3131, 3132, 3133, 3134, 3135, 3137, 3138, 3141, 3142, 3143, 3144, 3146, 3147, 3148, 3149, 3150, 3151, 3152, 3153, 3154, 3155, 3156, 3157, 3158, 3159, 3160, 3161, 3162, 3163, 3164, 3167, 3168, 3169, 3170, 3171, 3172, 3173, 3174, 3175, 3177, 3178, 3179, 3181, 3183, 3184, 3185, 3187, 3188, 3189, 3190, 3191, 3193, 3194, 3195, 3196, 3197, 3198, 3199, 3200, 3202, 3203, 3204, 3205, 3206, 3207, 3208, 3210, 3211, 3212, 3213, 3214, 3219, 3220, 3221, 3222, 3225, 3226, 3227, 3229, 3230, 3232, 3234, 3235, 3236, 3237, 3238, 3239, 3240, 3241, 3242, 3243, 3244, 3245, 3246, 3248, 3249, 3250, 3252, 3253, 3254, 3257, 3258, 3260, 3261, 3262, 3263, 3264, 3265, 3266, 3267, 3271, 3272, 3276, 3278, 3279, 3280, 3281, 3282, 3283, 3284, 3285, 3286, 3287, 3288, 3289, 3290, 3291, 3292, 3293, 3294, 3296, 3297, 3298, 3299, 3300, 3301, 3302, 3303, 3304, 3305, 3306, 3307, 3308, 3309, 3310, 3311, 3312, 3313, 3314, 3315, 3316, 3317, 3318, 3319, 3320, 3321, 3322, 3324, 3325, 3326, 3327, 3328, 3329, 3330, 3331, 3332, 3333, 3334, 3335, 3338, 3341, 3343, 3344, 3345, 3346, 3347, 3348, 3349, 3350, 3351, 3352, 3353, 3355, 3357, 3358, 3359, 3362, 3363, 3364, 3365, 3366, 3368, 3370, 3371, 3372, 3373, 3374, 3375, 3377, 3378, 3379, 3380, 3381, 3382, 3383, 3384, 3385, 3386, 3387, 3388, 3389, 3390, 3392, 3393, 3395, 3396, 3397, 3398, 3399, 3402, 3403, 3405, 3406, 3407, 3408, 3409, 3410, 3411, 3412, 3413, 3414, 3415, 3416, 3417, 3418, 3419, 3422, 3423, 3424, 3425, 3426, 3427, 3428, 3429, 3430, 3431, 3432, 3434, 3435, 3436, 3437, 3438, 3439, 3440, 3441, 3442, 3443, 3444, 3445, 3446, 3447, 3448, 3449, 3450, 3451, 3452, 3453, 3454, 3455, 3456, 3457, 3458, 3459, 3460, 3461, 3464, 3465, 3466, 3467, 3468, 3469, 3470, 3471, 3472, 3473, 3474, 3475, 3476, 3477, 3478, 3479, 3481, 3482, 3483, 3484, 3485, 3486, 3487, 3488, 3489, 3490, 3491, 3492, 3493, 3494, 3495, 3498, 3499, 3500, 3501, 3502, 3503, 3504, 3505, 3506, 3507, 3508, 3509, 3510, 3511, 3512, 3513, 3514, 3515, 3516, 3517, 3518, 3519, 3520, 3521, 3522, 3525, 3526, 3527, 3528, 3529, 3530, 3531, 3532, 3533, 3534, 3535, 3537, 3538, 3539, 3540, 3541, 3542, 3543, 3544, 3545, 3546, 3547, 3548, 3549, 3550, 3551, 3552, 3553, 3554, 3555, 3556, 3557, 3558, 3559, 3560, 3561, 3562, 3563, 3564, 3565, 3567, 3568, 3570, 3571, 3572, 3573, 3574, 3575, 3576, 3577, 3578, 3579, 3580, 3583, 3584, 3585, 3586, 3587, 3588, 3589, 3590, 3591, 3592, 3595, 3603, 3604, 3605, 3607, 3608, 3609, 3610, 3611, 3612, 3613, 3614, 3615, 3617, 3618, 3620, 3621, 3622, 3623, 3624, 3625, 3626, 3627, 3628, 3629, 3630, 3631, 3632, 3633, 3634, 3635, 3636, 3638, 3639, 3640, 3641, 3642, 3643, 3644, 3645, 3646, 3648, 3649, 3650, 3651, 3653, 3654, 3658, 3659, 3660, 3661, 3662, 3663, 3664, 3665, 3666, 3668, 3671, 3672, 3673, 3676, 3677, 3678, 3679, 3684, 3685, 3686, 3687, 3688, 3689, 3690, 3691, 3692, 3693, 3694, 3695, 3696, 3697, 3698, 3699, 3700, 3701, 3702, 3703, 3704, 3705, 3706, 3707, 3708, 3709, 3710, 3711, 3712, 3713, 3714, 3715, 3716, 3717, 3718, 3719, 3720, 3721, 3722, 3723, 3724, 3725, 3726, 3727, 3728, 3729, 3730, 3731, 3732, 3733, 3734, 3735, 3736, 3740, 3741, 3742, 3744, 3745, 3746, 3747, 3748, 3749, 3750, 3751, 3752, 3753, 3754, 3755, 3756, 3757, 3758, 3759, 3760, 3761, 3762, 3763, 3764, 3765, 3766, 3769, 3770, 3771, 3772, 3773, 3774, 3775, 3778, 3779, 3780, 3783, 3784, 3785, 3786, 3788, 3789, 3791, 3792, 3795, 3796, 3799, 3800, 3803, 3804, 3805, 3806, 3807, 3808, 3811, 3812, 3813, 3815, 3816, 3817, 3818, 3819, 3820, 3821, 3822, 3823, 3824, 3825, 3826, 3827, 3828, 3829, 3830, 3831, 3832, 3834, 3836, 3837, 3838, 3841, 3842, 3843, 3844, 3846, 3847, 3849, 3850, 3851, 3852, 3853, 3854, 3855, 3856, 3857, 3858, 3860, 3861, 3862, 3863, 3864, 3865, 3866, 3867, 3868, 3869, 3872, 3873, 3874, 3876, 3877, 3878, 3879, 3881, 3882, 3883, 3884, 3885, 3887, 3888, 3889, 3890, 3891, 3892, 3893, 3894, 3895, 3896, 3900, 3901, 3902, 3903, 3904, 3905, 3907, 3908, 3909, 3910, 3911, 3914, 3915, 3916, 3917, 3918, 3919, 3920, 3921, 3922, 3923, 3924, 3925, 3927, 3928, 3929, 3930, 3931, 3932, 3933, 3934, 3935, 3936, 3937, 3938, 3939, 3940, 3941, 3942, 3943, 3944, 3945, 3946, 3947, 3948, 3950, 3951, 3952, 3953, 3957, 3958, 3959, 3960, 3961, 3963, 3964, 3965, 3966, 3967, 3968, 3969, 3970, 3971, 3972, 3976, 3977, 3978, 3979, 3980, 3981, 3982, 3983, 3985, 3986, 3987, 3988, 3989, 3990, 3991, 3992, 3993, 3994, 3995, 3996, 3997, 3998, 4000, 4003, 4004, 4005, 4006, 4009, 4010, 4011, 4012, 4013, 4014, 4015, 4016, 4017, 4018, 4019, 4020, 4021, 4022, 4023, 4024, 4025, 4026, 4027, 4028, 4029, 4030, 4031, 4032, 4033, 4034, 4035, 4038, 4039, 4040, 4041, 4042, 4043, 4044, 4045, 4046, 4047, 4048, 4049, 4050, 4051, 4052, 4053, 4054, 4055, 4056, 4057, 4058, 4059, 4060, 4062, 4063, 4064, 4065, 4066, 4067, 4068, 4069, 4070, 4071, 4072, 4073, 4074, 4076, 4077, 4078, 4079, 4081, 4082, 4083, 4084, 4085, 4087, 4088, 4089, 4090, 4091, 4092, 4093, 4094, 4095, 4096, 4097, 4098, 4099, 4100, 4101, 4102, 4103, 4105, 4106, 4107, 4108, 4112, 4113, 4115, 4118, 4119, 4120, 4121, 4122, 4123, 4125, 4127, 4128, 4129, 4130, 4131, 4132, 4133, 4134, 4135, 4136, 4137, 4138, 4139, 4140, 4141, 4142, 4145, 4146, 4147, 4148, 4149, 4150, 4151, 4155, 4157, 4159, 4162, 4164, 4165, 4166, 4167, 4169, 4170, 4171, 4173, 4174, 4175, 4177, 4178, 4179, 4180, 4181, 4185, 4186, 4187, 4188, 4189, 4190, 4191, 4192, 4193, 4194, 4197, 4198, 4199, 4200, 4201, 4202, 4203, 4204, 4205, 4206, 4207, 4208, 4210, 4211, 4212, 4213, 4214, 4215, 4216, 4217, 4218, 4219, 4220, 4221, 4222, 4224, 4225, 4227, 4228, 4229, 4231, 4232, 4233, 4234, 4235, 4236, 4237, 4238, 4239, 4240, 4241, 4242, 4243, 4244, 4245, 4246, 4247, 4248, 4249, 4250, 4251, 4254, 4255, 4256, 4257, 4258, 4259, 4260, 4261, 4262, 4263, 4264, 4265, 4266, 4267, 4268, 4269, 4271, 4274, 4276, 4277, 4278, 4279, 4280, 4281, 4282, 4283, 4284, 4285, 4286, 4287, 4288, 4289, 4290, 4291, 4292, 4293, 4294, 4295, 4296, 4297, 4298, 4299, 4302, 4303, 4304, 4305, 4306, 4307, 4308, 4309, 4310, 4311, 4312, 4313, 4314, 4315, 4316, 4317, 4318, 4319, 4320, 4321, 4322, 4323, 4324, 4325, 4326, 4329, 4330, 4332, 4333, 4334, 4335, 4336, 4337, 4338, 4339, 4340, 4341, 4342, 4344, 4345, 4346, 4347, 4348, 4349, 4350, 4351, 4352, 4353, 4354, 4356, 4357, 4358, 4359, 4360, 4361, 4362, 4365, 4366, 4368, 4369, 4370, 4372, 4373, 4374, 4375, 4376, 4377, 4379, 4381, 4382, 4383, 4385, 4386, 4387, 4389, 4391, 4392, 4394, 4395, 4396, 4397, 4398, 4399, 4400, 4401, 4402, 4403, 4404, 4405, 4406, 4407, 4408, 4409, 4410, 4411, 4412, 4413, 4414, 4415, 4416, 4417, 4419, 4421, 4422, 4423, 4427, 4428, 4429, 4430, 4431, 4432, 4433, 4434, 4435, 4437, 4438, 4439, 4440, 4441, 4442, 4443, 4444, 4446, 4447, 4448, 4449, 4450, 4451, 4452, 4453, 4458, 4459, 4460, 4461, 4462, 4464, 4465, 4466, 4469, 4475, 4476, 4477, 4478, 4479, 4480, 4482, 4483, 4484, 4485, 4486, 4488, 4489, 4490, 4491, 4492, 4493, 4494, 4495, 4496, 4500, 4501, 4502, 4503, 4504, 4505, 4506, 4507, 4508, 4509, 4510, 4511, 4512, 4515, 4516, 4517, 4520, 4521, 4522, 4523, 4524, 4525, 4527, 4528, 4531, 4536, 4537, 4538, 4540, 4541, 4542, 4543, 4544, 4545, 4546, 4547, 4548, 4549, 4550, 4552, 4553, 4554, 4555, 4556, 4557, 4558, 4559, 4560, 4561, 4562, 4563, 4564, 4565, 4567, 4568, 4572, 4575, 4577, 4580, 4581, 4583, 4585, 4588, 4589, 4590, 4591, 4592, 4593, 4594, 4597, 4598, 4599, 4600, 4602, 4603, 4604, 4605, 4606, 4609, 4610, 4611, 4612, 4613, 4614, 4615, 4616, 4617, 4618, 4619, 4620, 4621, 4622, 4625, 4626, 4627, 4628, 4629, 4630, 4631, 4632, 4633, 4634, 4635, 4637, 4638, 4639, 4640, 4641, 4642, 4643, 4644, 4645, 4646, 4650, 4654, 4656, 4657, 4658, 4659, 4660, 4662, 4663, 4664, 4665, 4666, 4667, 4668, 4669, 4670, 4671, 4672, 4673, 4674, 4675, 4676, 4677, 4678, 4679, 4680, 4681, 4682, 4683, 4684, 4687, 4688, 4689, 4690, 4691, 4692, 4693, 4694, 4695, 4697, 4698, 4699, 4700, 4701, 4702, 4703, 4704, 4705, 4706, 4707, 4709, 4710, 4711, 4713, 4714, 4715, 4716, 4717, 4718, 4719, 4720, 4721, 4722, 4723, 4724, 4725, 4726, 4727, 4728, 4729, 4730, 4732, 4733, 4734, 4736, 4737, 4738, 4739, 4742, 4743, 4744, 4745, 4746, 4747, 4750, 4755, 4756, 4759, 4760, 4763, 4764, 4765, 4766, 4767, 4768, 4769, 4770, 4771, 4772, 4773, 4774, 4776, 4777, 4779, 4780, 4781, 4782, 4783, 4784, 4786, 4787, 4788, 4789, 4790, 4791, 4792, 4793, 4794, 4795, 4796, 4797, 4798, 4799, 4803, 4804, 4805, 4810, 4811, 4812, 4813, 4814, 4815, 4817, 4818, 4819, 4820, 4821, 4822, 4823, 4824, 4825, 4826, 4827, 4828, 4829, 4830, 4831, 4832, 4833, 4834, 4835, 4836, 4837, 4838, 4839, 4840, 4841, 4842, 4843, 4844, 4845, 4846, 4847, 4848, 4849, 4850, 4852, 4853, 4854, 4855, 4856, 4858, 4859, 4860, 4863, 4864, 4865, 4866, 4868, 4869, 4870, 4871, 4872, 4873, 4874, 4875, 4876, 4877, 4878, 4879, 4880, 4881, 4882, 4883, 4884, 4885, 4886, 4887, 4888, 4890, 4891, 4892, 4893, 4894, 4895, 4896, 4897, 4898, 4899, 4900, 4901, 4902, 4903, 4904, 4905, 4906, 4907, 4908, 4909, 4910, 4912, 4915, 4917, 4918, 4919, 4920, 4921, 4922, 4923, 4925, 4926, 4930, 4931, 4934, 4935, 4936, 4937, 4938, 4939, 4940, 4941, 4942, 4943, 4944, 4945, 4946, 4948, 4949, 4950, 4951, 4953, 4956, 4957, 4958, 4959, 4960, 4961, 4962, 4963, 4964, 4965, 4966, 4969, 4970, 4972, 4973, 4974, 4975, 4976, 4977, 4978, 4980, 4982, 4983, 4984, 4985, 4987, 4988, 4989, 4990, 4991, 4992, 4994, 4995, 4996, 4997, 4998, 5005, 5006, 5007, 5008, 5009, 5010, 5011, 5012, 5013, 5014, 5015, 5016, 5017, 5018, 5019, 5020, 5021, 5022, 5023, 5024, 5025, 5026, 5027, 5028, 5029, 5030, 5032, 5033, 5034, 5035, 5036, 5041, 5043, 5044, 5045, 5046, 5050, 5051, 5052, 5053, 5054, 5055, 5056, 5057, 5058, 5059, 5060, 5064, 5065, 5066, 5068, 5069, 5070, 5073, 5074, 5077, 5079, 5080, 5081, 5083, 5084, 5085, 5086, 5087, 5088, 5089, 5090, 5091, 5092, 5093, 5094, 5095, 5096, 5097, 5098, 5099, 5100, 5101, 5102, 5105, 5107, 5108, 5109, 5110, 5111, 5113, 5114, 5115, 5116, 5117, 5118, 5119, 5121, 5122, 5123, 5124, 5125, 5126, 5127, 5128, 5129, 5130, 5131, 5132, 5133, 5135, 5136, 5137, 5138, 5139, 5140, 5141, 5142, 5143, 5144, 5145, 5146, 5147, 5148, 5149, 5150, 5151, 5152, 5153, 5154, 5155, 5156, 5157, 5158, 5159, 5160, 5161, 5162, 5163, 5164, 5166, 5167, 5168, 5169, 5171, 5173, 5174, 5175, 5178, 5179, 5181, 5182, 5184, 5185, 5187, 5188, 5189, 5191, 5192, 5193, 5194, 5195, 5196, 5197, 5198, 5199, 5200, 5201, 5202, 5203, 5204, 5205, 5206, 5207, 5208, 5209, 5210, 5211, 5212, 5213, 5214, 5215, 5216, 5217, 5219, 5220, 5221, 5223, 5224, 5226, 5227, 5230, 5231, 5232, 5233, 5234, 5235, 5236, 5237, 5242, 5243, 5244, 5245, 5246, 5247, 5248, 5249, 5250, 5252, 5253, 5254, 5255, 5256, 5258, 5259, 5260, 5261, 5262, 5264, 5265, 5266, 5268, 5269, 5270, 5284, 5287, 5292, 5295, 5296, 5297, 5298, 5299, 5300, 5301, 5302, 5303, 5304, 5305, 5306, 5307, 5308, 5309, 5311, 5313, 5315, 5316, 5317, 5318, 5321, 5322, 5323, 5324, 5325, 5326, 5327, 5328, 5329, 5330, 5332, 5334, 5335, 5336, 5339, 5340, 5341, 5342, 5344, 5345, 5346, 5347, 5349, 5350, 5351, 5352, 5353, 5354, 5358, 5359, 5360, 5361, 5363, 5364, 5365, 5366, 5368, 5369, 5370, 5371, 5372, 5373, 5374, 5377, 5378, 5379, 5380, 5381, 5382, 5383, 5384, 5385, 5386, 5387, 5389, 5390, 5391, 5394, 5395, 5396, 5397, 5398, 5399, 5402, 5403, 5404, 5405, 5406, 5408, 5409, 5411, 5412, 5413, 5416, 5417, 5418, 5419, 5420, 5421, 5422, 5423, 5424, 5425, 5426, 5427, 5428, 5429, 5430, 5431, 5432, 5433, 5434, 5435, 5436, 5437, 5438, 5442, 5443, 5444, 5447, 5448, 5449, 5450, 5451, 5452, 5453, 5454, 5455, 5457, 5458, 5459, 5460, 5461, 5462, 5463, 5465, 5466, 5467, 5469, 5470, 5471, 5472, 5473, 5474, 5475, 5476, 5477, 5478, 5479, 5480, 5481, 5482, 5483, 5485, 5486, 5487, 5488, 5489, 5490, 5491, 5492, 5493, 5494, 5495, 5496, 5497, 5501, 5502, 5503, 5508, 5509, 5510, 5511, 5512, 5513, 5514, 5515, 5516, 5517, 5518, 5519, 5520, 5521, 5522, 5523, 5525, 5526, 5527, 5528, 5529, 5530, 5531, 5532, 5533, 5544, 5545, 5546, 5547, 5548, 5549, 5550, 5551, 5552, 5553, 5554, 5555, 5556, 5557, 5559, 5560, 5561, 5562, 5563, 5564, 5565, 5566, 5567, 5568, 5569, 5573, 5574, 5575, 5576, 5577, 5578, 5579, 5580, 5581, 5582, 5583, 5584, 5585, 5586, 5587, 5589, 5592, 5593, 5594, 5595, 5601, 5602, 5603, 5604, 5605, 5606, 5607, 5608, 5609, 5610, 5611, 5612, 5613, 5614, 5615, 5616, 5617, 5618, 5619, 5621, 5623, 5624, 5625, 5626, 5627, 5628, 5631, 5632, 5633, 5636, 5637, 5638, 5640, 5641, 5642, 5643, 5644, 5646, 5647, 5648, 5649, 5650, 5651, 5652, 5655, 5656, 5657, 5658, 5659, 5660, 5662, 5663, 5664, 5665, 5666, 5667, 5670, 5671, 5672, 5674, 5676, 5677, 5678, 5679, 5680, 5681, 5682, 5683, 5684, 5687, 5689, 5690, 5691, 5692, 5694, 5695, 5696, 5697, 5698, 5700, 5701, 5702, 5703, 5704, 5707, 5708, 5709, 5710, 5711, 5712, 5713, 5714, 5715, 5716, 5717, 5719, 5721, 5722, 5723, 5724, 5725, 5726, 5727, 5728, 5729, 5730, 5733, 5734, 5735, 5737, 5739, 5740, 5741, 5742, 5745, 5746, 5747, 5748, 5749, 5750, 5753, 5754, 5755, 5756, 5757, 5758, 5759, 5760, 5761, 5762, 5763, 5764, 5765, 5766, 5767, 5768, 5769, 5770, 5771, 5772, 5773, 5774, 5775, 5776, 5777, 5778, 5779, 5780, 5781, 5782, 5783, 5784, 5785, 5786, 5787, 5788, 5789, 5791, 5792, 5793, 5794, 5799, 5800, 5801, 5802, 5803, 5804, 5805, 5806, 5807, 5808, 5809, 5810, 5811, 5812, 5813, 5816, 5817, 5818, 5819, 5820, 5821, 5823, 5824, 5825, 5826, 5827, 5828, 5829, 5830, 5831, 5832, 5833, 5834, 5835, 5836, 5837, 5838, 5841, 5842, 5843, 5846, 5847, 5848, 5849, 5850, 5851, 5852, 5853, 5854, 5855, 5856, 5857, 5858, 5859, 5860, 5861, 5863, 5864, 5865, 5866, 5867, 5868, 5869, 5870, 5871, 5872, 5873, 5874, 5877, 5878, 5879, 5881, 5882, 5883, 5886, 5887, 5888, 5889, 5890, 5891, 5892, 5893, 5894, 5895, 5896, 5897, 5898, 5899, 5900, 5901, 5902, 5903, 5905, 5906, 5907, 5908, 5910, 5911, 5912, 5913, 5914, 5915, 5916, 5917, 5918, 5919, 5920, 5921, 5922, 5923, 5924, 5925, 5926, 5927, 5928, 5929, 5930, 5932, 5933, 5934, 5935, 5936, 5937, 5938, 5939, 5940, 5941, 5942, 5943, 5944, 5945, 5946, 5947, 5948, 5949, 5950, 5951, 5952, 5953, 5955, 5956, 5957, 5958, 5959, 5961, 5962, 5963, 5966, 5967, 5968, 5971, 5972, 5973, 5974, 5975, 5976, 5980, 5981, 5986, 5988, 5990, 5991, 5992, 5993, 5994, 5995, 5996, 5997, 5998, 5999, 6000, 6001, 6002, 6004, 6005, 6006, 6008, 6009, 6010, 6011, 6013, 6014, 6016, 6017, 6018, 6019, 6020, 6021, 6022, 6023, 6024, 6025, 6026, 6027, 6028, 6029, 6030, 6031, 6032, 6033, 6034, 6035, 6036, 6037, 6038, 6039, 6040, 6041, 6043, 6046, 6047, 6049, 6050, 6051, 6052, 6055, 6056, 6058, 6059, 6060, 6061, 6062, 6063, 6064, 6065, 6066, 6069, 6070, 6071, 6072, 6073, 6074, 6075, 6076, 6077, 6078, 6079, 6080, 6081, 6084, 6085, 6086, 6087, 6088, 6089, 6090, 6091, 6092, 6093, 6095, 6099, 6100, 6101, 6102, 6103, 6104, 6105, 6106, 6108, 6109, 6110, 6111, 6114, 6115, 6116, 6117, 6118, 6119, 6120, 6122, 6123, 6124, 6125, 6126, 6127, 6128, 6129, 6132, 6133, 6134, 6135, 6138, 6139, 6140, 6143, 6144, 6145, 6146, 6148, 6149, 6150, 6151, 6152, 6153, 6154, 6156, 6158, 6159, 6160, 6161, 6162, 6163, 6166, 6167, 6169, 6172, 6173, 6174, 6177, 6180, 6181, 6182, 6184, 6185, 6186, 6187, 6188, 6189, 6190, 6191, 6192, 6194, 6195, 6196, 6197, 6198, 6199, 6200, 6201, 6202, 6203, 6204, 6206, 6207, 6208, 6209, 6210, 6211, 6212, 6213, 6214, 6215, 6217, 6218, 6219, 6220, 6223, 6224, 6225, 6226, 6227, 6228, 6229, 6230, 6231, 6232, 6233, 6237, 6238, 6239, 6240, 6241, 6242, 6243, 6244, 6245, 6247, 6249, 6250, 6251, 6252, 6253, 6255, 6257, 6258, 6259, 6260, 6261, 6264, 6265, 6266, 6269, 6270, 6271, 6272, 6273, 6274, 6275, 6276, 6277, 6278, 6279, 6280, 6283, 6285, 6286, 6289, 6291, 6292, 6293, 6294, 6295, 6296, 6297, 6298, 6299, 6300, 6302, 6305, 6306, 6307, 6308, 6309, 6310, 6311, 6312, 6313, 6314, 6315, 6316, 6317, 6324, 6325, 6327, 6328, 6329, 6330, 6331, 6332, 6333, 6334, 6336, 6337, 6338, 6341, 6342, 6343, 6344, 6348, 6349, 6356, 6357, 6358, 6359, 6360, 6362, 6363, 6364, 6365, 6366, 6367, 6369, 6370, 6371, 6372, 6373, 6374, 6375, 6376, 6377, 6378, 6379, 6380, 6381, 6382, 6383, 6384, 6385, 6386, 6387, 6388, 6389, 6390, 6392, 6393, 6394, 6395, 6396, 6397, 6398, 6399, 6400, 6401, 6402, 6403, 6404, 6405, 6406, 6407, 6410, 6411, 6412, 6415, 6416, 6417, 6418, 6419, 6420, 6421, 6422, 6426, 6427, 6428, 6429, 6430, 6431, 6432, 6433, 6434, 6435, 6436, 6437, 6438, 6439, 6440, 6441, 6442, 6443, 6444, 6446, 6447, 6448, 6449, 6450, 6451, 6452, 6453, 6454, 6455, 6456, 6457, 6458, 6459, 6460, 6461, 6462, 6464, 6465, 6466, 6467, 6469, 6470, 6471, 6472, 6473, 6474, 6475, 6476, 6477, 6478, 6483, 6484, 6485, 6486, 6487, 6488, 6489, 6490, 6491, 6492, 6493, 6494, 6495, 6498, 6499, 6500, 6501, 6502, 6503, 6506, 6507, 6508, 6509, 6510, 6511, 6512, 6513, 6514, 6515, 6516, 6517, 6518, 6519, 6520, 6521, 6522, 6523, 6524, 6525, 6526, 6527, 6528, 6529, 6530, 6531, 6532, 6533, 6534, 6537, 6539, 6540, 6541, 6542, 6546, 6547, 6548, 6549, 6550, 6552, 6553, 6558, 6559, 6560, 6561, 6562, 6563, 6564, 6565, 6566, 6567, 6570, 6571, 6572, 6573, 6574, 6575, 6576, 6578, 6579, 6581, 6582, 6583, 6584, 6585, 6586, 6590, 6591, 6592, 6593, 6595, 6596, 6597, 6598, 6599, 6600, 6601, 6602, 6603, 6604, 6605, 6607, 6608, 6609, 6610, 6611, 6612, 6613, 6615, 6616, 6617, 6618, 6620, 6621, 6622, 6623, 6624, 6625, 6626, 6629, 6630, 6631, 6632, 6633, 6634, 6635, 6636, 6638, 6639, 6640, 6641, 6643, 6644, 6645, 6646, 6647, 6648, 6649, 6650, 6651, 6652, 6653, 6654, 6655, 6656, 6657, 6658, 6666, 6667, 6669, 6670, 6671, 6672, 6673, 6674, 6675, 6677, 6679, 6681, 6682, 6683, 6684, 6685, 6686, 6687, 6688, 6689, 6691, 6692, 6698, 6699, 6700, 6703, 6704, 6705, 6706, 6707, 6708, 6709, 6710, 6711, 6712, 6713, 6714, 6715, 6716, 6717, 6718, 6719, 6720, 6721, 6724, 6725, 6726, 6727, 6728, 6729, 6730, 6731, 6732, 6734, 6736, 6737, 6738, 6739, 6740, 6741, 6742, 6743, 6744, 6745, 6746, 6747, 6750, 6751, 6752, 6753, 6754, 6756, 6757, 6758, 6759, 6760, 6761, 6764, 6767, 6770, 6771, 6772, 6773, 6774, 6775, 6776, 6777, 6778, 6779, 6780, 6781, 6782, 6783, 6784, 6785, 6786, 6788, 6790, 6792, 6793, 6794, 6795, 6797, 6800, 6803, 6804, 6805, 6806, 6807, 6809, 6810, 6811, 6812, 6813, 6814, 6819, 6820, 6821, 6822, 6823, 6824, 6825, 6826, 6827, 6828, 6831, 6832, 6833, 6834, 6835, 6836, 6837, 6838, 6839, 6841, 6842, 6843, 6844, 6845, 6846, 6847, 6848, 6849, 6851, 6853, 6854, 6855, 6856, 6857, 6861, 6862, 6863, 6864, 6865, 6866, 6870, 6871, 6874, 6875, 6876, 6877, 6878, 6879, 6880, 6881, 6882, 6883, 6884, 6886, 6887, 6888, 6889, 6890, 6891, 6892, 6893, 6894, 6895, 6897, 6898, 6900, 6901, 6902, 6903, 6904, 6905, 6906, 6907, 6909, 6910, 6912, 6913, 6914, 6915, 6916, 6917, 6918, 6919, 6920, 6921, 6922, 6923, 6924, 6925, 6926, 6927, 6928, 6942, 6943, 6944, 6945, 6946, 6948, 6949, 6950, 6953, 6954, 6955, 6956, 6957, 6958, 6959, 6960, 6961, 6962, 6963, 6964, 6965, 6966, 6967, 6968, 6969, 6970, 6971, 6972, 6974, 6975, 6976, 6977, 6978, 6979, 6980, 6981, 6982, 6983, 6984, 6985, 6986, 6987, 6988, 6989, 6990, 6991, 6992, 6994, 6997, 6998, 6999, 7000, 7001, 7008, 7009, 7010, 7011, 7012, 7013, 7015, 7016, 7017, 7018, 7019, 7021, 7022, 7023, 7024, 7025, 7026, 7029, 7030, 7031, 7033, 7034, 7036, 7037, 7039, 7040, 7041, 7042, 7043, 7045, 7046, 7047, 7048, 7049, 7050, 7051, 7052, 7053, 7054, 7055, 7057, 7058, 7059, 7060, 7061, 7062, 7063, 7064, 7065, 7066, 7067, 7068, 7069, 7070, 7071, 7072, 7073, 7074, 7075, 7076, 7077, 7078, 7079, 7080, 7081, 7082, 7084, 7085, 7086, 7087, 7088, 7089, 7090, 7091, 7092, 7093, 7094, 7095, 7096, 7097, 7098, 7099, 7100, 7101, 7102, 7103, 7104, 7105, 7108, 7109, 7110, 7111, 7112, 7113, 7114, 7115, 7116, 7117, 7118, 7119, 7120, 7121, 7122, 7125, 7126, 7127, 7128, 7129, 7130, 7131, 7132, 7133, 7134, 7135, 7136, 7137, 7138, 7139, 7140, 7142, 7143, 7147, 7148, 7149, 7154, 7155, 7156, 7157, 7158, 7159, 7160, 7161, 7164, 7165, 7166, 7167, 7168, 7169, 7170, 7171, 7172, 7173, 7174, 7175, 7176, 7177]
if __name__ == '__main__':
    splitted = companies.split("\n")
    companies = []
    extra_wds = ["Inc.", "Inc", "Incorporated", "Corporation", "Corp.", "Corp", "Class", "Series", "Preferred",
                 "Acquisition", "Depositary", "Holdings", "Holding", "Ordinary", "Fund", "Group", "Trust", "Income",
                 "Cumulative", "Non-Cumulative", "Company", "Interest", "Ltd.", "Ltd", "Limited", "Financial", "Unit",
                 "Units", "Beneficial", "Warrant", "Warrants", "Perpetual", "Capital", "Redeemable", "Therapeutics",
                 "Energy", "Bancorp", "Bancorporation", "International", "Notes", "Rate", "Pharmaceuticals", "Share",
                 "Technologies", "Technology", "Global", "Municipal", "Investment", "ETF", "(", "Partners", "Equity",
                 "Fixed-to-Floating","Realty", "S.A.", "Industries", "Systems", "Co.", "Senior", "Services",
                 "Subordinated", "LP", "L.P.", "PLC", "plc", "Health", "Resources", "Each", "Properties","Healthcare",
                 "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]

    extra_phrases = ["Common Stock", "American Depositary Shares", "Common Shares", "Ordinary Shares",
                     "Depositary Shares", "("]
    splitted = splitted[1:]

    company_indices = []

    for i, company in enumerate(splitted):
        if company.startswith("The"):
            company = company[4:]
        for extra in extra_phrases:
            if extra in company:
                company = company[:company.index(extra)].strip()
        chucks = company.split(" ")
        for chuck in chucks:
            if chuck != chucks[0] and (chuck in extra_wds or "%" in chuck or len(chuck) == 1):
                company = company[:company.index(chuck)].strip()
                break

        if company not in companies:
            company_indices.append(i)
            companies.append(company)

        # for chuck in chucks:
        #     if chuck not in commons.keys():
        #         commons[chuck] = 1
        #     else:
        #         commons[chuck] += 1

    # commons = {k: v for k, v in sorted(commons.items(), key=lambda item: item[1], reverse=True)}
    with open('companies.txt', 'w') as f:
        for company in companies:
            f.write("%s\n" % company.lower())

    print(company_indices)
