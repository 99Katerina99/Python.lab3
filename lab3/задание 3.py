
def function_name(search: str, status: bool, *args: object, **kwargs: object) -> object:
    """
      Функция обрабатывает аргументы в зависимости от параметров search и status. Она может выполнить одно из следующих действий:
       Вывести список позиционных аргументов, которые являются целыми числами.
       Объединить все позиционные аргументы в одну строку.
       Сформировать строку, содержащую пары "ключ-значение" всех именованных аргументов.
       Если параметр search принимает значение, отличное от "args" или "kwargs", функция вызывает исключение.

       Параметры:
       search(str): определяет тип обрабатываемых аргументов — позиционные ("args") или именованные ("kwargs").
       Status(bool): влияет на формат вывода позиционных аргументов.
       *args(object): произвольные позиционные аргументы.
       **kwargs(object): произвольные именованные аргументы.

       Возвращаемое значение:
       list[]: если выводятся целочисленные позиционные аргументы.
       Str:если объединяются все позиционные аргументы или выводятся пары "ключ-значение" именованных аргументов.

       Исключения:
       ValueError: вызывается, если search не соответствует допустимым значениям ("args" или "kwargs").

      """

    result: list = []
    result_2: str = ""
    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f"{i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += ("Key: {}, Value: {}; ".format(k, v))
        return result_2
    else:
        raise ValueError("Error for search")