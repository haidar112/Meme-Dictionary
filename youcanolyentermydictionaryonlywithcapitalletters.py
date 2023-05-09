meme_dict = {'CRINGE':'sesuatu yang alay atau menjijikan',
             'LOL':'ketawa yang sangat kencang',
             'ROFL':'Tanggapan terhadap lelucon',
             'SHEESH':'sedikit ketidaksetujuan',
             'CREEPY':'menakutkan, tidak menyenangkan',
             'AGGRO':'untuk menjadi agresif/marah'
            }

word = input('Ketik kata yang ingin dicari tahu:')

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('Kata yang dicari tidak tersedia')
