from abc import ABC,abstractmethod
import json

#书籍类
class Book:
    def __init__(self,id, title, author, total):
        self.id = id            #书籍ID
        self.title = title      #书籍标题
        self.author = author    #书籍作者
        self.total = total      #书籍总数
        self.__available = total  #书籍可用数量


    def borrow_book(self):  #借阅书籍
        if self.__available > 0 :
            self.__available -= 1
            return True
        return False

    def return_book(self):  #归还书籍
        self.__available += 1


    def get_available(self):  #获取可用数量
        return self.__available

#抽象类:不能直接实例化,只能被继承类实例化
#       作用:规定子必须要实现哪些方法,强制子类必须遵守统一的代码规范
#python中的抽象类,需要继承abc模块中的ABC类 --->ABC:Abstract Base Class
#会员类
class Member(ABC):
    def __init__(self,card_no,password,name):
        self.card_no = card_no  #会员卡号
        self.__password = password  #会员密码
        self.name = name  #会员姓名
        self.__borrowed_books = []  #会员借阅的书籍列表


    def borrowed_book(self,book: Book):  #借阅书籍
        # 判断当前会员借阅数量是否达到最大限制
        if len(self.__borrowed_books) >= self.get_max_books():
            print("借阅失败,您的借阅数量已达最大限制!")
            return False

        # 判断书籍是否可借阅
        if book.borrow_book():
            self.__borrowed_books.append(book)
            return True
        else:
            print(f"{self.name}借阅{book.title}失败,书籍已借阅完!")
            return False



    def return_book(self,book: Book):  #归还书籍
        # 判断当前会员是否借阅了该书籍
        if book in self.__borrowed_books:
            # 还书
            book.return_book()
            self.__borrowed_books.remove(book)
        else:
            print(f"归还失败,您未借阅{book.title}!")


    def get_password(self):
        return  self.__password

    def get_borrowed_books(self):
        return self.__borrowed_books

    # 获取会员最大借阅数量(需在子类种实现)
    @abstractmethod
    def get_max_books(self) -> int:
        pass


# 普通会员类
class NormalMember(Member):
    def get_max_books(self) -> int:
        return 3

# VIP会员类
class VIPMember(Member):
    def __init__(self,card_no,password,name,vip_level):
        super().__init__(card_no,password,name)
        self.vip_level = vip_level     #会员等级

    def get_max_books(self) -> int:
        return 6 + self.vip_level


# 图书馆管理系统
class LibrarySystem:
    def __init__(self):
        self.books = { }  # 书籍字典-->key:书籍ID,value:书籍对象{"AI001":Book对象}
        self.members = { }  # 会员字典-->key:会员ID,value:会员对象{"1001":Member对象}
        self.current_member: Member | None = None # 当前登录会员
        # 加载数据(书籍,会员)
        self.load_books_data()
        self.load_members_data()


    def load_books_data(self):
        # 加载data-图书管理系统/book.json文件
        with open("data-图书管理系统/book.json","r",encoding="utf-8") as f:
            books_data = json.load(f)
            for book in books_data:
                self.books[book["id"]] = Book(book["id"],book["title"],book["author"],book["total"])
        print("书籍数据加载完成!")

    def load_members_data(self):
        # 加载data-图书管理系统/members.json文件
        with open("data-图书管理系统/members.json","r",encoding="utf-8") as f:
            members_data = json.load(f)
            for member in members_data:
                if member["card_no"].startswith("M"):
                    self.members[member["card_no"]] = NormalMember(member["card_no"],member["password"],member["name"])
                else:
                    self.members[member["card_no"]] = VIPMember(member["card_no"],member["password"],member["name"],member["vip_level"])
        print("会员数据加载完成!")


    def login(self):   #登录
        while True:
            print("\n登录")
            card_no = input("请输入会员卡号:")
            # 判断会员卡号是否存在
            if card_no not in self.members:
                print("会员卡号不存在!")
                continue
            password = input("请输入会员密码:")



            # 判断密码是否正确
            member = self.members[card_no]
            if member.get_password() == password:
                print(f"{member.name}登录成功!")
                self.current_member = member
                return True

            else:
                print("密码错误!")
                continue

    def borrow_book(self): #借阅图书
        #1.展示当前图书馆的图书列表
        for book in self.books.values():
            print(f"编号:{book.id}, 书名:{book.title}, 作者:{book.author}, 总数量:{book.total}, 可用:{book.get_available()} ")

        #2.获取用户输入的图书编号,执行借书操作
        book_id = input("请输入要借阅的图书编号:")
        if book_id in self.books:
            book = self.books[book_id]
            if self.current_member.borrowed_book(book):
                print(f"{self.current_member.name}成功借阅{book.title}")
        else:
            print(f"借阅失败,书籍{book_id}不存在!")


    def return_book(self): #归还图书
        #1.展示当前会员的借阅记录
        borrowed_books = self.current_member.get_borrowed_books()
        print("已经借阅的图书列表:")
        for book in borrowed_books:
            print(f"编号:{book.id}, 书名:{book.title}")

        #2.获取用户输入的图书编号,执行还书操作
        book_id = input("请输入要归还的图书编号:").strip()
        book = self.books.get(book_id)
        if book is None or book not in borrowed_books:
            print(f"归还失败,书籍{book_id}不存在或您未借阅{book.title}!")
            return
        else:
            self.current_member.return_book(book)
            print(f"{self.current_member.name}成功归还{book.title}")




    def query_borrowed_books(self): #查询借阅记录
        #1.展示当前会员的借阅记录
        borrowed_books = self.current_member.get_borrowed_books()
        if len(borrowed_books) > 0:
            print("已经借阅的图书列表:")
            for book in borrowed_books:
                print(f"编号:{book.id}, 书名:{book.title}")
        else:
            print("您没有借阅任何图书!")


    def run(self):
        if self.login():
            while True:
                print("1.借阅图书")
                print("2.归还图书")
                print("3.查询借阅记录")
                print("4.退出系统")

                choice = input("请输入您的选择(1-4):")
                match choice:
                    case "1":
                        self.borrow_book()
                    case "2":
                        self.return_book()
                    case "3":
                        self.query_borrowed_books()
                    case "4":
                        print("谢谢使用!")
                        break
                    case _:
                        print("输入错误,请重新输入!")


if __name__ == '__main__':
    library = LibrarySystem()
    library.run()



