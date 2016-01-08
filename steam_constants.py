render_timeout = 15
load_errors = ['The server is temporarily unable to service your request', 'You\'ve made too many requests recently.']
render_search = 'http://steamcommunity.com/market/search/render/?' \
                'query=&' \
                'start=0&' \
                'count=100&' \
                'sort_column=price&' \
                'sort_dir=asc&' \
                'category_730_Weapon[]=tag_weapon_item&' \
                'currency=3&'
render_bayonets = 'http://steamcommunity.com/market/search/render/?' \
                        'query=bayonet NOT scorched NOT stained NOT boreal NOT safari&' \
                        'start=0&' \
                        'count=100&' \
                        'sort_column=price&' \
                        'sort_dir=asc&' \
                        'category_730_Weapon[]=any&' \
                        'currency=3&'
render_guns = 'http://steamcommunity.com/market/search/render/?' \
              'query=Exterior NOT \"USP-S\" NOT \"FAMAS\" NOT \"AUG\" NOT \"Tec-9\" NOT \"Galil\" NOT \"CZ75-Auto\" NOT \"SG 553\" NOT \"P2000\" NOT \"Five-SeveN\" ' \
                    'NOT \"Dual Berettas\" NOT \"SCAR-20\" NOT \"SSG 08\" NOT \"G3SG1\" NOT \"R8 Revolver\" NOT \"(Dragon King)\" NOT \"Catacombs\" NOT \"Bunsen Burner\" ' \
                    'NOT \"Souvenir\" NOT \"Death Rattle\" NOT \"Urban DDPAT\" NOT \"Atomic Alloy\" NOT \"18 | Brass\" NOT \"AK-47 | Predator\" NOT \"AK-47 | Black\" ' \
                    'NOT \"VariCamo\" NOT \"M4A4 | Tornado\" NOT \"Grinder\" NOT \"Blood Tiger\" NOT \"Wraiths\" NOT \"Safari Mesh\" NOT \"Elite Build\" NOT \"Boreal Forest\" NOT \"Candy Apple\" ' \
                    'NOT \"Desert Storm\" NOT \"18 | Night\" NOT \"Jungle Tiger\" NOT \"Groundwater\" NOT \"Blue Fissure\"  NOT \"Faded Zebra\" NOT \"Evil Daimyo\"  NOT \"M4A4 | Griffin\" ' \
                    'NOT \"-S | Guardian\" NOT \"Desert Storm\" NOT \"Steel Disruption\" NOT \"Jungle Spray\" NOT \"Sand Dune\" NOT \"Worm God\" NOT \"Emerald Pinstripe\" NOT \"-S | Basilisk\" ' \
                    'NOT \"-S | Nitro\" NOT \"Pit Viper\" NOT \"Desert-Strike\" NOT \"Blue Laminate\" NOT \"47 | Cartel\" NOT \"Water Elemental\" NOT \"18 | Reactor\" NOT \"Sun in Leo\" ' \
                    'NOT \"Snake Camo\" NOT \"Bright Water\" NOT \"Dark Water\" NOT \"Corticera\" NOT \"Bullet Rain\" NOT \"47 | First Class\" NOT \"47 | Jet Set\" NOT \"Man-o\'-war\" ' \
                    'NOT \"AWP | Redline\" NOT \"Electric Hive\" NOT \"AWP | BOOM\" NOT \"Pink DDPAT\" NOT \"M4A4 | Zirka\" NOT \"Red Laminate\" ' \
                    'NOT \"Desert Eagle\" NOT \"Twilight Galaxy\" NOT \"P250 | Muertos\" NOT \"P250 | Cartel\" NOT \"P250 | Undertow\" NOT \"P250 | Mehndi\" NOT \"P250 | Franklin\" ' \
                    'NOT \"P250 | Wingshot\" NOT \"P250 | Supernova\" NOT \"P250 | Splash\" NOT \"P250 | Valence\" NOT \"P250 | Steel Disruption\" NOT \"P250 | Hive\" ' \
                    'NOT \"| Modern Hunter\" NOT \"P250 | Crimson Kimono\" NOT \"P250 | Contamination\" NOT \"P250 | Metallic DDPAT\" NOT \"P250 | Mint Kimono\" NOT \"P250 | Gunsmoke\" ' \
                    'NOT \"P250 | Facets\" NOT \"P250 | Sand Dune\" NOT \"P250 | Boreal Forest\" NOT \"P250 | Bone Mask\" NOT \"Dragon Tattoo\"&' \
              'start=0&' \
              'count=100&' \
              'search_descriptions=1&' \
              'sort_column=price&' \
              'sort_dir=asc&' \
              'category_730_Weapon[]=any&' \
              'category_730_Type[]=tag_CSGO_Type_Pistol&' \
              'category_730_Type[]=tag_CSGO_Type_Rifle&' \
              'category_730_Type[]=tag_CSGO_Type_SniperRifle&'
FN = 'category_730_Exterior[]=tag_WearCategory0&'
MW = 'category_730_Exterior[]=tag_WearCategory1&'
FT = 'category_730_Exterior[]=tag_WearCategory2&'
WW = 'category_730_Exterior[]=tag_WearCategory3&'
BS = 'category_730_Exterior[]=tag_WearCategory4&'
Nilla = 'category_730_Exterior[]=tag_WearCategoryNA&'
render_names = ['m4a1', 'knife_m9_bayonet', 'bayonets', 'ak47', 'bayonet', 'p250', 'glock', 'awp', 'm4a1_silencer']
render_wears = {'knife_m9_bayonet': [FN, MW, FT, BS, Nilla],
                'bayonet': [FN, MW, Nilla],
                'ak47': [FN, MW, BS],
                'bayonets': [FN, MW, BS, Nilla],
                'guns': [FN, MW]}
pack = {'bayonets': ['knife_m9_bayonet', 'bayonet'],
        'guns': ['glock', 'p250', 'ak47', 'awp', 'm4a1_silencer', 'm4a1']}
urls = {'bayonets': render_bayonets,
        'guns': render_guns}
render_pls = "\"normal_price\\\">$"                             # render price left shell
render_prs = " USD<\\/span>"                                    # render price right shell
render_wls = ";\\\">"                                           # render weapon left shell
render_wrs = "<\\/span>\\r\\n\\t\\t\\t<br"                      # render weapon right shell

market_template_link = 'https://steamcommunity.com/market/listings/730/'