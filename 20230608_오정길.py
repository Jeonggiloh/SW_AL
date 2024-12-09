
# coding: utf-8

# In[ ]:


import random

class ArrayQueue:
    """ 배열 기반 큐 구현 """
    def __init__(self, size):
        self.queue = [None] * size  # 큐의 최대 크기
        self.front = 0  # 큐의 앞 부분 인덱스
        self.rear = 0   # 큐의 뒷 부분 인덱스
    
    def enqueue(self, value):
        """ 큐에 값을 추가 """
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % len(self.queue)
    
    def dequeue(self):
        """ 큐에서 값을 꺼내기 """
        value = self.queue[self.front]
        self.front = (self.front + 1) % len(self.queue)
        return value
    
    def is_empty(self):
        """ 큐가 비었는지 확인 """
        return self.front == self.rear
    
    def size(self):
        """ 큐의 현재 크기 """
        return (self.rear - self.front) % len(self.queue)


def radix_sort(students, key):
    """
    기수 정렬 알고리즘.
    각 자릿수에 대해 정렬을 수행하고 그 과정을 출력합니다.
    성적을 기준으로 정렬합니다.
    """
    Buckets = 10  # 십진수 정렬 (0~9)
    Digits = 3    # 정렬할 숫자의 자릿수 (최대 3자리 성적)

    # 각 자릿수를 위한 원형 큐 생성
    queues = [ArrayQueue(len(students)) for _ in range(Buckets)]

    n = len(students)
    factor = 1  # 1, 10, 100... (자릿수에 맞춰 증가)
    
    for d in range(Digits):
        print(f"\nSorting by digit at place {factor}:")
        
        # 1. 각 자릿수에 대해 정렬 (성적 기준)
        for i in range(n):
            digit = (students[i][key] // factor) % Buckets  # 해당 자릿수 추출
            queues[digit].enqueue(students[i])  # 해당 큐에 삽입
            print(f"Enqueued {students[i]} in bucket {digit}")
        
        # 2. 큐에서 다시 배열로 값을 꺼내어 정렬된 상태로 재배열
        i = 0
        for b in range(Buckets):
            while not queues[b].is_empty():
                students[i] = queues[b].dequeue()  # 큐에서 꺼내어 배열에 재배치
                i += 1
        
        # 3. 현재 자릿수 기준으로 정렬된 배열 상태 출력
        print(f"After sorting by digit {factor}, array: {students}")
        
        # 4. 다음 자릿수로 이동 (자릿수 증가)
        factor *= Buckets
    
    # 최종 결과 출력
    print("\nFinal sorted array:", students)


# 학생 정보 생성 함수
def generate_students(num_students=30):
    students = []
    for _ in range(num_students):
        name = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))
        age = random.randint(18, 22)
        score = random.randint(0, 100)
        students.append({"이름": name, "나이": age, "성적": score})
    return students


# 선택 정렬 구현
def selection_sort(arr, key):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j][key] < arr[min_index][key]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        # 각 단계에서 배열 상태 출력
        print(f"Step {i + 1}: {arr}\n")


# 삽입 정렬 구현
def insertion_sort(arr, key):
    for i in range(1, len(arr)):
        key_value = arr[i]
        j = i - 1
        while j >= 0 and arr[j][key] > key_value[key]: # key_value보다 큰 값들을 오른쪽으로 이동
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_value
        # 각 단계에서 배열 상태 출력
        print(f"Step {i}: {arr}")


# 퀵 정렬 구현
def quick_sort(arr, left, right, key):
    if left < right:
        q = partition(arr, left, right, key)
        quick_sort(arr, left, q - 1, key)
        quick_sort(arr, q + 1, right, key)


def partition(arr, left, right, key):
    low = left + 1
    high = right
    pivot = arr[left][key]
    
    while low <= high:
        while low <= right and arr[low][key] <= pivot:
            low += 1
        while high >= left and arr[high][key] > pivot:
            high -= 1
        
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
    
    arr[left], arr[high] = arr[high], arr[left]
    return high


# 메뉴 출력 및 사용자 입력 처리
def display_menu():
    print("\n학생 성적 관리 시스템")
    print("1. 이름을 기준으로 정렬")
    print("2. 나이를 기준으로 정렬")
    print("3. 성적을 기준으로 정렬")
    print("4. 프로그램 종료")
    while True:
        try:
            choice = int(input("원하는 작업을 선택하세요: "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("1~4 사이의 숫자를 입력하세요.")
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")


# 메인 프로그램
def main():
    students = generate_students()
    print("정렬 전 상태:")
    for student in students:
            print(student)
    while True:
        choice = display_menu()
        if choice == 4:
            print("프로그램을 종료합니다.")
            break

        print("\n1. 선택 정렬")
        print("2. 삽입 정렬")
        print("3. 퀵 정렬")
        if choice == 3:  # 성적 정렬 시 기수 정렬 가능
            print("4. 기수 정렬")
        sort_choice = int(input("사용할 정렬 알고리즘을 선택하세요: "))

        key = "이름" if choice == 1 else "나이" if choice == 2 else "성적"

        if sort_choice == 1:
            selection_sort(students, key)
        elif sort_choice == 2:
            insertion_sort(students, key)
        elif sort_choice == 3:
            quick_sort(students, 0, len(students) - 1, key)
        elif sort_choice == 4 and choice == 3:
            radix_sort(students, "성적")
        else:
            
            print("잘못된 입력입니다.")
            continue

        print(f"\n{key} 기준으로 정렬된 결과:")
        for student in students:
            print(student)


# 프로그램 실행
if __name__ == "__main__":
    main()

