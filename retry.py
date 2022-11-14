import os, time
import colorama
from colorama import Fore, Back, Style

def retry():
    os.system("clear")
    print(Back.RED + '                                ')
    print(Back.RED + '          '+Style.RESET_ALL+'_,---._'+Style.RESET_ALL+Back.RED+'               ')
    print(Back.RED +Fore.RED+'XXXXXXXX'+Style.RESET_ALL+'___________'+Back.RED+Fore.RED+'XXXXXXXXXXXXX')
    print(Back.RED +Fore.RED+'XXXXXXXXX'+Style.RESET_ALL+'-( X X )-'+Back.RED+Fore.RED+'XXXXXXXXXXXXXX')
    print('XXXXXXXXXX'+Style.RESET_ALL+' \(_)/ '+Back.RED+Fore.RED+'XXXXXXXXXXXXXXX')
    print('XXXXXXXXXXX'+Style.RESET_ALL+' )~( '+Back.RED+Fore.RED+'XXXXXXXXXXXXXXXX')
    print('XXXXXXXXXXXX'+Style.RESET_ALL+'"""'+Back.RED+Fore.RED+'XXXXXXXXXXXXXXXXX')
    print('XXXXXXXX'+Style.RESET_ALL+'            '+Back.RED+Fore.RED+'XXXXXXXXXXXX')
    print('XXXXXXXX'+Style.RESET_ALL+'  YOU DIED  '+Back.RED+Fore.RED+'XXXXXXXXXXXX')
    print('XXXXXXXX'+Style.RESET_ALL+'            '+Back.RED+Fore.RED+'XXXXXXXXXXXX')
    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    print(Style.RESET_ALL)
    time.sleep(1)
    print(Back.LIGHTRED_EX+Fore.BLACK+Style.BRIGHT)
    print(''' *******   ********     **     *******  
/**////** /**/////     ****   /**////** 
/**    /**/**         **//**  /**    /**
/**    /**/*******   **  //** /**    /**
/**    /**/**////   **********/**    /**
/**    ** /**      /**//////**/**    ** 
/*******  /********/**     /**/*******  
///////   //////// //      // ///////   ''')
    print(Style.RESET_ALL)
    time.sleep(0.5)
    while True:
        try:
            retrykey=input('Retry (y/n): ')
            if retrykey == 'y':
                return
            if retrykey == 'n':
                print("See you!")
                quit()
        except KeyboardInterrupt:
            print('Interrupted by player, exiting the game.....\033[?25h')
            break 
