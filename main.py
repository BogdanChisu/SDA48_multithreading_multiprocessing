# import threading
# from time import sleep
# # def va_itera(iterabil_element):
# #     for el in iterabil_element:
# #         print(el)
# #
# # job_1 = threading.Thread(target= va_itera, args=(range(1,9,2),))
# # job_2 = threading.Thread(target= va_itera, args=(range(11,20,2),))
# # job_3 = threading.Thread(target= va_itera, args=(range(111,119,2),))
# #
# # #incepem procesele
# # job_1.start()
# # job_2.start()
# # job_3.start()
# #
# # #waiting for jobs to finish
# # # job_1.join()
# # # job_2.join()
# # # job_3.join()
# #
# # print("\nFinally here")
#
# class ThreadingCuValoare(threading.Thread):
#
#     def __init__(self, target, args=()):
#         self.target = target
#         self.args = args
#         super().__init__()
#
#     def run(self):
#         self.result = self.target(*self.args)
#
#     def join(self, timeout = None):
#         super().join(timeout)
#         return self.result
#
# def print_a_la_puterea_b(a,b):
#     sleep(1)
#     return f"a la puterea b = {a**b}"
#
# job_1 = ThreadingCuValoare(target=print_a_la_puterea_b, args=(3,4))
# job_2 = ThreadingCuValoare(target=print_a_la_puterea_b, args=(2,5))
#
# job_1.start()
# job_2.start()
#
# valoarea_pentru_job_1 = job_1.join()
# valoarea_pentru_job_2 = job_2.join()
# print(valoarea_pentru_job_1)
# print(valoarea_pentru_job_2)

# from time import sleep
# import multiprocessing
def print_from_range(de_la:int, pana_la:int):
    for x in range(de_la, pana_la):
        sleep(0.3)
        print(x)
#
# if __name__ == "__main__":
#     process_1 = multiprocessing.Process(target=print_from_range, args=(1,9))
#     # sleep(5)
#     process_2 = multiprocessing.Process(target=print_from_range, args=(11,19))
#
#     process_1.start()
#     sleep(1)
#     process_2.start()
#
#     process_1.join()
#     sleep(1)
#     process_2.join()