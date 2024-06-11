# from enum import Enum

# 과목
subject_format = ["수학 상", "수학 하", "수학 I", "수학 II", "미적분", "확률과 통계", "기하"]

# 과목: 세부개념
subject2detail = {
    "기하": ["이차곡선", "이차곡선과 직선", "벡터의 연산", "평면벡터의 성분과 내적", "공간도형", "공간좌표"],
    "확률과 통계": ["순열과 조합", "이항정리", "확률", "조건부확률", "확률분포", "통계적 추정"],
    "미적분": ["수열의 극한", "급수", "여러가지 함수의 미분", "여러가지 미분법", "도함수의 활용", "여러가지 적분법", "정적분의 활용"],
    "수학 II": ["함수의 극한", "함수의 연속", "미분계수", "도함수", "도함수의 활용", "부정적분", "정적분", "정적분의 활용"],
    "수학 I": ["지수와 로그", "지수함수와 로그함수", "삼각함수", "삼각함수의 그래프", "삼각함수의 활용", "등차수열과 등비수열", "수열의 합", "수학적 귀납법"],
    "수학 하": ["집합의 뜻과 표현", "집합의 연산", "명제", "함수", "유리식과 유리함수", "무리식과 무리함수", "순열과 조합"],
	"수학 상": ["다항식의 연산", "나머지정리와 인수분해", "복소수", "이차방정식", "이차방정식과 이차함수", "여러가지 방정식", "일차부등식", "이차부등식", "평면좌표", "직선의 방정식", "원의 방정식", "도형의 이동"],
}

# 과목: 단원
subject2category = {
	"수학 상": ["다항식", "방정식", "부등식", "도형의 방정식"],
	"수학 하": ["집합과 명제", "함수", "순열과 조합"],
	"수학1": ["지수함수와 로그함수", "삼각함수", "수열"],
	"수학2": ["함수의 극한과 연속", "미분", "적분"],
	"미적분": ["수열의 극한", "미분법", "적분법"],
	"확률과 통계": ["경우의 수", "확률", "통계"],
	"기하": ["이차곡선", "평면벡터", "공간도형과 공간좌표"]
}


# class SubjectEnum(Enum):
#     Math_high = "수학 상",
#     Math_low = "수학 하"
#     Math_1 = "수학1"
#     Math_2 = "수학2"
#     Calculus = "미적분"
#     Probability_and_Statistics = "확률과 통계"
#     Geometry = "기하"
#     Mix = "혼합형"

# class ChapterEnum(Enum):
#     #수학 상
#     Polynomial = "다항식"
#     Equations = "방정식"
#     Inequalities = "부등식"
#     Equations_of_Shapes = "도형의 방정식"

#    	#수학 하
#     Sets_and_Propositions = "집합과 명제"
#     Functions = "함수"
#     Permutations_and_Combinations = "순열과 조합"

#    	#수학1
#     Exponential_and_Logarithmic_Functions = "지수함수와 로그함수"
#     Trigonometric_Functions = "삼각함수"
#     Sequences = "수열"

#    	#수학2
#     Functions_Limits_and_Continuity = "함수의 극한과 연속"
#     Differentiation = "미분"
#     Integration_in_Math_2 = "적분"

#    	#미적분
#     Limits_of_Sequences = "수열의 극한"
#     Differential_Calculus = "미분법"
#     Integration_in_calculus = "적분법"

#    	#확률과 통계
#     Counting_Methods = "경우의 수"
#     Probability = "확률"
#     Statistics = "통계"

#    	#기하
#     Conic_Sections = "이차곡선"
#     Plane_Vectors = "평면벡터"
#     Spatial_Shapes_and_Coordinates = "공간도형과 공간좌표"

# class SubConceptEnum(Enum):
#     #------------------수학 상-----------------------
#     # Polynomial : 다항식
#     Operations_of_polynomials = "다항식의 연산"
#     Remainder_theorem_and_factorization = "나머지정리와 인수분해"

#     # Equations : 방정식
#     Complex_numbers = "복소수"
#     Quadratic_equations = "이차방정식"
#     Quadratic_equations_and_quadratic_functions = "이차방정식과 이차함수"
#     Various_types_of_equations = "여러 가지 방정식"

