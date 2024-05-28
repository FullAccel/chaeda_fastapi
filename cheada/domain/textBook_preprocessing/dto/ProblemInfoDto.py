class ProblemInfoDto:
    def __init__(self, subject, publish_year, textbook_name, page_num, problem_num, image_file_extension):
        """
        문제 정보를 담는 DTO 클래스.

        :param subject: 과목 이름
        :param publish_year: 교재의 출판 연도
        :param textbook_name: 교재 이름
        :param page_num: 페이지 번호
        :param problem_num: 문제 번호
        :param image_file_extension: 이미지 파일 확장자
        """
        
        self.subject = subject
        self.publish_year = publish_year
        self.textbook_name = textbook_name
        self.page_num = page_num
        self.problem_num = problem_num
        self.image_file_extension = image_file_extension