{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "04814efe",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "acecacc9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import mysql.connector"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6824ca17",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "adc1124f",
   "metadata": {},
   "outputs": [],
   "source": [
    "conn=mysql.connector.connect(host='127.0.0.1',port='3306',user='root',password='root',database='newdb')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "4a68cb0e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Connected\n"
     ]
    }
   ],
   "source": [
    "if conn.is_connected():\n",
    "    print('Connected')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "ff5b201f",
   "metadata": {},
   "outputs": [],
   "source": [
    "mycursor=conn.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "1b13568f",
   "metadata": {},
   "outputs": [],
   "source": [
    "mycursor.execute('select * from student')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "b216bffd",
   "metadata": {},
   "outputs": [],
   "source": [
    "myresult=mycursor.fetchall()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "29e33716",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Veeranna', 30, 'M', 1000),\n",
       " ('Vikrant', 3, 'M', 1),\n",
       " ('Vishal', 22, 'M', 1000),\n",
       " ('Veena', 28, 'F', 500)]"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myresult"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "812aa3fb",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_sql('select * from student',conn)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "9c27fc5e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>Pythonmark</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Veeranna</td>\n",
       "      <td>30</td>\n",
       "      <td>M</td>\n",
       "      <td>1000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Vikrant</td>\n",
       "      <td>3</td>\n",
       "      <td>M</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Vishal</td>\n",
       "      <td>22</td>\n",
       "      <td>M</td>\n",
       "      <td>1000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Veena</td>\n",
       "      <td>28</td>\n",
       "      <td>F</td>\n",
       "      <td>500</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       name  age sex  Pythonmark\n",
       "0  Veeranna   30   M        1000\n",
       "1   Vikrant    3   M           1\n",
       "2    Vishal   22   M        1000\n",
       "3     Veena   28   F         500"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ea810bd7",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