#     # Inequalities : 부등식
#     Linear_inequalities = "일차부등식"
#     Quadratic_inequalities = "이차부등식"

#     # Equations_of_Shapes : 도형의 방정식
#     Plane_coordinates = "평면좌표"
#     Equations_of_lines = "직선의 방정식"
#     Equations_of_circles = "원의 방정식"
#     Transformation_of_shapes = "도형의 이동"


#     #------------------수학 하-----------------------
#     # Sets_and_Propositions : 집합과 명제
#     Meaning_and_representation_of_sets = "집합의 뜻과 표현"
#     Operations_of_sets = "집합의 연산"
#     Propositions = "명제"

#     # Functions : 함수
#     Functions = "함수"
#     Rational_expressions_and_rational_functions = "유리식과 유리함수"
#     Irrational_expressions_and_irrational_functions = "무리식과 무리함수"

#     # Permutations_and_Combinations : 순열과 조합
#     Permutations_and_combinations = "순열과 조합"


#     #------------------수1-----------------------
#     #Exponential_and_Logarithmic_Functions : 지수함수와 로그함수
#     Exponents_and_Logarithms = "지수와 로그"
#     Exponential_and_Logarithmic_Functions = "지수함수와 로그함수"

#     #Trigonometric_Functions : 삼각함수
#     Trigonometric_Functions = "삼각함수"
#     Graphs_of_Trigonometric_Functions = "삼각함수의 그래프"
#     Applications_of_Trigonometric_Functions = "삼각함수의 활용"

#     #Sequences : 수열
#     Arithmetic_and_Geometric_Sequences = "등차수열과 등비수열"
#     Sum_of_Sequences = "수열의 합"
#     Mathematical_Induction = "수학적 귀납법"


#     #------------------수학 II-----------------------
#     # Functions_Limits_and_Continuity : 함수의 극한과 연속
#     Functions_Limits = "함수의 극한"
#     Functions_Continuity = "함수의 연속"

#     # Differentiation : 미분
#     Differential_Coefficient = "미분계수"
#     Derivative_Functions = "도함수"
#     Applications_of_Derivatives = "도함수의 활용"

#     # Integration : 적분
#     Indefinite_Integrals = "부정적분"
#     Definite_Integrals = "정적분"
#     Applications_of_Definite_Integrals_in_Math_2 = "정적분의 활용"


#     #------------------미적분-----------------------
#     # Limits_of_Sequences : 수열의 극한
#     Limits_of_Sequences = "수열의 극한"
#     Series = "급수"

#     # Differential_Calculus : 미분법
#     Differentiation_of_Various_Functions = "여러 가지 함수의 미분"
#     Various_Differentiation_Methods = "여러 가지 미분법"
#     Applications_of_Derivative_Functions = "도함수의 활용"

#     # Integration : 적분법
#     Various_Integration_Methods = "여러 가지 적분법"
#     Applications_of_Definite_Integrals_in_Calculus = "정적분의 활용"


#     #------------------확률과 통계-----------------------
#     # Counting_Methods : 경우의 수
#     Permutations_and_Combinations = "순열과 조합"
#     Binomial_Theorem = "이항정리"

#     # Probability : 확률
#     Probability = "확률"
#     Conditional_Probability = "조건부확률"

#     # Statistics : 통계
#     Probability_Distributions = "확률분포"
#     Statistical_Estimation = "통계적 추정"


#     #------------------기하-----------------------
#     # Conic_Sections : 이차곡선
#     Conic_Sections = "이차곡선"
#     Conic_Sections_and_Lines = "이차곡선과 직선"

#     # Plane_Vectors : 평면벡터
#     Vector_Operations = "벡터의 연산"
#     Components_and_Dot_Product_of_Plane_Vectors = "평면벡터의 성분과 내적"

#     # Spatial_Shapes_and_Coordinates : 공간도형과 공간좌표
#     Spatial_Shapes = "공간도형"
#     Spatial_Coordinates = "공간좌표"


from enum import Enum
from typing import List

