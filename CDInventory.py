#------------------------------------------#
# Title: CDInventory.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# CMontejo, 2022-Aug-13, Copied File
# CMontejo, 2022-Aug-14, Cleaned up formatting and comments, moved TODOs to functions, added error handling to read_file function 
#------------------------------------------#

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object


# -- PROCESSING -- #
class DataProcessor:
    """Processing the data within the script"""

    @staticmethod
    def add_cd(lstTbl, strID, strTitle, strArtist):
        """Adds new CD to the table
        
        Args:
            lstTbl (list of lists): 2D table to hold CD Inventory data
            strID (string): ID number for the CD
            strTitle (string): Title of the CD
            strArtist (string): Artist for the CD 
        
        Returns:
            None.
            """
        intID = int(float(strID))
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
        lstTbl.append(dicRow)
        IO.show_inventory(lstTbl)
    
    @staticmethod
    def del_cd(lstTbl):
        """Deletes a CD from the table
    
        Args:
            lstTbl (list of lists): 2D table to hold CD Inventory data
        
        Returns:
            lstTbl (list of lists): 2D table to hold CD Inventory data
            """
        intRowNr = -1
        blnCDRemoved = False
        for row in lstTbl:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstTbl[intRowNr]
                blnCDRemoved = True
        if blnCDRemoved:
            print('The CD was removed\n')
            return lstTbl
        else:
            print('Could not find this CD!\n')

class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        try:
            table.clear()  # this clears existing data and allows to load data from file
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',')
                dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
                table.append(dicRow)
            objFile.close()
        except:
            pass

    @staticmethod
    def write_file(file_name, table):
        """Function to manage data ingestion from a list of dictionaries to a file
    
        Reads the data from a 2D table (list of dictionaries) identified as lstTbl into a file.
    
        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
    
        Returns:
            None.
        """
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            lstValues = list(row.values())
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()


# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] Load Inventory from File\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] Delete CD from Inventory\n[s] Save Inventory to File\n[x] Exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x
        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.
        """
        print()  # Add extra space for layout
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')
        print()  # Add extra space for layout
    
    @staticmethod
    def new_cd():
        """Get user input for a new CD
        
        Args:
            None.
        
        Returns:
            None.
        """
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        DataProcessor.add_cd(lstTbl, strID, strTitle, strArtist)

# -- INTERFACE -- #
# 1. When program starts, read in the currently saved Inventory
FileProcessor.read_file(strFileName, lstTbl)

# 2. Start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

# 3. Process menu selection
    # 3.1 Process exit first
    if strChoice == 'x':
        break
        
    # 3.2 Process to load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('Type \'yes\' to continue and reload from file. Otherwise reload will be canceled\n')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileProcessor.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # Start loop back at top
        
    # 3.3 Process to add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist and add item to the table (Was a TODO)
        IO.new_cd()
        continue  # Start loop back at top
        
    # 3.4 Process to display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # Start loop back at top
        
    # 3.5 Process to delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
            # 3.5.1.1 Display Inventory to user
        IO.show_inventory(lstTbl)
            # 3.5.1.2 Ask user which ID to remove
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        # 3.5.2 Search thru table and delete CD (Was a TODO)
        DataProcessor.del_cd(lstTbl)
        IO.show_inventory(lstTbl)
        continue  # Start loop back at top
        
    # 3.6 Process to save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 Save data (Was a TODO)
           FileProcessor.write_file(strFileName, lstTbl)
           pass
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # Start loop back at top
        
    # 3.7 Catch-all should not be possible, as user choice gets vetted in I/O, but to be safe:
    else:
        print('General Error')




