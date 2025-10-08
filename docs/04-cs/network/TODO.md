# TODO

底層到 kernel 層級與 socket/連線 相關設定
sysctl 有哪些與 TCP 連線行為相關的設定？這些參數如何影響 socket 行為？

解釋 SO_REUSEADDR 與 SO_REUSEPORT 的差異與使用情境。

如何在 Linux 上調整 TIME_WAIT 的行為？這些設定可能有什麼副作用？

tcp_tw_reuse 與 tcp_tw_recycle 分別是什麼？為什麼後者在現代 Linux 系統被移除？

如何設定 ephemeral port 範圍？為什麼需要調整它？

Linux kernel 如何追蹤每個 TCP socket 的狀態？對應的檔案或工具有哪些？

使用 netstat 或 ss 怎麼查看 socket 狀態？如何排查大量 CLOSE_WAIT 或 TIME_WAIT？

怎麼設定 TCP keepalive？有哪些 kernel 參數與 socket options 會影響它？

tcp_fin_timeout 是什麼？它與 socket 關閉時的行為有何關聯？

如何調整 accept queue 大小？listen backlog 與 somaxconn 有什麼關係？

應用層使用非阻塞 socket 時，哪些 kernel 層設定會影響其行為？

請解釋 tcp_rmem 和 tcp_wmem 的作用，它們如何影響傳輸效率與延遲？

描述 SYN flood 攻擊與 Linux 上如何調整參數防禦。

在高並發伺服器中，為了避免連線耗盡，kernel 層可以做哪些優化設定？

請解釋 TCP backlog 滿時會發生什麼事？Linux 如何處理尚未 accept 的 socket？