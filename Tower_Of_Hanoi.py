def TOH(numbers, start, auxilary,end):
    if numbers == 1:
        print("move disk 1 from rod {} to rod{}".format(start,end))
        return
    TOH(numbers -1,start,end, auxilary)
    print("move disk{} from rod {} to rod {}".format(numbers,start,end))
    TOH(numbers -1, auxilary, start,end)

disc = 5
TOH(disc,"Start","Auxilary","End")
    