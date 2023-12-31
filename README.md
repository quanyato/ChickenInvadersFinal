# PYTHON Game Design Document

## Game Overview

- **Title: Bắn gà huyền thoại**
- **Genre: SHMUP**
- **Platform: Windows**

## Game Concept

- **Summary:** Trò chơi là cuộc chiến giữa một phi thuyền đơn độc và một chủng tộc gà đến từ không gian, sở hữu các công nghệ tiên tiến, những sinh vật có ý định chinh phục Trái đất.

## Gameplay

- **Mechanics:** Bắn và né.
    - Cơ chế tính điểm: Thu nhặt những đùi gà rơi ra sau khi tiêu diệt gà. Sau khi tích đủ một lượng đùi gà nhất định sẽ tự động được quy đổi sang tên lửa, một vũ khí siêu mạnh.
    - Cơ chế sinh mệnh: Người chơi có 100% điểm sinh mệnh, mỗi lần bị va chạm hoặc bị tấn công trúng sẽ bị trừ dần. Game over khi điểm sinh mệnh về 0 và reset tiến trình game.
- **Objectives:** Tiêu diệt toàn bộ gà trong màn chơi.
- **Controls:** Di chuyển phi thuyền bằng các phím mũi tên hoặc ASWD. Tấn công thường bằng phím space. Tấn công đặc biệt bằng phím R.

- **Platforms:** Windows
- **Programming Languages:** Python
- **Engine:** Pygame