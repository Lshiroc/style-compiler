def isDelimeter(char: str):
    DELIMETERS = [' ', '+', '-', '*', '/', ',', ';', '%', '>', '<', '=', '(', ')', '[', ']', '{', '}']
    
    return char in DELIMETERS

def isOperator(char: str):
    OPERATOR = ['+', '-', '*', '/', '>', '<', '=']

    return char in OPERATOR

def isValidIdentifier(str: str):
    INVALID_START_IDENTIFIERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    return str[0] not in INVALID_START_IDENTIFIERS and not isDelimeter(str[0])

def isKeyword(str: str):
    KEYWORDS = ['change', 'upgrade']

    return str in KEYWORDS

def isInteger(str: str):
    return str.isdigit()

def lexicalAnalyzer(input: list[str]):
    left = 0
    right = 0
    length = len(input)

    def isValidIndex():
        return len(input)-1 >= right

    while(right < length and left <= right):
        try:
            if isValidIndex() and not isDelimeter(input[right]):
                right += 1

            if isValidIndex() and isDelimeter(input[right]) and left == right:
                if isOperator(input[right]):
                    print(f'Operator: {input[right]}')
                right += 1
                left = right
            elif isValidIndex() and isDelimeter(input[right]) and left != right or (right == len and left != right):
                substr = input[left:right]

                if isKeyword(substr):
                    print(f'Keyword: {substr}')
                elif isInteger(substr):
                    print(f'Integer: {substr}')
                elif isValidIdentifier(substr):
                    print(f'Identifier: {substr}')
                
                left = right

        except KeyboardInterrupt:
            break

    return

lexicalAnalyzer('> change , ; update 2 <myvaria upgrade;')


