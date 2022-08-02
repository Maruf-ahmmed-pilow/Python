{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4290ea34",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your Email : pilowpp1997@gmail.pom\n",
      " Right Email\n"
     ]
    }
   ],
   "source": [
    "email = input(\"Enter your Email : \")\n",
    "k=0\n",
    "j=0\n",
    "d=0\n",
    "if len(email)>=10:\n",
    "    if email[0].isalpha():\n",
    "        if (\"@\" in email) and (email.count(\"@\")==1):\n",
    "            if (email[-4] ==\".\")^(email[-3]==\".\"):\n",
    "                for i in email:\n",
    "                    if i==i.isspace():\n",
    "                        k=1\n",
    "                    elif i.isalpha():\n",
    "                        if i==i.upper():\n",
    "                            j=1\n",
    "                    elif i.isdigit():\n",
    "                        continue\n",
    "                    elif i==\"_\"or i==\".\" or i==\"@\":\n",
    "                        continue\n",
    "                    else:\n",
    "                        d=1\n",
    "                        \n",
    "                            \n",
    "                if k==1 or j==1 or d==1:\n",
    "                    print(' Wrong Email 5')\n",
    "                else:\n",
    "                    print(' Right Email')\n",
    "            else:\n",
    "                print(' Wrong Email 4 ')\n",
    "                \n",
    "        else:\n",
    "            print(' Wrong Email 3')\n",
    "    else:\n",
    "        print(' Wrong Email 2 ')\n",
    "else:\n",
    "    print(' Wrong Email 1 ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "36931069",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
