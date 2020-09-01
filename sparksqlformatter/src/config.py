# -*- coding: utf-8 -*-


class SparkSQL:
    # http://spark.apache.org/docs/latest/sql-ref-ansi-compliance.html#sql-keywords
    class Keyword:
        RESERVED_KEYWORDS = [
            'ALL', 'ALTER', 'ANALYZE', 'AND', 'ANY', 'ARRAY', 'AS', 'ASC', 'AT', 'BETWEEN', 'BOTH', 'BY', 'CASE',
            'CAST', 'CHECK', 'COLLATE', 'COLUMN', 'CONSTRAINT', 'CREATE', 'CROSS', 'CURRENT', 'CURRENT_DATE',
            'CURRENT_TIME', 'CURRENT_TIMESTAMP', 'CURRENT_USER', 'DATABASE', 'DAY', 'DELETE', 'DESC', 'DESCRIBE',
            'DISTINCT', 'DIV', 'DROP', 'ELSE', 'END', 'ESCAPE', 'EXCEPT', 'EXISTS', 'EXTERNAL', 'EXTRACT', 'FALSE',
            'FETCH', 'FILTER', 'FOLLOWING', 'FOR', 'FOREIGN', 'FROM', 'FULL', 'FUNCTION', 'GLOBAL', 'GRANT', 'GROUP',
            'GROUPING', 'HAVING', 'HOUR', 'IF', 'IN', 'INNER', 'INSERT', 'INTERSECT', 'INTERVAL', 'INTO', 'IS', 'JOIN',
            'KEYS', 'LATERAL', 'LEADING', 'LEFT', 'LIKE', 'LIMIT', 'LOCAL', 'MINUS', 'MINUTE', 'MONTH', 'MSCK',
            'NATURAL', 'NO', 'NOT', 'NULL', 'OF', 'ON', 'ONLY', 'OPTION', 'OPTIONS', 'OR', 'ORDER', 'OUT', 'OUTER',
            'OVER', 'OVERLAPS', 'PARTITION', 'PARTITIONED', 'POSITION', 'PRIMARY', 'REFERENCES', 'REPAIR', 'RIGHT',
            'ROW', 'ROWS', 'SCHEMA', 'SECOND', 'SELECT', 'SEMI', 'SESSION_USER', 'SET', 'SKEWED', 'SOME', 'SORT',
            'START', 'TABLE', 'THEN', 'TO', 'TRAILING', 'TRUE', 'TRUNCATE', 'UNBOUNDED', 'UNION', 'UNIQUE', 'UNKNOWN',
            'UPDATE', 'USE', 'USER', 'USING', 'VALUES', 'VIEW', 'WHEN', 'WHERE', 'WINDOW', 'WITH', 'YEAR'
        ]

        NON_RESERVED_KEYWORDS = [
            'ADD', 'AFTER', 'ANTI', 'ARCHIVE', 'AUTHORIZATION', 'BUCKET', 'BUCKETS', 'CACHE', 'CASCADE', 'CHANGE',
            'CLEAR', 'CLUSTER', 'CLUSTERED', 'CODEGEN', 'COLLECTION', 'COLUMNS', 'COMMENT', 'COMMIT', 'COMPACT',
            'COMPACTIONS', 'COMPUTE', 'CONCATENATE', 'COST', 'CUBE', 'DATA', 'DATABASES', 'DBPROPERTIES', 'DEFINED',
            'DELIMITED', 'DFS', 'DIRECTORIES', 'DIRECTORY', 'DISTRIBUTE', 'ESCAPED', 'EXCHANGE', 'EXPLAIN', 'EXPORT',
            'EXTENDED', 'FIELDS', 'FILEFORMAT', 'FIRST', 'FORMAT', 'FORMATTED', 'FUNCTIONS', 'IGNORE', 'IMPORT',
            'INDEX', 'INDEXES', 'INPATH', 'INPUTFORMAT', 'ITEMS', 'LAST', 'LAZY', 'LINES', 'LIST', 'LOAD', 'LOCATION',
            'LOCK', 'LOCKS', 'LOGICAL', 'MACRO', 'MAP', 'MATCHED', 'MERGE', 'NAMESPACE', 'NAMESPACES', 'NULLS',
            'OUTPUTFORMAT', 'OVERLAY', 'OVERWRITE', 'PARTITIONS', 'PERCENT', 'PIVOT', 'PLACING', 'PRECEDING',
            'PRINCIPALS', 'PROPERTIES', 'PURGE', 'QUERY', 'RECORDREADER', 'RECORDWRITER', 'RECOVER', 'REDUCE',
            'REFRESH', 'RENAME', 'REPLACE', 'RESET', 'RESTRICT', 'REVOKE', 'RLIKE', 'ROLE', 'ROLES', 'ROLLBACK',
            'ROLLUP', 'SEPARATED', 'SERDE', 'SERDEPROPERTIES', 'SETS', 'SHOW', 'SORTED', 'STATISTICS', 'STORED',
            'STRATIFY', 'STRUCT', 'SUBSTR', 'SUBSTRING', 'TABLES', 'TABLESAMPLE', 'TBLPROPERTIES', 'TEMPORARY',
            'TERMINATED', 'TOUCH', 'TRANSACTION', 'TRANSACTIONS', 'TRANSFORM', 'TRIM', 'UNARCHIVE', 'UNCACHE', 'UNLOCK',
            'UNSET', 'VIEWS'
        ]

        DATA_TYPES = [
            'BOOLEAN', 'BYTE', 'TINYINT', 'SHORT', 'SMALLINT', 'INT', 'INTEGER', 'LONG', 'BIGINT', 'FLOAT', 'REAL',
            'DOUBLE', 'DATE', 'TIMESTAMP', 'STRING', 'BINARY', 'DECIMAL', 'DEC', 'NUMERIC', 'INTERVAL', 'ARRAY',
            'STRUCT', 'MAP'
        ]

        TOP_LEVEL_KEYWORDS = [
            'ADD', 'AFTER', 'ALTER COLUMN', 'ALTER TABLE', 'CREATE TABLE', 'CROSS JOIN', 'DELETE FROM', 'ELSE',
            'EXCEPT', 'FETCH FIRST', 'FROM', 'GROUP BY', 'GO', 'HAVING', 'INNER JOIN', 'INSERT INTO', 'INSERT', 'JOIN',
            'LEFT JOIN', 'LEFT OUTER JOIN', 'LIMIT', 'MODIFY', 'ORDER BY', 'OUTER JOIN', 'PARTITION BY', 'RIGHT JOIN',
            'RIGHT OUTER JOIN', 'SELECT', 'SET CURRENT SCHEMA', 'SET SCHEMA', 'SET', 'THEN', 'UPDATE', 'VALUES', 'WHEN',
            'WHERE'
        ]

        TOP_LEVEL_KEYWORDS_NO_INDENT = ['INTERSECT ALL', 'INTERSECT', 'MINUS', 'UNION ALL', 'UNION']

        NEWLINE_KEYWORDS = [
            'AND', 'ELSE', 'LATERAL', 'ON', 'OPTIONS', 'OR', 'PARTITIONED BY', 'THEN', 'USING', 'WHEN', 'XOR'
        ]

    class Function:
        # http://spark.apache.org/docs/latest/sql-ref-functions-builtin.html
        AGGREGATE_FUNCTIONS = [
            'any', 'approx_count_distinct', 'approx_percentile', 'avg', 'bit_or', 'bit_xor', 'bool_and', 'bool_or',
            'collect_list', 'collect_set', 'corr', 'count', 'count_if', 'count_min_sketch', 'covar_pop', 'covar_samp',
            'every', 'first', 'first_value', 'kurtosis', 'last', 'last_value', 'max', 'mean', 'min', 'min_by',
            'percentile', 'skewness', 'some', 'std', 'stddev', 'stddev_pop', 'stddev_samp', 'sum', 'var_pop',
            'var_samp', 'variance'
        ]
        ARRAY_FUNCTIONS = [
            'array_contains', 'array_distinct', 'array_except', 'array_intersect', 'array_join', 'array_max',
            'array_min', 'array_position', 'array_remove', 'array_repeat', 'array_union', 'arrays_overlap',
            'arrays_zip', 'concat', 'flatten', 'reverse', 'sequence', 'shuffle', 'slice', 'sort_array'
        ]
        DATE_TIME_FUNCTIONS = [
            'add_months', 'current_date', 'current_timestamp', 'date_add', 'date_format', 'date_part', 'date_sub',
            'date_trunc', 'datediff', 'dayofweek', 'dayofyear', 'from_unixtime', 'from_utc_timestamp', 'hour',
            'last_day', 'make_date', 'make_timestamp', 'minute', 'month', 'months_between', 'next_day', 'now',
            'quarter', 'second', 'to_date', 'to_timestamp', 'to_unix_timestamp', 'to_utc_timestamp', 'trunc',
            'unix_timestamp', 'weekday', 'weekofyear', 'year'
        ]
        JSON_FUNCTIONS = ['from_json', 'get_json_object', 'json_tuple', 'schema_of_json', 'to_json']
        MAP_FUNCTIONS = ['map_concat', 'map_entries', 'map_from_entries', 'map_keys', 'map_values']
        WINDOW_FUNCTIONS = ['cume_dist', 'dense_rank', 'lag', 'lead', 'ntile', 'percent_rank', 'rank', 'row_number']


