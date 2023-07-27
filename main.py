from mcc import MCC

def main():
    mcc=MCC()
    while True:
        print("*********WELCOME**********")
        print()
        print("Press 1 to Insert new User")
        print("Press 2 to display all User")
        print("Press 3 to display Single User")
        print("Press 4 to delete User")
        print("Press 5 to Update User")
        print("Press 6 to exit Program")
        print()

        try:
            choice=int(input())
            if choice==1:
                id=int(input("Enter user Id "))
                name=input("Enter user Name ")
                phone=input("Enter user Phone ")
                mcc.insert_user(id,name,phone)
            elif choice == 2:
                mcc.fetch_all()
            elif choice == 3:
                id=int(input("Enter User Id"))
                mcc.fetch_one(id)
            elif choice == 4:
                id=int(input("Enter User Id"))
                mcc.delete_user(id)
            elif choice == 5:
                id=int(input("Enter user Id "))
                name=input("Enter new user Name ")
                phone=input("Enter new user Phone ")
                mcc.update_user(id,name,phone)
            elif choice== 6:
                break
            else:
                print("Enter Above Number Only")
        except:
            print("Enter A Valid Option")

if __name__=="__main__":
    main()