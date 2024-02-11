filename = r""

"""
item start offset (no base): 0xAB8
item end offset (no base): 0xD97?
base offset: 0x2AE
some useful data offsets: (not tested, thank you afterbirth save editor)
"0x4", "Mom Kills",
"0x8", "Broken Rocks",
"0xC", "Broken Tinted Rocks",
"0x10", "Poop Destroyed",
// "0x14",   "???", Blank
"0x18", "Death Cards Used?", //?
"0x1C", "??? (0x1C)", //?
"0x20", "Arcades Visited?", //?
"0x24", "Deaths",
"0x28", "Isaac Kills?",
"0x2C", "Shop Keepers Destroyed",
"0x30", "Satan Kills?",
"0x34", "Shell Game Playcount",
"0x38", "Angel Items Taken?",
"0x3C", "Devil Deals Taken?",
"0x40", "Blood Donations?",
"0x44", "Slots Destroyed",
"0x48", "??? (0x48)",
"0x4C", "Pennies Donated",✅
"0x50", "Eden Tokens",✅
"0x54", "Win Streak", 
"0x58", "Best Streak", ✅
"0x5C", "??? Kills?",
"0x60", "Lamb Kills?",
"0x64", "??? (0x64)",
"0x1A8", "Loss Streak", 
"0x1B0", "Pennies Donated (Greed)", 
"0x254", "Greed Donations (Isaac)",
"0x258", "Greed Donations (Maggy)",
"0x25C", "Greed Donations (Cain)",
"0x260", "Greed Donations (Judas)",
"0x264", "Greed Donations (???)",
"0x268", "Greed Donations (Eve)",
"0x26C", "Greed Donations (Samson)",
"0x270", "Greed Donations (Azazel)",
"0x274", "Greed Donations (Lazarus)",
"0x278", "Greed Donations (Eden)",
"0x27C", "Greed Donations (The Lost)",
"0x280", "Greed Donations (Lilith)",
"0x284", "Greed Donations (Keeper)",
"0x298", "Caves Cleared",
"0x29C", "Basements Cleared",
"0x2A0", "??? (0x2A0)",
"0x2A4", "Depths Cleared"
"""

characters = ["Isaac", "Maggy", "Cain", "Judas", "???", "Eve", "Samson", "Azazel", 
              "Lazarus", "Eden", "The Lost", "Lilith", "Keeper", "Apollyon", "Forgotten", "Bethany",
              "Jacob & Esau", "T Isaac", "T Maggy", "T Cain", "T Judas", "T ???", "T Eve", "T Samson", "T Azazel", 
              "T Lazarus", "T Eden", "T Lost", "T Lilith", "T Keeper", "T Apollyon", "T Forgotten", "T Bethany",
              "T Jacob"]
checklist_order = ["Isaac's Heart", "Isaac", "Satan", "Boss Rush", "Chest", "Dark Room", "Mega Satan", "Hush", "Greed", "Delirium", "Mother", "Beast"]

def rshift(val, n): 
    return val>>n if val >= 0 else (val+0x100000000)>>n

def getSectionOffsets(data):
    ofs = 0x14
    sectData = [-1, -1, -1]
    entryLens = [1,4,4,1,1,1,1,4,4,1]
    sectionOffsets = [0] * 10
    for i in range(len(entryLens)):
        for j in range(3):
            sectData[j] = int.from_bytes(data[ofs:ofs+2], 'little', signed=False)
            ofs += 4
        if sectionOffsets[i] == 0:
            sectionOffsets[i] = ofs
        for j in range(sectData[2]):
            ofs += entryLens[i]
    return sectionOffsets

def updateCheckListUnlocks(data, char_index, new_checklist_data):
    if char_index == 14:
        clu_ofs = getSectionOffsets(data)[1] + 0x32C
        for i in range(len(new_checklist_data)):
            current_ofs = clu_ofs + i * 4
            data = alterInt(data, current_ofs, new_checklist_data[i])
            if i == 8:
                clu_ofs += 0x4
            if i == 9:
                clu_ofs += 0x37C
            if i == 10:
                clu_ofs += 0x84
    elif char_index > 14:
        clu_ofs = getSectionOffsets(data)[1] + 0x31C
        for i in range(len(new_checklist_data)):
            current_ofs = clu_ofs + char_index * 4 + i * 19 * 4
            data = alterInt(data, current_ofs, new_checklist_data[i])
            if i == 8:
                clu_ofs += 0x4C
            if i == 9:
                clu_ofs += 0x3C
            if i == 10:
                clu_ofs += 0x3C
    else:
        clu_ofs = getSectionOffsets(data)[1] + 0x6C
        for i in range(len(new_checklist_data)):
            current_ofs = clu_ofs + char_index * 4 + i * 14 * 4
            data = alterInt(data, current_ofs, new_checklist_data[i])
            if i == 5:
                clu_ofs += 0x14
            if i == 8:
                clu_ofs += 0x3C
            if i == 9:
                clu_ofs += 0x3B0
            if i == 10:
                clu_ofs += 0x50
    return data