class SubConceptEnum(Enum):
    Operations_of_polynomials = "다항식의 연산"
    Remainder_theorem_and_factorization = "나머지정리와 인수분해"
    Complex_numbers = "복소수"
    Quadratic_equations = "이차방정식"
    Quadratic_equations_and_quadratic_functions = "이차방정식과 이차함수"
    Various_types_of_equations = "여러 가지 방정식"
    Linear_inequalities = "일차부등식"
    Quadratic_inequalities = "이차부등식"
    Plane_coordinates = "평면좌표"
    Equations_of_lines = "직선의 방정식"
    Equations_of_circles = "원의 방정식"
    Transformation_of_shapes = "도형의 이동"
    Meaning_and_representation_of_sets = "집합의 뜻과 표현"
    Operations_of_sets = "집합의 연산"
    Propositions = "명제"
    Functions = "함수"
    Rational_expressions_and_rational_functions = "유리식과 유리함수"
    Irrational_expressions_and_irrational_functions = "무리식과 무리함수"
    Permutations_and_combinations = "순열과 조합"
    Exponents_and_Logarithms = "지수와 로그"
    Exponential_and_Logarithmic_Functions = "지수함수와 로그함수"
    Trigonometric_Functions = "삼각함수"
    Graphs_of_Trigonometric_Functions = "삼각함수의 그래프"
    Applications_of_Trigonometric_Functions = "삼각함수의 활용"
    Arithmetic_and_Geometric_Sequences = "등차수열과 등비수열"
    Sum_of_Sequences = "수열의 합"
    Mathematical_Induction = "수학적 귀납법"
    Functions_Limits = "함수의 극한"
    Functions_Continuity = "함수의 연속"
    Differential_Coefficient = "미분계수"
    Derivative_Functions = "도함수"
    Applications_of_Derivatives = "도함수의 활용"
    Indefinite_Integrals = "부정적분"
    Definite_Integrals = "정적분"
    Applications_of_Definite_Integrals_in_Math_2 = "정적분의 활용"
    Limits_of_Sequences = "수열의 극한"
    Series = "급수"
    Differentiation_of_Various_Functions = "여러 가지 함수의 미분"
    Various_Differentiation_Methods = "여러 가지 미분법"
    Applications_of_Derivative_Functions = "도함수의 활용"
    Various_Integration_Methods = "여러 가지 적분법"
    Applications_of_Definite_Integrals_in_Calculus = "정적분의 활용"
    Binomial_Theorem = "이항정리"
    Probability = "확률"
    Conditional_Probability = "조건부확률"
    Probability_Distributions = "확률분포"
    Statistical_Estimation = "통계적 추정"
    Conic_Sections = "이차곡선"
    Conic_Sections_and_Lines = "이차곡선과 직선"
    Vector_Operations = "벡터의 연산"
    Components_and_Dot_Product_of_Plane_Vectors = "평면벡터의 성분과 내적"
    Spatial_Shapes = "공간도형"
    Spatial_Coordinates = "공간좌표"