class SQL:
    # http://spark.apache.org/docs/latest/api/sql/index.html
    class Function:
        AGGREGATE_FUNCTIONS = [
            'aggregate', 'any', 'approx_count_distinct', 'approx_percentile', 'avg', 'bit_and', 'bit_count',
            'bit_length', 'bit_or', 'bit_xor', 'bool_and', 'bool_or', 'collect_list', 'collect_set', 'corr', 'count',
            'count_if', 'count_min_sketch', 'covar_pop', 'covar_samp', 'every', 'first', 'first_value', 'greatest',
            'kurtosis', 'last', 'last_value', 'least', 'length', 'max', 'max_by', 'mean', 'min', 'min_by',
            'octet_length', 'percentile', 'percentile_approx', 'size', 'skewness', 'some', 'std', 'stddev',
            'stddev_pop', 'stddev_samp', 'sum', 'var_pop', 'var_samp', 'variance'
        ]
        ARRAY_FUNCTIONS = [
            'array', 'array_contains', 'array_distinct', 'array_except', 'array_intersect', 'array_join', 'array_max',
            'array_min', 'array_position', 'array_remove', 'array_repeat', 'array_sort', 'array_union',
            'arrays_overlap', 'arrays_zip', 'cardinality', 'element_at', 'elt', 'exists', 'filter', 'find_in_set',
            'flatten', 'forall', 'reverse', 'sequence', 'shuffle', 'slice', 'sort_array', 'transform', 'zip_with'
        ]
        CONDITIONAL_FUNCTIONS = [
            'assert_true', 'coalesce', 'if', 'ifnull', 'in', 'isnan', 'isnotnull', 'isnull', 'nanvl', 'nullif', 'nvl',
            'nvl2', 'when'
        ]
        DATE_TIME_FUNCTIONS = [
            'add_months', 'current_date', 'current_timestamp', 'date', 'date_add', 'date_format', 'date_part',
            'date_sub', 'date_trunc', 'datediff', 'day', 'dayofmonth', 'dayofweek', 'dayofyear', 'extract',
            'from_unixtime', 'from_utc_timestamp', 'hour', 'last_day', 'make_date', 'make_interval', 'make_timestamp',
            'minute', 'month', 'months_between', 'next_day', 'now', 'quarter', 'second', 'timestamp', 'to_date',
            'to_timestamp', 'to_unix_timestamp', 'to_utc_timestamp', 'trunc', 'unix_timestamp', 'weekday', 'weekofyear',
            'year'
        ]
        HASH_FUNCTIONS = ['hash', 'crc32', 'sha', 'sha1', 'sha2']
        JSON_FUNCTIONS = ['get_json_object', 'schema_of_json', 'json_tuple', 'from_json', 'to_json']
        MAP_FUNCTIONS = [
            'map', 'map_concat', 'map_entries', 'map_filter', 'map_from_arrays', 'map_from_entries', 'map_keys',
            'map_values', 'map_zip_with', 'str_to_map', 'transform_keys', 'transform_values'
        ]
        MATHEMATICAL_FUNCTIONS = [
            'abs', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'bround', 'cbrt', 'ceil', 'ceiling',
            'conv', 'cos', 'cosh', 'cot', 'degrees', 'div', 'e', 'exp', 'expm1', 'factorial', 'floor', 'format_number',
            'hypot', 'ln', 'log', 'log10', 'log1p', 'log2', 'mod', 'pi', 'pmod', 'pow', 'power', 'radians', 'rint',
            'round', 'sign', 'signum', 'sin', 'sinh', 'sqrt', 'tan', 'tanh'
        ]
        MISC_FUNCTIONS = [
            'current_database', 'input_file_block_length', 'input_file_block_start', 'input_file_name', 'grouping',
            'grouping_id', 'java_method', 'monotonically_increasing_id', 'positive', 'rand', 'randn', 'random',
            'reflect', 'cube', 'rollup', 'schema_of_csv', 'spark_partition_id', 'typeof', 'uuid', 'version', 'xxhash64'
        ]
        OPERATOR_FUNCTIONS = ['negative', 'not', 'or', 'shiftleft', 'shiftright', 'shiftrightunsigned']
        STRING_FUNCTIONS = [
            'ascii', 'base64', 'char', 'char_length', 'character_length', 'chr', 'concat', 'concat_ws', 'decode',
            'encode', 'format_string', 'initcap', 'instr', 'lcase', 'left', 'levenshtein', 'like', 'locate', 'lower',
            'lpad', 'ltrim', 'md5', 'overlay', 'parse_url', 'position', 'printf', 'regexp_extract', 'regexp_replace',
            'repeat', 'replace', 'right', 'rlike', 'rpad', 'rtrim', 'sentences', 'soundex', 'space', 'split', 'substr',
            'substring', 'substring_index', 'translate', 'trim', 'ucase', 'unbase64', 'upper'
        ]
        STRUCT_FUNCTIONS = ['from_csv', 'named_struct', 'struct', 'to_csv']
        TABLE_GENERATING_FUNCTIONS = [
            'explode', 'explode_outer', 'inline', 'stack', 'inline_outer', 'posexplode', 'posexplode_outer'
        ]
        TYPE_CONVERSION_FUNCTIONS = [
            'bigint', 'bin', 'binary', 'boolean', 'cast', 'decimal', 'double', 'float', 'hex', 'int', 'smallint',
            'string', 'tinyint', 'unhex'
        ]
        WINDOW_FUNCTIONS = ['cume_dist', 'dense_rank', 'lag', 'lead', 'ntile', 'percent_rank', 'rank', 'row_number']
        XPATH_FUNCTIONS = [
            'xpath', 'xpath_boolean', 'xpath_double', 'xpath_float', 'xpath_int', 'xpath_long', 'xpath_number',
            'xpath_short', 'xpath_string'
        ]


