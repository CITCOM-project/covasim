def get_country_household_sizes():
    '''
    This file contains the data from https://population.un.org/household/exceldata/population_division_UN_Houseshold_Size_and_Composition_2019.xlsx
    '''

    data = {'afghanistan': 8.03673885632185, 'albania': 3.29961078595413, 'angola': 4.81565736350675, 'argentina': 3.25865830068813, 'armenia': 3.54208464567852, 'aruba': 2.88944680362676, 'australia': 2.54677670219101, 'austria': 2.2679986813942, 'azerbaijan': 4.54852867256945, 'bahamas': 3.39563829580179, 'bangladesh': 4.46971417265744, 'belarus': 2.42672287258474, 'belgium': 2.3234556991274, 'benin': 5.18649416042462, 'bermuda': 2.26230845629966, 'bhutan': '..', 'bolivia (plurinational state of)': 3.5304590604877, 'botswana': '..', 'brazil': 3.31148982178934, 'brunei darussalam': '..', 'bulgaria': '..', 'burkina faso': 5.9244534660988, 'burundi': 4.83019337510145, 'cambodia': 4.61184313032466, 'cameroon': 4.99234197870694, 'canada': 2.44882526250561, 'cayman islands': '..', 'central african republic': 4.90678370265536, 'chad': 5.77717953423277, 'chile': 3.57367786514165, 'china': '..', 'china, hong kong sar': 2.83461753317284, 'china, macao sar': 3.06609687213535, 'colombia': 3.52685205109591, 'comoros': 5.37160110924601, 'congo': 4.3074023816909, 'cook islands': '..', 'costa rica': 3.4565365191543, 'croatia': 2.79539616520456, 'cuba': 3.13669985331294, 'cyprus': 2.75874054385606, 'czechia': 2.34028102530627, "côte d'ivoire": 5.09006311104997, "dem. people's rep. of korea": 3.92930886623476, 'dem. republic of the congo': 5.3020675050332, 'dominican republic': 3.47793354224461, 'ecuador': 3.77918714053727, 'egypt': 4.13085758320921, 'el salvador': 4.06997716976167, 'estonia': 2.29751757241856, 'ethiopia': 4.61457783976785, 'fiji': 4.57243740637706, 'finland': 2.07495909856428, 'france': 2.22205672177275, 'french guiana': 3.45475745050298, 'french polynesia': '..', 'gabon': 4.09759781345222, 'gambia': 8.22968138889476, 'georgia': 3.33786841939178, 'germany': 2.13881151612819, 'ghana': 3.49288612007447, 'greece': 2.55549939051526, 'guadeloupe': 2.2965290141222, 'guatemala': 4.80571376455854, 'guinea': 6.25081903910384, 'guyana': 3.79520268281347, 'haiti': 4.29334977105548, 'honduras': 4.46749153441871, 'hungary': 2.36188228680656, 'india': 4.57218899216434, 'indonesia': 3.85945273578042, 'iran (islamic republic of)': '..', 'iraq': 7.70302801425421, 'ireland': 2.72662748578172, 'isle of man': 2.28392472667282, 'israel': 3.14194539238823, 'italy': 2.40259252424227, 'jamaica': 3.06092285168149, 'japan': 2.33062334276867, 'jordan': 4.71876280946192, 'kazakhstan': 3.49662788873433, 'kenya': 3.63882380648678, 'kyrgyzstan': 4.21447820303052, "lao people's dem. republic": 5.76530408354279, 'latvia': 2.37726020355352, 'lesotho': 3.34493465723311, 'liberia': 4.94573145418242, 'liechtenstein': 2.32024833473453, 'lithuania': 2.38252653639661, 'luxembourg': 2.4130606765277, 'madagascar': 4.94926350622938, 'malawi': 4.50891809012562, 'malaysia': 4.57438144364422, 'maldives': 5.39992241878289, 'mali': 5.81114539185664, 'malta': 2.67215547333604, 'martinique': 2.24845954611123, 'mauritius': 3.47529761733847, 'mayotte': 4.10216586217368, 'mexico': 3.74017497083236, 'mongolia': 4.32143522139053, 'montenegro': 3.21401150633056, 'morocco': 5.2361663882699, 'mozambique': 4.36636284544404, 'myanmar': 4.22379426809677, 'namibia': 4.2382239682248, 'nepal': 4.23936444257142, 'netherlands': 2.22639156224361, 'new caledonia': '..', 'new zealand': 2.67282310110229, 'nicaragua': 4.91987664489436, 'niger': 5.91684917249255, 'nigeria': 4.90142866431412, 'norway': 2.21543726122912, 'oman': 8.01771089432877, 'pakistan': 6.80447866248035, 'palau': '..', 'panama': 3.67008259406546, 'papua new guinea': 5.43010129941242, 'paraguay': 4.63244207422508, 'peru': 3.75218227894024, 'philippines': 4.22666134737057, 'poland': 2.81580919217578, 'portugal': 2.58091571980891, 'puerto rico': 2.67050237031479, 'republic of korea': 2.52940626434054, 'republic of moldova': 2.88879842375214, 'romania': 2.66718752028833, 'russian federation': 2.58354936060394, 'rwanda': 4.25929245684135, 'réunion': 2.64317813908999, 'saint helena': '..', 'saint kitts and nevis': '..', 'saint-barthélemy': 2.42479408018303, 'saint-martin (french part)': 2.56405506963395, 'samoa': 6.75141966759003, 'sao tome and principe': '..', 'senegal': 8.66164024149629, 'serbia': 2.87916488134907, 'seychelles': '..', 'sierra leone': 5.89907498760491, 'singapore': 3.29143482965652, 'sint maarten (dutch part)': 2.5798973082309, 'slovakia': 2.89586273531529, 'slovenia': 2.46740138518368, 'south africa': 3.36220315919585, 'south sudan': 5.9479727880003, 'spain': 2.57551003141505, 'state of palestine': 5.88706697459584, 'sudan': 5.59037592812814, 'suriname': 3.94080817734868, 'swaziland': 4.73718042366691, 'switzerland': 2.24459563606459, 'tajikistan': 5.99313917762588, 'thailand': '..', 'timor-leste': 5.26791911327593, 'togo': 4.55131040551872, 'tokelau': 5.24390243902439, 'trinidad and tobago': '..', 'turkey': 4.07131378673696, 'uganda': 4.53433756282406, 'ukraine': 2.45829841936276, 'united kingdom': 2.3468577528801, 'united republic of tanzania': 4.85154785176155, 'united states of america': 2.49113173309193, 'uruguay': 2.79554666617926, 'uzbekistan': 5.24207713780226, 'venezuela (bolivarian republic of)': 4.33136162221914, 'viet nam': '..', 'yemen': 6.67268064092928, 'zambia': 5.13078885536711, 'zimbabwe': 4.07717933273453}

    return data
