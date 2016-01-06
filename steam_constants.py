render_timeout = 15
load_errors = ['The server is temporarily unable to service your request', 'You\'ve made too many requests recently.']
render_search = 'http://steamcommunity.com/market/search/render/?query=&' \
                'start=0&' \
                'count=100&' \
                'sort_column=price&' \
                'sort_dir=asc&' \
                'category_730_Weapon[]=tag_weapon_item&' \
                'currency=3&'
FN = 'category_730_Exterior[]=tag_WearCategory0&'
MW = 'category_730_Exterior[]=tag_WearCategory1&'
FT = 'category_730_Exterior[]=tag_WearCategory2&'
WW = 'category_730_Exterior[]=tag_WearCategory3&'
BS = 'category_730_Exterior[]=tag_WearCategory4&'
Nilla = 'category_730_Exterior[]=tag_WearCategoryNA&'
render_names = ['m4a1', 'knife_m9_bayonet', 'bayonet', 'ak47']
render_wears = {'knife_m9_bayonet': [FN, MW, FT, BS, Nilla],
                'bayonet': [FN, MW, Nilla],
                'ak47': [FN, MW, BS]}
render_pls = "\"normal_price\\\">$"                             # render price left shell
render_prs = " USD<\\/span>"                                    # render price right shell
render_wls = ";\\\">"                                           # render weapon left shell
render_wrs = "<\\/span>\\r\\n\\t\\t\\t<br"                      # render weapon right shell

market_template_link = 'https://steamcommunity.com/market/listings/730/'