class Keyword:
    RESERVED_KEYWORDS = SparkSQL.Keyword.RESERVED_KEYWORDS
    NON_RESERVED_KEYWORDS = SparkSQL.Keyword.NON_RESERVED_KEYWORDS + SparkSQL.Keyword.DATA_TYPES
    TOP_LEVEL_KEYWORDS = SparkSQL.Keyword.TOP_LEVEL_KEYWORDS
    TOP_LEVEL_KEYWORDS_NO_INDENT = SparkSQL.Keyword.TOP_LEVEL_KEYWORDS_NO_INDENT
    NEWLINE_KEYWORDS = SparkSQL.Keyword.NEWLINE_KEYWORDS


class Function:
    AGGREGATE_FUNCTIONS = list(set(SparkSQL.Function.AGGREGATE_FUNCTIONS + SQL.Function.AGGREGATE_FUNCTIONS))
    ARRAY_FUNCTIONS = list(set(SparkSQL.Function.ARRAY_FUNCTIONS + SQL.Function.ARRAY_FUNCTIONS))
    CONDITIONAL_FUNCTIONS = SQL.Function.CONDITIONAL_FUNCTIONS
    DATE_TIME_FUNCTIONS = list(set(SparkSQL.Function.DATE_TIME_FUNCTIONS + SQL.Function.DATE_TIME_FUNCTIONS))
    HASH_FUNCTIONS = SQL.Function.HASH_FUNCTIONS
    JSON_FUNCTIONS = list(set(SparkSQL.Function.JSON_FUNCTIONS + SQL.Function.JSON_FUNCTIONS))
    MAP_FUNCTIONS = list(set(SparkSQL.Function.MAP_FUNCTIONS + SQL.Function.MAP_FUNCTIONS))
    MATHEMATICAL_FUNCTIONS = SQL.Function.MATHEMATICAL_FUNCTIONS
    MISC_FUNCTIONS = SQL.Function.MISC_FUNCTIONS
    OPERATOR_FUNCTIONS = SQL.Function.OPERATOR_FUNCTIONS
    STRING_FUNCTIONS = list(set(SparkSQL.Function.JSON_FUNCTIONS + SQL.Function.STRING_FUNCTIONS))
    STRUCT_FUNCTIONS = SQL.Function.STRUCT_FUNCTIONS
    TABLE_GENERATING_FUNCTIONS = SQL.Function.TABLE_GENERATING_FUNCTIONS
    TYPE_CONVERSION_FUNCTIONS = SQL.Function.TYPE_CONVERSION_FUNCTIONS
    WINDOW_FUNCTIONS = list(set(SparkSQL.Function.WINDOW_FUNCTIONS + SQL.Function.WINDOW_FUNCTIONS))
    XPATH_FUNCTIONS = SQL.Function.XPATH_FUNCTIONS


KEYWORDS = (Keyword.RESERVED_KEYWORDS + Keyword.NON_RESERVED_KEYWORDS + Function.AGGREGATE_FUNCTIONS +
            Function.ARRAY_FUNCTIONS + Function.CONDITIONAL_FUNCTIONS + Function.DATE_TIME_FUNCTIONS +
            Function.HASH_FUNCTIONS + Function.JSON_FUNCTIONS + Function.MAP_FUNCTIONS +
            Function.MATHEMATICAL_FUNCTIONS + Function.MISC_FUNCTIONS + Function.OPERATOR_FUNCTIONS +
            Function.STRING_FUNCTIONS + Function.STRUCT_FUNCTIONS + Function.TABLE_GENERATING_FUNCTIONS +
            Function.TYPE_CONVERSION_FUNCTIONS + Function.WINDOW_FUNCTIONS + Function.XPATH_FUNCTIONS)
