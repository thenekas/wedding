#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# config.js
config_content = """/* Меняйте данные приглашения только в этом файле */
window.WEDDING_CONFIG = {
  groom: "Атриё",
  bride: "Элина",
  date: "2026-11-28T14:00:00+03:00",
  time: "14:00",
  venue: "Банкет холл «Асаки»",
  region: "Москва",
  address: "улица Юных Ленинцев, 12",
  mapLink: "https://yandex.ru/maps/?text=%D0%91%D0%B0%D0%BD%D0%BA%D0%B5%D1%82%20%D1%85%D0%BE%D0%BB%D0%BB%20%D0%90%D1%81%D0%B0%D0%BA%D0%B8%2C%20%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0%20%D0%AE%D0%BD%D1%8B%D1%85%20%D0%9B%D0%B5%D0%BD%D0%B8%D0%BD%D1%86%D0%B5%D0%B2%2C%2012",
  googleScriptUrl: "https://script.google.com/macros/s/AKfycbyG68_3fcdj3_pUD1V-Vh8mU3ILk_boHBON3cDoyNUoBmKwvGUkguUpJXUdM59y66_d2w/exec"
};
"""

with open('config.js', 'w', encoding='utf-8') as f:
    f.write(config_content)
print("✓ config.js обновлен")

# index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('Бахтиёр', 'Атриё')
html = html.replace('Савсан', 'Элина')
html = html.replace('24.10.2026', '28.11.2026')
html = html.replace('октябрь', 'ноябрь')
html = html.replace('nekqadamovsino-spec.github.io/wedding-bakhtiyorsavsan', 'thenekas.github.io/wedding')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("✓ index.html обновлен")

# CNAME
with open('CNAME', 'w', encoding='utf-8') as f:
    f.write('atriyo-elina.ru')
print("✓ CNAME создан")

print("\n✅ Все файлы обновлены!")
