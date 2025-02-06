# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

import re
from typing import Counter

article = "Donald John Trump, born on June 14, 1946, in Queens, New York City, is an American businessman, television personality, and politician who served as the 45th president of the United States from 2017 to 2021. He was the fourth of five children born to Fred Trump, a real estate developer, and Mary Anne MacLeod Trump. Trump attended the Kew-Forest School and later the New York Military Academy. He began his higher education at Fordham University and transferred to the Wharton School of the University of Pennsylvania, graduating in 1968 with a Bachelor of Science in economics. After college, Trump joined his fathers real estate business, The Trump Organization, focusing on residential projects in Brooklyn, Queens, and Staten Island. He later expanded into Manhattan, developing and renovating skyscrapers, hotels, and casinos. Trump gained national recognition by branding his name on various properties and ventures, including the Trump Tower in New York City and the Taj Mahal casino in Atlantic City. He also licensed his name for various products and services, generating significant revenue. In 1988, Trump established the Donald J. Trump Foundation, a private charitable organization. Initially, he contributed personal funds, but after 2006, the foundations donations came primarily from other sources. The foundation supported health and sports-related charities, conservative groups, and organizations hosting events at Trump properties. In 2016, reports emerged alleging legal and ethical violations, including self-dealing and potential tax evasion. The New York attorney generals office investigated, leading to the foundations dissolution in 2018. In 2019, Trump was ordered to pay $2 million to a group of charities for misusing foundation funds. Throughout his career, Trump and his businesses have been involved in numerous legal actions. Between 1991 and 2009, his hotel and casino businesses filed for Chapter 11 bankruptcy protection six times, allowing them to restructure debt while continuing operations. Despite these challenges, Trump maintained a prominent public profile, hosting the reality television show “The Apprentice” from 2004 to 2015. In 2016, Trump entered politics and secured the Republican nomination for president. He won the general election against Democratic nominee Hillary Clinton and assumed office on January 20, 2017. His presidency was marked by significant policy changes, including tax reform, deregulation efforts, and the appointment of conservative judges. He also faced two impeachment trials, both resulting in acquittal. After an unsuccessful re-election bid in 2020, Trump continued to be an influential and controversial figure in American politics."

cleaned_text = re.sub(r'[^\w\s]', '', article).lower()

words = cleaned_text.split()

word_counts = Counter(words)

most_common_words = word_counts.most_common(10)

print("Топ-10 самых частых слов:")
for word, count in most_common_words:
    print(f"{word}: {count}")