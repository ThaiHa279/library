use libraryschema;
-- Xem lịch sử mượn sách
delimiter $$
create procedure view_history(in user_id int) 
begin
	select * from history where history.user_id = user_id;
end $$
delimiter ;

call view_history(2);


-- Tính phí khi trễ hạn trả sách
DELIMITER //
CREATE FUNCTION Late_fee(user_id INT) 
RETURNS FLOAT
DETERMINISTIC
BEGIN
    DECLARE fee FLOAT;
    SELECT sum((to_days(pay_time) - to_days(borrow_time)-10) * 10000) into fee
    FROM history
    WHERE user_id = history.user_id AND (to_days(pay_time) - to_days(borrow_time) > 10) AND history.status is NULL;
	RETURN fee;
END //
DELIMITER ;


SELECT Late_fee(2);


-- Giao dich muon sach

DELIMITER //
CREATE PROCEDURE MuonSach(in p_user_id int, in p_book_id int)
BEGIN
START TRANSACTION;

-- Giả sử bạn có bảng Books với các cột id, title, author, và status
-- và bảng Borrowers với các cột id, name, và book_id

-- Đầu tiên, chúng ta cần kiểm tra xem sách có sẵn để mượn hay không
	IF EXISTS (SELECT * FROM history WHERE history.book_id = p_book_id AND pay_time is NULL) THEN
		-- Nếu sách không có sẵn, chúng ta in ra thông báo
		SELECT 'The book is not available for borrowing.' AS ErrorMessage;
	ELSE
		-- Thêm người mượn vào bảng history
		INSERT INTO history (user_id, book_id, borrow_time)
		VALUES (p_user_id, p_book_id, date(now()));
	END IF;
COMMIT;
END //
DELIMITER //

CALL MuonSach(2, 10);