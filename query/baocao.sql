use libraryschema;

create table borrow_book(
	id_borrow int auto_increment,
    id_book varchar(100),
    id_user int,
    borrow_day date,
    pay_day date,
    state boolean,
    primary key(id_borrow),
    foreign key(id_book) references book(`Book ID`),
    foreign key(id_user) references user(id)
);

drop table borrow_book;

insert into borrow_book(id_book, id_user, borrow_day, pay_day, state) 
values('10.1163/j.ctt1w76trp', 1, '2023-11-06', '2023-11-07', 0);
insert into borrow_book(id_book, id_user, borrow_day, pay_day, state) 
values('10.1163/j.ctt1w76ts6', 4, '2023-11-06', '2023-11-07', 0);
----------------------------------------------------------------------------------------
-- Thêm user
delimiter $$
create procedure pr_insert_user(in uname varchar(255), in pass varchar(255))
begin
	insert into user(username, password) values(uname, pass);
end $$
delimiter ;

call pr_insert_user('Nguyen Quoc Khai','khai123');
------------------------------------------------------------------------------------------------------
-- Xem DS mượn
delimiter $$
create procedure pr_view_borrow() 
begin
	select * from borrow_book;
end $$
delimiter ;
----------------------------------------------------------------------------------------------
-- Cập nhật DS mượn
delimiter $$
create procedure pr_updateBorrow(in loaiChinhSua varchar(25), in idBorrow int, in idbook varchar(100), in iduser int, in borrowDay date, 
								in payDay date, in state boolean)
begin
	if loaiChinhSua = 'id_book' then
		update borrow_book set id_book = idbook
        where id_borrow = idBorrow;
	elseif loaiChinhSua = 'id_user' then
		update borrow_book set id_user = iduser
        where id_borrow = idBorrow;
	elseif loaiChinhSua = 'borrow_day' then
		update borrow_book set borrow_day = borrowDay
        where id_borrow = idBorrow;
	elseif loaiChinhSua = 'pay_day' then
		update borrow_book set pay_day = payDay
        where id_borrow = idBorrow;
	elseif loaiChinhSua = 'state' then
		update borrow_book as bb set bb.state = state
        where id_borrow = idBorrow;
	elseif loaiChinhSua = 'overdue_fee' then
		update borrow_book set overdue_fee = overdueFee
        where id_borrow = idBorrow;
	end if;
end $$
delimiter ;

call pr_updateBorrow('pay_day', 1, null, null, null, '2023-10-10', null);
call pr_updateBorrow('borrow_day', 2, null, null, '2023-11-5', null, null);
--------------------------------------------------------------------------------------------------------
-- Tính phí khi trễ hạn trả sách
delimiter $$
create function overdueFee(idBorrow int)
returns float
deterministic
begin
    declare nTra date;
    
    select pay_day into nTra from borrow_book
    where id_borrow = idBorrow;
    
    -- Với phí là 10.000/Ngày
    return ((date(now()) - nTra)*10000);
end $$
delimiter ;

select overdueFee(1);