def getChecklistUnlocks(data, char_index):
    checklist_data = []
    if char_index == 14:
        clu_ofs = getSectionOffsets(data)[1] + 0x32C
        for i in range(12):
            current_ofs = clu_ofs + i * 4
            checklist_data.append(getInt(data, current_ofs))
            if i == 8:
                clu_ofs += 0x4
            if i == 9:
                clu_ofs += 0x37C
            if i == 10:
                clu_ofs += 0x84
    elif char_index > 14:
        clu_ofs = getSectionOffsets(data)[1] + 0x31C
        for i in range(12):
            current_ofs = clu_ofs + char_index * 4 + i * 19 * 4
            checklist_data.append(getInt(data, current_ofs))
            if i == 8:
                clu_ofs += 0x4C
            if i == 9:
                clu_ofs += 0x3C
            if i == 10:
                clu_ofs += 0x3C
    else:
        clu_ofs = getSectionOffsets(data)[1] + 0x6C
        for i in range(12):
            current_ofs = clu_ofs + char_index * 4 + i * 14 * 4
            checklist_data.append(getInt(data, current_ofs))
            if i == 5:
                clu_ofs += 0x14
            if i == 8:
                clu_ofs += 0x3C
            if i == 9:
                clu_ofs += 0x3B0
            if i == 10:
                clu_ofs += 0x50
    return checklist_data

def getItems(data):
    item_data = []
    offs = getSectionOffsets(data)[3]
    for i in range(1, 733):
        item_data.append(getInt(data, offs+i, num_bytes=1))
    return item_data

def getChallenges(data):
    challenge_data = []
    offs = getSectionOffsets(data)[6]
    for i in range(1, 46):
        challenge_data.append(getInt(data, offs+i, num_bytes=1))
    return challenge_data

def getSecrets(data):
    secrets_data = []
    offs = getSectionOffsets(data)[0]
    for i in range(1, 638):
        secrets_data.append(getInt(data, offs+i, num_bytes=1))
    return secrets_data


