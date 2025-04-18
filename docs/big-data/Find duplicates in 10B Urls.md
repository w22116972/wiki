# Find duplicates in 10B Urls

> Cracking the code interview


這裡的題目只有到一千萬個url → 1 url 約 = 100 chars + 1 char = 4 bytes → 一千萬個url=4TB

### Sol: one disk

1. 將所有url分成4000個1GB(共4TB)，把url存進 `{hash(url)%4000}.txt`
2. 把檔案放進記憶體，建立URL的hash table後開始檢查重複

### Sol: multiple machine

把前面第一個步驟存進檔案改成存進machine
