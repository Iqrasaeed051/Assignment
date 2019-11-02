{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Twinkle, Twinkle little star,\n",
      "\t How I wonder what you are!\n",
      "\t\t Up above the world so high,\n",
      "\t\t Like the diamond in the sky.\n",
      " Twinkle, Twinkle,little star,\n",
      "\t How I wonder What you are!\n"
     ]
    }
   ],
   "source": [
    "print(\"Twinkle, Twinkle little star,\\n\\t How I wonder what you are!\\n\\t\\t Up above the world so high,\\n\\t\\t Like the diamond in the sky.\\n Twinkle, Twinkle,little star,\\n\\t How I wonder What you are!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.7.4 (default, Aug  9 2019, 18:22:51) [MSC v.1915 32 bit (Intel)]\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "print(sys.version)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "now= 2019-11-01 01:18:13.555561\n",
      "date and time= 01/11/2019 01:18:13\n"
     ]
    }
   ],
   "source": [
    "from datetime import datetime\n",
    "now- datetime.now()\n",
    "print(\"now=\",now)\n",
    "st_string = now.strftime(\"%Y%m%d %H:%M:%S\")\n",
    "print(\"date and time=\",dt_string)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the are of a circle:25\n",
      "1962.5\n"
     ]
    }
   ],
   "source": [
    "pi = 3.14\n",
    "r = float(input(\"Enter the are of a circle:\"))\n",
    "area = pi*r*r\n",
    "print(area)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "iqra saeed\n",
      "deeas arqi\n"
     ]
    }
   ],
   "source": [
    "f_name = \"iqra\"\n",
    "l_name = \"saeed\"\n",
    "final = f_name + \" \" + l_name\n",
    "str_length = len(final)\n",
    "sl = final[str_length::-1]\n",
    "print(final)\n",
    "print(sl)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter first number:10\n",
      "Enter second number:10\n",
      "20\n"
     ]
    }
   ],
   "source": [
    "a = input(\"Enter first number:\")\n",
    "b = input(\"Enter second number:\")\n",
    "sum = int(a)+int(b)\n",
    "print(sum)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
