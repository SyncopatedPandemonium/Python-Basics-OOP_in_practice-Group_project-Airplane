from task_2_passenger import Pilot, Crew, Passenger


class BoarderFactory:

    @staticmethod
    def create_object(boarder_type, *args, **kwargs):
        if boarder_type == 'Pilot':
            object = Pilot(*args, **kwargs)
        elif boarder_type == 'Crew':
            object = Crew(*args, **kwargs)
        elif boarder_type == 'Passenger':
            object = Passenger(*args, **kwargs)
        else:
            raise NotImplementedError('Wrong boarder type')
        return object
