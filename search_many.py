from steam_constants import *
import webbrowser
import time
import requests
from tools.capsule import *
import winsound

Freq = 800
Dur = 200                                                                            # 0.2 seconds seems more than enough

class PageLoader:
    def __init__(self, wait_for_timeout=True, session=None):
        self.wft = wait_for_timeout
        self.dmgctrl = 0                                                             # when loading the page takes too much, subtract that time for the timeout
        if self.wft:
            qprint('Between page loads we\'ll be waiting %d seconds to comply with Steam Market.' % render_timeout)
        if session:
            self.session = session
        else:
            self.session = requests

    def load_backbone(self, url):
        if self.wft:
            time.sleep(render_timeout - self.dmgctrl)
        try:
            s_now = time.time()
            source = self.session.get(url).content.decode()                          # page source as a string
            if len(source) > 10 and no_conflicts(load_errors, source):
                self.dmgctrl = int(time.time() - s_now)
                return source
            raise Exception()
        except:
            return False

    def load(self, url):
        qprint('Single load attempt for %s executing...' % str(url), end=' ')
        source = self.load_backbone(url)
        if not source:
            qprint('Operatation failed.')
        else:
            qprint('Page successfully loaded.')
        return source

    def rload(self, url):                                                            # recursive page load
        qprint('Recursively trying to load %s.' % str(url))
        source = False
        count = 1
        while not source:
            qprint('Executing attempt No. %d: ' % count, end='')
            count += 1
            source = self.load_backbone(url)
            if source:
                qprint('page successfully loaded.')
                return source
            else:
                qprint('operation failed. Waiting %d seconds...' % render_timeout)


def no_conflicts(errors, subject):                                                   # no_conflicts(List<String>, String)
    for error in errors:
        if error in subject:
            return False
    return True


def sift_weapons(url, pl):
    source = pl.rload(url).replace("StatTrak\\u2122", "StatTrak™").replace('\\u2605', '★')
    weapons = get_all_cores(source, render_wls, render_wrs, 1100)
    prices = get_all_cores(source, render_pls, render_prs)
    for i in range(len(weapons)):
        if weapons[i] in targets.keys():
            if float(prices[i]) <= targets[weapons[i]]:
                winsound.Beep(Freq,Dur)
                webbrowser.open(market_template_link + weapons[i])
            if ((float(prices[i]) - targets[weapons[i]]) / float(prices[i])) < 0.02:
                qprint(weapons[i] + ' is at ' + prices[i] + ' (only %f more than target).' % ((float(prices[i]) - targets[weapons[i]]) / float(prices[i])))


def create_url(name):
    if len(pack[name]) > 1:
        res = urls[name]                                                             # should adapt at a later point in time
    else:
        res = render_search.replace('item', name)
    for wear in render_wears[name]:
        res += wear
    return res.strip('&')

names = ['guns']

targets = {}
for name in names:
    if name not in pack.keys():                                                      # so that we can deal with 'bayonets' (comprising regular bayos and m9s)
        pack[name] = [name]
    for weapon_name in pack[name]:
        file = open('./dols/' + weapon_name + '.dol', 'r')                                       # cause dolla-dolla :o
        for line in file:
            [weapon, price] = line.strip().split(':')
            price = float(price)
            targets[weapon.replace('â˜…', '★').replace('â„¢', '™')] = price

pl = PageLoader()

while 1:
    for name in names:
        sift_weapons(create_url(name), pl)