class ChapterEnum(Enum):
    Polynomial = ("다항식", [SubConceptEnum.Operations_of_polynomials, SubConceptEnum.Remainder_theorem_and_factorization])
    Equations = ("방정식", [SubConceptEnum.Complex_numbers, SubConceptEnum.Quadratic_equations, SubConceptEnum.Quadratic_equations_and_quadratic_functions, SubConceptEnum.Various_types_of_equations])
    Inequalities = ("부등식", [SubConceptEnum.Linear_inequalities, SubConceptEnum.Quadratic_inequalities])
    Equations_of_Shapes = ("도형의 방정식", [SubConceptEnum.Plane_coordinates, SubConceptEnum.Equations_of_lines, SubConceptEnum.Equations_of_circles, SubConceptEnum.Transformation_of_shapes])
    Sets_and_Propositions = ("집합과 명제", [SubConceptEnum.Meaning_and_representation_of_sets, SubConceptEnum.Operations_of_sets, SubConceptEnum.Propositions])
    Functions = ("함수", [SubConceptEnum.Functions, SubConceptEnum.Rational_expressions_and_rational_functions, SubConceptEnum.Irrational_expressions_and_irrational_functions])
    Permutations_and_Combinations = ("순열과 조합", [SubConceptEnum.Permutations_and_combinations])
    Exponential_and_Logarithmic_Functions = ("지수함수와 로그함수", [SubConceptEnum.Exponents_and_Logarithms, SubConceptEnum.Exponential_and_Logarithmic_Functions])
    Trigonometric_Functions = ("삼각함수", [SubConceptEnum.Trigonometric_Functions, SubConceptEnum.Graphs_of_Trigonometric_Functions, SubConceptEnum.Applications_of_Trigonometric_Functions])
    Sequences = ("수열", [SubConceptEnum.Arithmetic_and_Geometric_Sequences, SubConceptEnum.Sum_of_Sequences, SubConceptEnum.Mathematical_Induction])
    Functions_Limits_and_Continuity = ("함수의 극한과 연속", [SubConceptEnum.Functions_Limits, SubConceptEnum.Functions_Continuity])
    Differentiation = ("미분", [SubConceptEnum.Differential_Coefficient, SubConceptEnum.Derivative_Functions, SubConceptEnum.Applications_of_Derivatives])
    Integration_in_Math_2 = ("적분", [SubConceptEnum.Indefinite_Integrals, SubConceptEnum.Definite_Integrals, SubConceptEnum.Applications_of_Definite_Integrals_in_Math_2])
    Limits_of_Sequences = ("수열의 극한", [SubConceptEnum.Limits_of_Sequences, SubConceptEnum.Series])
    Differential_Calculus = ("미분법", [SubConceptEnum.Differentiation_of_Various_Functions, SubConceptEnum.Various_Differentiation_Methods, SubConceptEnum.Applications_of_Derivative_Functions])
    Integration_in_calculus = ("적분법", [SubConceptEnum.Various_Integration_Methods, SubConceptEnum.Applications_of_Definite_Integrals_in_Calculus])
    Counting_Methods = ("경우의 수", [SubConceptEnum.Permutations_and_combinations, SubConceptEnum.Binomial_Theorem])
    Probability = ("확률", [SubConceptEnum.Probability, SubConceptEnum.Conditional_Probability])
    Statistics = ("통계", [SubConceptEnum.Probability_Distributions, SubConceptEnum.Statistical_Estimation])
    Conic_Sections = ("이차곡선", [SubConceptEnum.Conic_Sections, SubConceptEnum.Conic_Sections_and_Lines])
    Plane_Vectors = ("평면벡터", [SubConceptEnum.Vector_Operations, SubConceptEnum.Components_and_Dot_Product_of_Plane_Vectors])
    Spatial_Shapes_and_Coordinates = ("공간도형과 공간좌표", [SubConceptEnum.Spatial_Shapes, SubConceptEnum.Spatial_Coordinates])

    def __str__(self):
        return self.value[0]


class SubjectEnum(Enum):
    Math_high = ("수학 상", [ChapterEnum.Polynomial, ChapterEnum.Equations, ChapterEnum.Inequalities, ChapterEnum.Equations_of_Shapes])
    Math_low = ("수학 하", [ChapterEnum.Sets_and_Propositions, ChapterEnum.Functions, ChapterEnum.Permutations_and_Combinations])
    Math_1 = ("수학1", [ChapterEnum.Exponential_and_Logarithmic_Functions, ChapterEnum.Trigonometric_Functions, ChapterEnum.Sequences])
    Math_2 = ("수학2", [ChapterEnum.Functions_Limits_and_Continuity, ChapterEnum.Differentiation, ChapterEnum.Integration_in_Math_2])
    Calculus = ("미적분", [ChapterEnum.Limits_of_Sequences, ChapterEnum.Differential_Calculus, ChapterEnum.Integration_in_calculus])
    Probability_and_Statistics = ("확률과 통계", [ChapterEnum.Counting_Methods, ChapterEnum.Probability, ChapterEnum.Statistics])
    Geometry = ("기하", [ChapterEnum.Conic_Sections, ChapterEnum.Plane_Vectors, ChapterEnum.Spatial_Shapes_and_Coordinates])

    def __str__(self):
        return self.value[0]