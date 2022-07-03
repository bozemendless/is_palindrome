/* 
Palindrome (迴文)
透過JavaScript中的While迴圈對回文字串進行判斷
*/

// Solution

function isPalindrome(STR) { //有別於Python使用底線命名, 透過駝峰式命名法較符合JS風格
var i = 0;
var j = STR.length - 1;

while (i < j) { // 結束條件
    if (STR[i] != STR[j]) { //當字串index值為i的字元 不等於 index為j的字元時, 回傳false
    return false;
    } else { //當字串index值為i的字元 等於 index為j的字元時
    i++; //透過 i+1 自起始端往下一個字元
    j--; //透過 j-1 自末端往前一個字元
    }
}
return true; //當字串STR和反轉後的STR字串相同時回傳true
}

var STR = 'ABCBA'; 
isPalindrome(STR); // true
