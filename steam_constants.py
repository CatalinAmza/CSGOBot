render_timeout = 15
load_errors = ['The server is temporarily unable to service your request', 'You\'ve made too many requests recently.']
render_search = 'http://steamcommunity.com/market/search/render/?query=&' \
                'start=0&' \
                'count=100&' \
                'sort_column=price&' \
                'sort_dir=asc&' \
                'category_730_Weapon[]=tag_weapon_m4a1&' \
                'category_730_Exterior[]=tag_WearCategory2&' \
                'category_730_Exterior[]=tag_WearCategory1&' \
                'category_730_Exterior[]=tag_WearCategory0&' \
                'currency=3'
market_template_link = 'https://steamcommunity.com/market/listings/730/'

render_pls = "\"normal_price\\\">$"                             # render price left shell
render_prs = " USD<\\/span>"                                    # render price right shell
render_wls = ";\\\">"                                           # render weapon left shell
render_wrs = "<\\/span>\\r\\n\\t\\t\\t<br"                      # render weapon right shell