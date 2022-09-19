import sys, ujson, logging, json_log_formatter 

from ddtrace import patch; patch(logging=True)

FORMAT = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] '
            '[dd.service=%(dd.service)s dd.env=%(dd.env)s dd.version=%(dd.version)s dd.trace_id=%(dd.trace_id)s dd.span_id=%(dd.span_id)s] '
            '- %(message)s')

formatter = json_log_formatter.JSONFormatter()
formatter.json_lib = ujson # type: ignore

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)

logging.basicConfig(format=FORMAT)
custom_logger = logging.getLogger(__name__)
custom_logger.addHandler(handler)
custom_logger.level = logging.INFO