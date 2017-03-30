#!/usr/bin/env python
# -*- coding:utf-8 -*-

import mechanize
from bs4 import BeautifulSoup
import urllib
from os import system
import sys


class Translator():
    def argument(self):
        try:
            _to_lang = sys.argv[1]
            _to_lang = str(_to_lang)
            _to_lang = _to_lang.strip()
            _to_lang = _to_lang.lower()
            self.to_language = _to_lang
        except:
            print 'Using : main.py [To Convert Language]'
            sys.exit(0)

    def open_site(self, word):

        _url = "https://translate.google.com.tr/m?hl=tr&sl=auto&tl={0}&ie=UTF-8&prev=_m&q=".format(self.to_language)

        if word == '' or word == ' ':
            print 'Input Value is Incorrect'
            return 'Try Again'

        word = word.replace(" ", "+")
        _url += word

        browser = mechanize.Browser()
        browser.set_handle_robots(False)
        browser.addheaders = [('User-agent',
                               "	Mozilla/5.0 (Windows NT 6.1) \
                                   AppleWebKit/537.36 (KHTML, like Gecko) \
                                   Chrome/41.0.2228.0 Safari/537.36"
                               )]

        browser.open(_url)
        browser.select_form(nr=0)

        html_codes = browser.open(_url).read()
        soup = BeautifulSoup(html_codes, 'html.parser')
        translate_word = soup.find_all('div', attrs={'class': 't0'})

        clear_text = str(translate_word[0])
        clear_text = clear_text[26:len(clear_text)]
        clear_text = clear_text[:-6]

        browser.close()

        return clear_text
        pass  # END

    # Give the command in program and text checker

    def __word_input__(self):

        correct_word = str(raw_input('> '))

        if (correct_word != '-c'):
            if (correct_word != ' '):
                return correct_word
            else:  # user not given a word, be like press enter
                print 'Input Value is Incorrect'

        else:  # command giving
            command_word = str(raw_input('command >>'))
            if command_word == 'clear':
                system('clear')
                self.__word_input__()
            if command_word == 'exit':
                sys.exit(0)

    def translate(self):
        while True:
            self.argument()
            try:
                word = self.__word_input__()
                trans_word = self.open_site(word)
                print ("> {0} \n".format(trans_word))
            except KeyboardInterrupt:
                print '\nGood Bye ...\n'
                sys.exit(0)
        pass  # END
