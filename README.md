#Game: Chicken Invaders

- Đây là một game bắn súng cố định, người chơi điều khiển một con tàu vũ trụ đơn độc di chuyển theo chiều ngang đến cuối màn hình 
và bắn vào bầy gà xâm lăng đến từ ngoài trái đất .Những con gà địch thủ sẽ thả vũ khí, chính là những quả trứng. 
Khi gà bị đánh bại, chúng sẽ thả những đùi gà, người chơi có thể thu thập để kiếm thêm một quả tên lửa, 
một loại vũ khí đặc biệt dùng đề qua màn. Và vào cuối màn, người chơi sẽ chiến đấu với một con trùm, đánh bại nó để chiến thắng game. 
Đây là một trò chơi vô tận, chỉ cho đến khi người chơi mất hết mạng, đồng nghĩa với kết thúc. 

-Hướng dẫn game:
   '-> '  để di chuyển qua trái
   '<-'  để di chuyển qua phải
   'key_down'  để di chuyển xuống
   'key_up'  để di chuyển lên
   'space' để  tàu vũ trụ nhả đạn
   'r' để bắn tên lửa 

- Các sự kiện game, tính năng game:
    + Map 1:  Tiêu diệt bầy gà 
    + Map 2: Tiêu diệt boss
    + Tính điểm đạt được
    + Hiển thị số lượng tên lửa
    + Hiển thị đùi gà ( 10 đùi gà = 1 tên lửa )
    + Hiển thị máu của tàu vũ trụ
    + Hiển thị máu của boss
    + Hiện thị màn hình game_over : khi lose hoặc win game

- Tính năng của tàu vũ trụ:
   + Nhả đạn
   + Bắn tên lửa
   + Sử dụng khiên ( bất tử )
   + Ăn đùi gà
 
- Tính năng của bầy gà:
   + đẻ trứng: ( trừ % máu tàu vũ trụ nếu trúng )
   + tia sáng phòng thủ ( không thể bị tấn công - trừ khi tên lửa )
   + khi chết random tỉ lệ xuất hiện đùi gà
   + random thời gian hồi sinh

- Tính năng của boss:
   + nhả đạn: ( trừ % máu tàu vũ trụ nếu trúng )
   + trừ máu : nếu bị tàu vũ trụ bắn trúng
   + khiên bảo vệ: (không thể bị tấn công - trừ khi tên lửa)
   + khi boss chết => Vụ nổ và kết thúc game

- Luật chơi:
	+ gà con 1 viên đạn sẽ bị tiêu diệt ( có thể cài đặt số lượng gà )
	+ tăng 10 điểm khi tiêu diệt 1 chú gà
	+ xuất hiện lại sau 1 khoảng thời gian
	+ khi tiêu diệt đủ 100 chú gà: Boss xuất hiện và đàn gà con biến mất
	+ Boss hết máu => boss died
        + Tiêu diệt boss để win game
	+ 10 đùi gà đổi lấy 1 tên lửa
	+ tiêu diệt 10 chú gà thưởng 7s sử dụng khiên
