class PixelPlotter:
    def __init__(self):
        self.image_array = []
    
    # this function reads the file and converts it to a python array
    def set_image_array(self):
        with open("image_array.txt", "r") as f:
            for i, r in enumerate(f.readlines()):
                # removes any spaces or newline characters
                self.image_array.append([value for value in r if value in ("0", "1")])


            #for i in self.image_array:
            #    print(i, "\n")
            #tmp = [line.split(" ") for line in f.readlines()]
            #newList = [x for i in tmp for j, x in enumerate(i) if j%2 != 0]

    
if __name__ == "__main__":
    pp = PixelPlotter()
    pp.set_image_array()
    #print(pp.image_array)