def calcAfterbirthChecksum(data, ofs, length):
    CrcTable = [
        0x00000000, 0x09073096, 0x120E612C, 0x1B0951BA, 0xFF6DC419, 0xF66AF48F, 0xED63A535, 0xE46495A3, 
        0xFEDB8832, 0xF7DCB8A4, 0xECD5E91E, 0xE5D2D988, 0x01B64C2B, 0x08B17CBD, 0x13B82D07, 0x1ABF1D91, 
        0xFDB71064, 0xF4B020F2, 0xEFB97148, 0xE6BE41DE, 0x02DAD47D, 0x0BDDE4EB, 0x10D4B551, 0x19D385C7, 
        0x036C9856, 0x0A6BA8C0, 0x1162F97A, 0x1865C9EC, 0xFC015C4F, 0xF5066CD9, 0xEE0F3D63, 0xE7080DF5, 
        0xFB6E20C8, 0xF269105E, 0xE96041E4, 0xE0677172, 0x0403E4D1, 0x0D04D447, 0x160D85FD, 0x1F0AB56B, 
        0x05B5A8FA, 0x0CB2986C, 0x17BBC9D6, 0x1EBCF940, 0xFAD86CE3, 0xF3DF5C75, 0xE8D60DCF, 0xE1D13D59, 
        0x06D930AC, 0x0FDE003A, 0x14D75180, 0x1DD06116, 0xF9B4F4B5, 0xF0B3C423, 0xEBBA9599, 0xE2BDA50F, 
        0xF802B89E, 0xF1058808, 0xEA0CD9B2, 0xE30BE924, 0x076F7C87, 0x0E684C11, 0x15611DAB, 0x1C662D3D, 
        0xF6DC4190, 0xFFDB7106, 0xE4D220BC, 0xEDD5102A, 0x09B18589, 0x00B6B51F, 0x1BBFE4A5, 0x12B8D433, 
        0x0807C9A2, 0x0100F934, 0x1A09A88E, 0x130E9818, 0xF76A0DBB, 0xFE6D3D2D, 0xE5646C97, 0xEC635C01,
        0x0B6B51F4, 0x026C6162, 0x196530D8, 0x1062004E, 0xF40695ED, 0xFD01A57B, 0xE608F4C1, 0xEF0FC457, 
        0xF5B0D9C6, 0xFCB7E950, 0xE7BEB8EA, 0xEEB9887C, 0x0ADD1DDF, 0x03DA2D49, 0x18D37CF3, 0x11D44C65, 
        0x0DB26158, 0x04B551CE, 0x1FBC0074, 0x16BB30E2, 0xF2DFA541, 0xFBD895D7, 0xE0D1C46D, 0xE9D6F4FB, 
        0xF369E96A, 0xFA6ED9FC, 0xE1678846, 0xE860B8D0, 0x0C042D73, 0x05031DE5, 0x1E0A4C5F, 0x170D7CC9, 
        0xF005713C, 0xF90241AA, 0xE20B1010, 0xEB0C2086, 0x0F68B525, 0x066F85B3, 0x1D66D409, 0x1461E49F, 
        0x0EDEF90E, 0x07D9C998, 0x1CD09822, 0x15D7A8B4, 0xF1B33D17, 0xF8B40D81, 0xE3BD5C3B, 0xEABA6CAD, 
        0xEDB88320, 0xE4BFB3B6, 0xFFB6E20C, 0xF6B1D29A, 0x12D54739, 0x1BD277AF, 0x00DB2615, 0x09DC1683, 
        0x13630B12, 0x1A643B84, 0x016D6A3E, 0x086A5AA8, 0xEC0ECF0B, 0xE509FF9D, 0xFE00AE27, 0xF7079EB1, 
        0x100F9344, 0x1908A3D2, 0x0201F268, 0x0B06C2FE, 0xEF62575D, 0xE66567CB, 0xFD6C3671, 0xF46B06E7, 
        0xEED41B76, 0xE7D32BE0, 0xFCDA7A5A, 0xF5DD4ACC, 0x11B9DF6F, 0x18BEEFF9, 0x03B7BE43, 0x0AB08ED5, 
        0x16D6A3E8, 0x1FD1937E, 0x04D8C2C4, 0x0DDFF252, 0xE9BB67F1, 0xE0BC5767, 0xFBB506DD, 0xF2B2364B, 
        0xE80D2BDA, 0xE10A1B4C, 0xFA034AF6, 0xF3047A60, 0x1760EFC3, 0x1E67DF55, 0x056E8EEF, 0x0C69BE79, 
        0xEB61B38C, 0xE266831A, 0xF96FD2A0, 0xF068E236, 0x140C7795, 0x1D0B4703, 0x060216B9, 0x0F05262F, 
        0x15BA3BBE, 0x1CBD0B28, 0x07B45A92, 0x0EB36A04, 0xEAD7FFA7, 0xE3D0CF31, 0xF8D99E8B, 0xF1DEAE1D, 
        0x1B64C2B0, 0x1263F226, 0x096AA39C, 0x006D930A, 0xE40906A9, 0xED0E363F, 0xF6076785, 0xFF005713, 
        0xE5BF4A82, 0xECB87A14, 0xF7B12BAE, 0xFEB61B38, 0x1AD28E9B, 0x13D5BE0D, 0x08DCEFB7, 0x01DBDF21, 
        0xE6D3D2D4, 0xEFD4E242, 0xF4DDB3F8, 0xFDDA836E, 0x19BE16CD, 0x10B9265B, 0x0BB077E1, 0x02B74777, 
        0x18085AE6, 0x110F6A70, 0x0A063BCA, 0x03010B5C, 0xE7659EFF, 0xEE62AE69, 0xF56BFFD3, 0xFC6CCF45, 
        0xE00AE278, 0xE90DD2EE, 0xF2048354, 0xFB03B3C2, 0x1F672661, 0x166016F7, 0x0D69474D, 0x046E77DB, 
        0x1ED16A4A, 0x17D65ADC, 0x0CDF0B66, 0x05D83BF0, 0xE1BCAE53, 0xE8BB9EC5, 0xF3B2CF7F, 0xFAB5FFE9, 
        0x1DBDF21C, 0x14BAC28A, 0x0FB39330, 0x06B4A3A6, 0xE2D03605, 0xEBD70693, 0xF0DE5729, 0xF9D967BF, 
        0xE3667A2E, 0xEA614AB8, 0xF1681B02, 0xF86F2B94, 0x1C0BBE37, 0x150C8EA1, 0x0E05DF1B, 0x0702EF8D
    ]
    checksum = 0xFEDCBA76
    checksum = ~checksum

    for i in range(ofs, ofs+length):
        checksum = CrcTable[((checksum & 0xFF)) ^ data[i]] ^ (rshift(checksum, 8))

    return ~checksum + 2 ** 32

