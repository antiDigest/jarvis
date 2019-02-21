# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

# ################################################################################################
#       
#         Bot initialization script, this is where we take the command from the command
#         line and send that command to the bot internal systems
# 
# ################################################################################################
# ################################################################################################
# 
#         @version 0: argument parser to the input from command line
# 
#         @author: Antriksh Agarwal
# 
# ################################################################################################

# from . import *
import argparse
from interface.speech import talk

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Extract intent from statement")
    parser.add_argument("-c", "--command", type=str,
                        help="write a command for a response")

    args = parser.parse_args()

    talk.waitForInit()
