def load_service_models():
    import pkgutil
    import service

    for service in pkgutil.walk_packages(service.__path__, service.__package__ + '.'):
        if not service.ispkg:
            module = __import__(service.name, globals(), locals(), ['*'])
            if hasattr(module, 'load_model'):
                print("Loading Model from : ", service.name, flush=True)
                module.load_model()


if __name__ == '__main__':
    load_service_models()
