import ClassRequest
import GenAlg

if __name__ == "__main__":

    query = ClassRequest.Request()

    apartment_type = ['End', 'Row']
    apartment_list = [query.end_apartments, query.row_apartments]

    for item in range(2):
        response = query.query_database(apartment_type[item])
        query.unpack_response(apartment_list[item])

    gen_floor = GenAlg.GenerationFloor([1, 0, 60000, 10000, 50, 30, 10, 10])
    best_floor = gen_floor.run_alg(20, query.end_apartments, query.row_apartments)
    best_floor.get_png()
