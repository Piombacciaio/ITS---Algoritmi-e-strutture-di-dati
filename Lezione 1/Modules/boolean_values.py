
def main():
    empty_string = ""
    empty_list = []
    empty_dict = {}
    empty_set = set()
    false_int = 0
    false_float = 0.0
    false_value = False
    none_value = None

    print(f"Empty string is {bool(empty_string)}")
    print(f"Empty list is {bool(empty_list)}")
    print(f"Empty dict is {bool(empty_dict)}")
    print(f"Empty set is {bool(empty_set)}")
    print(f"False int is {bool(false_int)}")
    print(f"False float is {bool(false_float)}")
    print(f"False value is {bool(false_value)}")
    print(f"None is {bool(none_value)}")

    non_empty_string = "Hello" # Qualsiasi stringa non vuota è considerata True
    non_empty_list = [1, 2, 3] # Qualsiasi lista non vuota è considerata True
    non_empty_dict = {"key": "value"} # Qualsiasi dizionario non vuoto è considerato True
    non_empty_set = {1, 2, 3} # Qualsiasi set non vuoto è considerato True
    true_int = 1 # Qualsiasi intero diverso da 0 è considerato True
    true_float = 3.14 # Qualsiasi float diverso da 0.0 è considerato True
    true_value = True 
    # Qualsiasi altro oggetto non None è considerato True

    print(f"Non-empty string is {bool(non_empty_string)}")
    print(f"Non-empty list is {bool(non_empty_list)}")
    print(f"Non-empty dict is {bool(non_empty_dict)}")
    print(f"Non-empty set is {bool(non_empty_set)}")
    print(f"Any int (diffrent from 0) is {bool(true_int)}")
    print(f"Any float (diffrent from 0) is {bool(true_float)}")
    print(f"True value is {bool(true_value)}")

if __name__ == "__main__":
    main()