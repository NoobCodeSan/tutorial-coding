zakaz_1 =100
price_borsh = 2.75
porsia_1 = zakaz_1 // price_borsh
sdacha_1 = zakaz_1 % price_borsh
sdacha_1 = round(sdacha_1, 2)
print('порций борща ' + str (porsia_1))
print('чай с борща ' + str(sdacha_1))
zakaz_2 = 100
price_palemans = 2.19
porsia_2 = zakaz_2 // price_palemans
sdacha_2 = zakaz_2 % price_palemans
sdacha_2 = round(sdacha_2, 2)
print('порций с пельмешей ' + str(porsia_2))
print('чай с пельмешей ' + str(sdacha_2))
zakaz_3 = 50
price_compote = 1.24
porsia_3 = zakaz_3 // price_compote
sdacha_3 = zakaz_3 % price_compote
sdacha_3 = round(sdacha_3, 2)
print('порций с капота ' + str(porsia_3))
print('чай с кампота ' + str(sdacha_3))
tea_money = sdacha_1 + sdacha_2 + sdacha_3
print('всего чаевых ' + str(tea_money))