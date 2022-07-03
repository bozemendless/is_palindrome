# Palindrome (迴文)
# 透過Python寫了兩種對回文的判別方式
# 回傳True表示STR為回文字串, 回傳False表示STR非回文字串

# Solution 1

def is_palin(STR):  # STR為字串
    i = 0
    j = len(STR) - 1
    while i < j: # 結束條件
        if STR[i] != STR[j]: #當字串index值為i的字元 不等於 index為j的字元時,回傳false
            return False # 回傳False
        else:  # 當字串index值為i的字元 等於 index為j的字元時
            i += 1 # 透過 i+1 自起始端往下一個字元
            j -= 1 # 透過 j-1 自末端往前一個字元
    return True # 當達成結束條件, 即所有字元比較完成皆相同時, 回傳True
# 當只有一個字元, 或STR為空字串時,  因達成while結束條件, 會回傳True
STR = "TEST"  
print(is_palin(STR)) # False


# Solution 2

def is_palin(STR):  # STR為字串
    if STR != STR[::-1]: # 透過字串切片方式產生和STR反轉字串進行比較
        return False # 當字串STR和反轉後的STR字串不相同時回傳False
    else:
        return True  # 當字串STR和反轉後的STR字串相同時回傳True

STR = "LEVEL"
print(is_palin(STR)) #True

### Solution 1 在自始、末向內夾擊時, 一旦遇到不同字元即回傳False, 不需將整個字串做比較
### Solution 2 需切片反轉整個字串後, 再對新舊兩個字串進行比較