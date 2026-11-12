book_type = input("Enter book type(regular/reference):")
member_status = input("Enter member status(regular/premium/staff):")


def calculate_borrowing_period(book_type, member_status):
    
    book_type = book_type.lower()
    member_status = member_status.lower()
    
    valid_book_types = ["regular", "reference"]
    valid_member_status = ["regular", "permium", "staff"]
    
    if book_type not in valid_book_types:
        print("Invalid book type")
    elif member_status not in valid_member_status:
        print("Invalid member status")
        
    else:
        if book_type == "reference":
            if member_status == "staff":
                print("Borrowing period: 3 days")
            else:
                print("Reference books can only be borrowed by staff members")
        elif book_type == "regular":
            if member_status == "regular":
                print("Borrowing period: 7 days")
            elif member_status == "premium":
                print("Borrowing period: 14 days")
            elif member_status == "staff":
                print("Borrowing period: 30 days ")


calculate_borrowing_period(book_type, member_status)
