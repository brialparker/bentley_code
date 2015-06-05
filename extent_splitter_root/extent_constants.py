from pprint import pprint

integers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

numbers_dict = {' Eight ': '8',
                ' Eighteen ': '18',
                ' Eighty ': '80',
                ' Eighty-eight ': '88',
                ' Eighty-five ': '85',
                ' Eighty-four ': '84',
                ' Eighty-nine ': '89',
                ' Eighty-one ': '81',
                ' Eighty-seven ': '87',
                ' Eighty-six ': '86',
                ' Eighty-three ': '83',
                ' Eighty-two ': '82',
                ' Eleven ': '11',
                ' Fifteen ': '15',
                ' Fifty ': '50',
                ' Fifty-eight ': '58',
                ' Fifty-five ': '55',
                ' Fifty-four ': '54',
                ' Fifty-nine ': '59',
                ' Fifty-one ': '51',
                ' Fifty-seven ': '57',
                ' Fifty-six ': '56',
                ' Fifty-three ': '53',
                ' Fifty-two ': '52',
                ' Five ': '5',
                ' Forty ': '40',
                ' Forty-eight ': '48',
                ' Forty-five ': '45',
                ' Forty-four ': '44',
                ' Forty-nine ': '49',
                ' Forty-one ': '41',
                ' Forty-seven ': '47',
                ' Forty-six ': '46',
                ' Forty-three ': '43',
                ' Forty-two ': '42',
                ' Four ': '4',
                ' Fourteen ': '14',
                ' Nine ': '9',
                ' Nineteen ': '19',
                ' Ninety ': '90',
                ' Ninety-eight ': '98',
                ' Ninety-five ': '95',
                ' Ninety-four ': '94',
                ' Ninety-nine ': '99',
                ' Ninety-one ': '91',
                ' Ninety-seven ': '97',
                ' Ninety-six ': '96',
                ' Ninety-three ': '93',
                ' Ninety-two ': '92',
                ' One ': '1',
                ' Seven ': '7',
                ' Seventeen ': '17',
                ' Seventy ': '70',
                ' Seventy-eight ': '78',
                ' Seventy-five ': '75',
                ' Seventy-four ': '74',
                ' Seventy-nine ': '79',
                ' Seventy-one ': '71',
                ' Seventy-seven ': '77',
                ' Seventy-six ': '76',
                ' Seventy-three ': '73',
                ' Seventy-two ': '72',
                ' Six ': '6',
                ' Sixteen ': '16',
                ' Sixty ': '60',
                ' Sixty-eight ': '68',
                ' Sixty-five ': '65',
                ' Sixty-four ': '64',
                ' Sixty-nine ': '69',
                ' Sixty-one ': '61',
                ' Sixty-seven ': '67',
                ' Sixty-six ': '66',
                ' Sixty-three ': '63',
                ' Sixty-two ': '62',
                ' Ten ': '10',
                ' Thirteen ': '13',
                ' Thirty ': '30',
                ' Thirty-eight ': '38',
                ' Thirty-five ': '35',
                ' Thirty-four ': '34',
                ' Thirty-nine ': '39',
                ' Thirty-one ': '31',
                ' Thirty-seven ': '37',
                ' Thirty-six ': '36',
                ' Thirty-three ': '33',
                ' Thirty-two ': '32',
                ' Three ': '3',
                ' Twelve ': '12',
                ' Twenty ': '20',
                ' Twenty-eight ': '28',
                ' Twenty-five ': '25',
                ' Twenty-four ': '24',
                ' Twenty-nine ': '29',
                ' Twenty-one ': '21',
                ' Twenty-seven ': '27',
                ' Twenty-six ': '26',
                ' Twenty-three ': '23',
                ' Twenty-two ': '22',
                ' Two ': '2',
                ' eight ': '8',
                ' eighteen ': '18',
                ' eighty ': '80',
                ' eighty-eight ': '88',
                ' eighty-five ': '85',
                ' eighty-four ': '84',
                ' eighty-nine ': '89',
                ' eighty-one ': '81',
                ' eighty-seven ': '87',
                ' eighty-six ': '86',
                ' eighty-three ': '83',
                ' eighty-two ': '82',
                ' eleven ': '11',
                ' fifteen ': '15',
                ' fifty ': '50',
                ' fifty-eight ': '58',
                ' fifty-five ': '55',
                ' fifty-four ': '54',
                ' fifty-nine ': '59',
                ' fifty-one ': '51',
                ' fifty-seven ': '57',
                ' fifty-six ': '56',
                ' fifty-three ': '53',
                ' fifty-two ': '52',
                ' five ': '5',
                ' forty ': '40',
                ' forty-eight ': '48',
                ' forty-five ': '45',
                ' forty-four ': '44',
                ' forty-nine ': '49',
                ' forty-one ': '41',
                ' forty-seven ': '47',
                ' forty-six ': '46',
                ' forty-three ': '43',
                ' forty-two ': '42',
                ' four ': '4',
                ' fourteen ': '14',
                ' nine ': '9',
                ' nineteen ': '19',
                ' ninety ': '90',
                ' ninety-eight ': '98',
                ' ninety-five ': '95',
                ' ninety-four ': '94',
                ' ninety-nine ': '99',
                ' ninety-one ': '91',
                ' ninety-seven ': '97',
                ' ninety-six ': '96',
                ' ninety-three ': '93',
                ' ninety-two ': '92',
                ' one ': '1',
                ' seven ': '7',
                ' seventeen ': '17',
                ' seventy ': '70',
                ' seventy-eight ': '78',
                ' seventy-five ': '75',
                ' seventy-four ': '74',
                ' seventy-nine ': '79',
                ' seventy-one ': '71',
                ' seventy-seven ': '77',
                ' seventy-six ': '76',
                ' seventy-three ': '73',
                ' seventy-two ': '72',
                ' six ': '6',
                ' sixteen ': '16',
                ' sixty ': '60',
                ' sixty-eight ': '68',
                ' sixty-five ': '65',
                ' sixty-four ': '64',
                ' sixty-nine ': '69',
                ' sixty-one ': '61',
                ' sixty-seven ': '67',
                ' sixty-six ': '66',
                ' sixty-three ': '63',
                ' sixty-two ': '62',
                ' ten ': '10',
                ' thirteen ': '13',
                ' thirty ': '30',
                ' thirty-eight ': '38',
                ' thirty-five ': '35',
                ' thirty-four ': '34',
                ' thirty-nine ': '39',
                ' thirty-one ': '31',
                ' thirty-seven ': '37',
                ' thirty-six ': '36',
                ' thirty-three ': '33',
                ' thirty-two ': '32',
                ' three ': '3',
                ' twelve ': '12',
                ' twenty ': '20',
                ' twenty-eight ': '28',
                ' twenty-five ': '25',
                ' twenty-four ': '24',
                ' twenty-nine ': '29',
                ' twenty-one ': '21',
                ' twenty-seven ': '27',
                ' twenty-six ': '26',
                ' twenty-three ': '23',
                ' twenty-two ': '22',
                ' two ': '2'}
