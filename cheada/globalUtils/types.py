# from enum import Enum

# # 과목
subject_format = ["수학 상", "수학 하", "수학 I", "수학 II", "미적분", "확률과 통계", "기하"]

# # 과목: 세부개념
# subject2detail = {
#     "기하": ["이차곡선", "이차곡선과 직선", "벡터의 연산", "평면벡터의 성분과 내적", "공간도형", "공간좌표"],
#     "확률과 통계": ["순열과 조합", "이항정리", "확률", "조건부확률", "확률분포", "통계적 추정"],
#     "미적분": ["수열의 극한", "급수", "여러가지 함수의 미분", "여러가지 미분법", "도함수의 활용", "여러가지 적분법", "정적분의 활용"],
#     "수학 II": ["함수의 극한", "함수의 연속", "미분계수", "도함수", "도함수의 활용", "부정적분", "정적분", "정적분의 활용"],
#     "수학 I": ["지수와 로그", "지수함수와 로그함수", "삼각함수", "삼각함수의 그래프", "삼각함수의 활용", "등차수열과 등비수열", "수열의 합", "수학적 귀납법"],
#     "수학 하": ["집합의 뜻과 표현", "집합의 연산", "명제", "함수", "유리식과 유리함수", "무리식과 무리함수", "순열과 조합"],
# 	"수학 상": ["다항식의 연산", "나머지정리와 인수분해", "복소수", "이차방정식", "이차방정식과 이차함수", "여러가지 방정식", "일차부등식", "이차부등식", "평면좌표", "직선의 방정식", "원의 방정식", "도형의 이동"],
# }

# # 과목: 단원
# subject2category = {
# 	"수학 상": ["다항식", "방정식", "부등식", "도형의 방정식"],
# 	"수학 하": ["집합과 명제", "함수", "순열과 조합"],
# 	"수학1": ["지수함수와 로그함수", "삼각함수", "수열"],
# 	"수학2": ["함수의 극한과 연속", "미분", "적분"],
# 	"미적분": ["수열의 극한", "미분법", "적분법"],
# 	"확률과 통계": ["경우의 수", "확률", "통계"],
# 	"기하": ["이차곡선", "평면벡터", "공간도형과 공간좌표"]
# }


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

class SubConcept(Enum):
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


class Chapter(Enum):
    Polynomial = ("다항식", [SubConcept.Operations_of_polynomials, SubConcept.Remainder_theorem_and_factorization])
    Equations = ("방정식", [SubConcept.Complex_numbers, SubConcept.Quadratic_equations, SubConcept.Quadratic_equations_and_quadratic_functions, SubConcept.Various_types_of_equations])
    Inequalities = ("부등식", [SubConcept.Linear_inequalities, SubConcept.Quadratic_inequalities])
    Equations_of_Shapes = ("도형의 방정식", [SubConcept.Plane_coordinates, SubConcept.Equations_of_lines, SubConcept.Equations_of_circles, SubConcept.Transformation_of_shapes])
    Sets_and_Propositions = ("집합과 명제", [SubConcept.Meaning_and_representation_of_sets, SubConcept.Operations_of_sets, SubConcept.Propositions])
    Functions = ("함수", [SubConcept.Functions, SubConcept.Rational_expressions_and_rational_functions, SubConcept.Irrational_expressions_and_irrational_functions])
    Permutations_and_Combinations = ("순열과 조합", [SubConcept.Permutations_and_combinations])
    Exponential_and_Logarithmic_Functions = ("지수함수와 로그함수", [SubConcept.Exponents_and_Logarithms, SubConcept.Exponential_and_Logarithmic_Functions])
    Trigonometric_Functions = ("삼각함수", [SubConcept.Trigonometric_Functions, SubConcept.Graphs_of_Trigonometric_Functions, SubConcept.Applications_of_Trigonometric_Functions])
    Sequences = ("수열", [SubConcept.Arithmetic_and_Geometric_Sequences, SubConcept.Sum_of_Sequences, SubConcept.Mathematical_Induction])
    Functions_Limits_and_Continuity = ("함수의 극한과 연속", [SubConcept.Functions_Limits, SubConcept.Functions_Continuity])
    Differentiation = ("미분", [SubConcept.Differential_Coefficient, SubConcept.Derivative_Functions, SubConcept.Applications_of_Derivatives])
    Integration_in_Math_2 = ("적분", [SubConcept.Indefinite_Integrals, SubConcept.Definite_Integrals, SubConcept.Applications_of_Definite_Integrals_in_Math_2])
    Limits_of_Sequences = ("수열의 극한", [SubConcept.Limits_of_Sequences, SubConcept.Series])
    Differential_Calculus = ("미분법", [SubConcept.Differentiation_of_Various_Functions, SubConcept.Various_Differentiation_Methods, SubConcept.Applications_of_Derivative_Functions])
    Integration_in_calculus = ("적분법", [SubConcept.Various_Integration_Methods, SubConcept.Applications_of_Definite_Integrals_in_Calculus])
    Counting_Methods = ("경우의 수", [SubConcept.Permutations_and_combinations, SubConcept.Binomial_Theorem])
    Probability = ("확률", [SubConcept.Probability, SubConcept.Conditional_Probability])
    Statistics = ("통계", [SubConcept.Probability_Distributions, SubConcept.Statistical_Estimation])
    Conic_Sections = ("이차곡선", [SubConcept.Conic_Sections, SubConcept.Conic_Sections_and_Lines])
    Plane_Vectors = ("평면벡터", [SubConcept.Vector_Operations, SubConcept.Components_and_Dot_Product_of_Plane_Vectors])
    Spatial_Shapes_and_Coordinates = ("공간도형과 공간좌표", [SubConcept.Spatial_Shapes, SubConcept.Spatial_Coordinates])

    def __str__(self):
        return self.value[0]


class Subject(Enum):
    Math_high = ("수학 상", [Chapter.Polynomial, Chapter.Equations, Chapter.Inequalities, Chapter.Equations_of_Shapes])
    Math_low = ("수학 하", [Chapter.Sets_and_Propositions, Chapter.Functions, Chapter.Permutations_and_Combinations])
    Math_1 = ("수학1", [Chapter.Exponential_and_Logarithmic_Functions, Chapter.Trigonometric_Functions, Chapter.Sequences])
    Math_2 = ("수학2", [Chapter.Functions_Limits_and_Continuity, Chapter.Differentiation, Chapter.Integration_in_Math_2])
    Calculus = ("미적분", [Chapter.Limits_of_Sequences, Chapter.Differential_Calculus, Chapter.Integration_in_calculus])
    Probability_and_Statistics = ("확률과 통계", [Chapter.Counting_Methods, Chapter.Probability, Chapter.Statistics])
    Geometry = ("기하", [Chapter.Conic_Sections, Chapter.Plane_Vectors, Chapter.Spatial_Shapes_and_Coordinates])

    def __str__(self):
        return self.value[0]