
# # 类型注解
# # 变量定义--无指定类型 --> 类型推断
# a1 = 666
# sc1 = 6.6
# ho1 = "C++"
# flag1 = True
# pic1 = None
#
# name1 = ["A", "B", "C"]
# phone1 = {"234352555"}
# opt1 = {"count": 1, "total": 10}
# good1 = ("手机", 9999, 1)
#
# # 变量定义--指定类型注解
# a2: int = 666
# sc2: float = 6.6
# ho2: str = "C++"
# flag2: bool = True
# pic2: None = None
#
# name2: list[str] = ["A", "B", "C"]
# phone2: set[str] = {"234352555"}
# opt2: dict[str, int] = {"count": 1, "total": 10}
# good2: tuple[str, int, int] = ("手机", 9999, 1)
#
# name2.append("A")


#函数类型注解
def cir_area_len(r:float) ->tuple[float,float]:
    return round(3.14*r**2,1),round(2*3.14*r,1)


al = cir_area_len(10)
print(al)