def alterSecret(data, achievement, unlock=True):
    offs = getSectionOffsets(data)[0]
    new_data = b'\x00'
    if unlock:
        new_data = b'\x01'
    new_data = data[:offs + achievement] + new_data + data[offs + achievement + 1:] 
    return new_data

def alterChallenge(data, challenge_index, unlock=True):
    if unlock:
        val = 1
    else:
        val = 0
    return alterInt(data, getSectionOffsets(data)[6]+challenge_index, val, num_bytes=1)

def alterItem(data, item_index, unlock=True):
    if unlock:
        val = 1
    else:
        val = 0
    return alterInt(data, getSectionOffsets(data)[3]+item_index, val, num_bytes=1)

def alterInt(data, offset, new_val, debug=False, num_bytes=2):
    if debug:
        print(f"current value: {int.from_bytes(data[offset:offset+num_bytes], 'little')}")
        print(f"new value: {new_val}")
    return data[:offset] + new_val.to_bytes(num_bytes, 'little', signed=True) + data[offset + num_bytes:]

def getInt(data, offset, debug=False, num_bytes=2):
    if debug: print(f"current value: {int.from_bytes(data[offset:offset+num_bytes], 'little', signed=False)}")
    return int.from_bytes(data[offset:offset+num_bytes], 'little')

def updateSecrets(data, secret_list):
    for i in range(1, 638):
        data = alterSecret(data, i, False)
    for i in secret_list:
        data = alterSecret(data, int(i))
    return data

def updateChallenges(data, challenge_list):
    for i in range(1, 46):
        data = alterChallenge(data, i, False)
    for i in challenge_list:
        data = alterChallenge(data, int(i), True)
    return data

def updateItems(data, item_list):
    for i in range(1, 733):
        if i in [43,59,61,235,587,613,620,630,648,656,662,666,718]:
            continue
        data = alterItem(data, i, False)
    for i in item_list:
        data = alterItem(data, int(i))
    return data

def updateChecksum(data):
    offset = 0x10
    length = len(data) - offset - 4
    return data[:offset + length] + calcAfterbirthChecksum(data, offset, length).to_bytes(5, 'little', signed=True)[:4]

# updateWinStreak: alterInt(data, getSectionOffsets(data)[1] + 0x4 + 0x54, 30)
# updateGreedMachine: alterInt(data, getSectionOffsets(data)[1] + 0x4 + 0x54, 30)
# updateDonationMachine: alterInt(data, getSectionOffsets(data)[1] + 0x4 + 0x1B0, 30)

if __name__ == "__main__":
    offset = 0x10
    with open(filename, "rb") as file:
        data = file.read()
        length = len(data) - offset - 4
        checksum = calcAfterbirthChecksum(data, offset, length).to_bytes(5, 'little', signed=True)[:4]
        print(checksum)
        old_checksum = data[offset + length:]    
    # below are some examples on how to use this script that aren't covered in the gui implementation.
    
    # update a character's post-it: 0 is not completed, 1 is completed on normal, 2 is completed on hard. order is in checklist_order.
    data = updateCheckListUnlocks(data, characters.index("Maggie"), [0,0,1,0,2,1,0,1,0,0,0,2])
    # enable secrets for online beta NOTE: THIS HAS NOT BEEN TESTED ON THE ONLINE BETA!!! USE AT OWN RISK!!!
    for i in range(638, 641):
        data = alterSecret(data, i)


    with open(filename, 'wb') as file:
        print(calcAfterbirthChecksum(data, offset, length).to_bytes(5, 'little', signed=True)[:4])
        file.write(updateChecksum(data))