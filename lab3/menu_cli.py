from serializers.json.json_serializer import JsonSerializer
from serializers.xml.xml_serializer import XmlSerializer


while True:
    print('Enter 1 to get from json')
    print('Enter 2 to get from xml')
    print('Enter 3 to convert json to xml')
    print('Enter 4 to convert xml to json')
    print('Enter 5 to exit')

    choice = input("Choose one option: ")

    if choice == '1':
        filename = input('Enter filename: ')
        print(JsonSerializer.load(filename))
    elif choice == '2':
        filename = input("Enter filename: ")
        print(XmlSerializer.load(filename))
    elif choice == '3':
        json_filename = input("Enter json filename: ")
        xml_filename = input('Enter xml filename: ')
        obj = JsonSerializer.load(json_filename)
        XmlSerializer.dump(obj, xml_filename)
    elif choice == '4':
        json_filename = input("Enter json filename: ")
        xml_filename = input('Enter xml filename: ')
        obj = XmlSerializer.load(xml_filename)
        JsonSerializer.dump(obj, json_filename)
    elif choice == '5':
        break
    else:
        print('Incorrect input. Try again.')
