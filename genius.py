import random
from blockchainJson import *

WalletNames = ["ERAGON_1997", "lifes_a_mystery", "aLmOniaCo", "Back2Papa22", "Synnernight", "CMJprime", "FugDog13", "BananaXXBeast", "DerLeon12", "WAPOO2014", "loluk25", "brqh", "MightYBurgeR", "Guillaumefeu", "DMRunner", "Bigkye", "swaglord_fxx", "subliminality", "_TheMerchant_", "Contrabants", "cOoKiEcAt000", "Tams_Show", "KronoVolt", "CarmenCreeper", "tcmage", "dani_wall", "BOCKIZZ", "PJstrong11", "SummtinSpecial", "NovaFan02", "Robertsihr", "Fuh_King", "Calvin813", "Foursam",
               "Daumpot", "g5326539", "Xbrogamer", "Ziziko", "Garri23", "Xxmrradicalxx", "AxelTheEagle", "Landyman01", "yossi2005", "Pipefitter597", "metrolink", "Its_a_spy123", "ProxyDeath", "Bbob5366", "Seprulta", "KitoKanabi", "CrimsonChaos", "Josinator101", "Boogwaaana", "Supersam8778", "Yettemaster77", "Zachariah1456", "Kaktuslecker", "Zakriah", "Sojudaddy", "Chaotic_Chroma", "Hazzakee", "theXpunisher", "jMorgan1010", "Jibtron", "Blutflagg", "Imrane_45", "Zomboney", "Ewanminion", "matLgr", ]

WALLETS = []
for name in WalletNames:
    WALLETS.append(godWallet(name))


def getRandomWallet():
    return WALLETS[random.randint(0, len(WALLETS)-1)]


blocks = 442
numTrans = 20

bc = Blockchain()

for count in range(blocks):
    amount = 0
    randint1 = random.randint(1, 4)
    if randint1 <= 3:
        amount = random.randint(2, 6)
    else:
        amount = random.randint(7, 15)
    for _ in range(amount):
        amount = 0
        randint1 = random.randint(1, 15)
        if randint1 <= 5:
            amount = random.randint(1, 20)
        elif randint1 <= 9:
            amount = random.randint(21, 40)
        elif randint1 <= 12:
            amount = random.randint(41, 60)
        elif randint1 <= 14:
            amount = random.randint(61, 80)
        else:
            amount = random.randint(81, 100)

        bc.addTransaction(Transaction(
            getRandomWallet(), getRandomWallet(), amount))
    getRandomWallet().mineBlock(bc)
    print(count)
