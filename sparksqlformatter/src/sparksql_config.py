# -*- coding: utf-8 -*-


class SparkSQL:
    # http://spark.apache.org/docs/latest/sql-ref-ansi-compliance.html#sql-keywords
    class Keyword:
        RESERVED_KEYWORDS = [
            'ALL',
            'ANALYZE',
            'AND',
            'ANY',
            'ARRAY',
            'AS',
            'ASC',
            'AT',
            'BETWEEN',
            'BOTH',
            'BY',
            'CASE',
            'CAST',
            'CHECK',
            'COLLATE',
            'COLUMN',
            'CONSTRAINT',
            'CREATE',
            'CROSS',
            'CURRENT',
            'CURRENT_DATE',
            'CURRENT_TIME',
            'CURRENT_TIMESTAMP',
            'CURRENT_USER',
            'DATABASE',
            'DAY',
            'DELETE',
            'DESC',
            'DESCRIBE',
            'DISTINCT',
            'DIV',
            'DROP',
            'ELSE',
            'END',
            'ESCAPE',
            'EXCEPT',
            'EXISTS',
            'EXTERNAL',
            'EXTRACT',
            'FALSE',
            'FETCH',
            'FILTER'
            'FOLLOWING',
            'FOR',
            'FOREIGN',
            'FROM',
            'FULL',
            'FUNCTION',
            'GLOBAL',
            'GRANT',
            'GROUP',
            'GROUPING',
            'HAVING',
            'HOUR',
            'IF',
            'IN',
            'INNER',
            'INSERT',
            'INTERSECT',
            'INTERVAL',
            'INTO',
            'IS',
            'JOIN',
            'KEYS',
            'LATERAL',
            'LEADING',
            'LEFT',
            'LIKE',
            'LIMIT',
            'LOCAL',
            'MINUS',
            'MINUTE',
            'MONTH',
            'NATURAL',
            'NO',
            'NOT',
            'NULL',
            'OF',
            'ON',
            'ONLY',
            'OPTION',
            'OPTIONS',
            'ORDER',
            'OUT',
            'OUTER',
            'OVER',
            'OVERLAPS',
            'PARTITION',
            'POSITION',
            'PRIMARY',
            'REFERENCES',
            'REPAIR',
            'RIGHT',
            'ROW',
            'ROWS',
            'SCHEMA',
            'SECOND',
            'SELECT',
            'SEMI',
            'SESSION_USER',
            'SET',
            'SKEWED',
            'SOME',
            'SORT',
            'START',
            'TABLE',
            'THEN',
            'TO',
            'TRAILING',
            'TRUE',
            'TRUNCATE',
            'UNBOUNDED',
            'UNION',
            'UNIQUE',
            'UNKNOWN',
            'UPDATE',
            'USE',
            'USER',
            'USING',
            'VALUES',
            'VIEW',
            'WHEN',
            'WHERE',
            'WINDOW',
            'WITH',
            'YEAR'
        ]

        NON_RESERVED_KEYWORDS = [
            'ADD',
            'AFTER',
            'ALTER',
            'ANTI',
            'ARCHIVE',
            'AUTHORIZATION',
            'BUCKET',
            'BUCKETS',
            'CACHE',
            'CASCADE',
            'CHANGE',
            'CLEAR',
            'CLUSTER',
            'CLUSTERED',
            'CODEGEN',
            'COLLECTION',
            'COLUMNS',
            'COMMENT',
            'COMMIT',
            'COMPACT',
            'COMPACTIONS',
            'COMPUTE',
            'CONCATENATE',
            'COST',
            'CUBE',
            'DATA',
            'DATABASES',
            'DBPROPERTIES',
            'DEFINED',
            'DELIMITED',
            'DFS',
            'DIRECTORIES',
            'DIRECTORY',
            'DISTRIBUTE',
            'ESCAPED',
            'EXCHANGE',
            'EXPLAIN',
            'EXPORT',
            'EXTENDED',
            'FIELDS',
            'FILEFORMAT',
            'FIRST',
            'FORMAT',
            'FORMATTED',
            'FUNCTIONS',
            'IGNORE',
            'IMPORT',
            'INDEX',
            'INDEXES',
            'INPATH',
            'INPUTFORMAT',
            'ITEMS',
            'LAST',
            'LAZY',
            'LINES',
            'LIST',
            'LOAD',
            'LOCATION',
            'LOCK',
            'LOCKS',
            'LOGICAL',
            'MACRO',
            'MAP',
            'MATCHED',
            'MERGE',
            'MSCK',
            'NAMESPACE',
            'NAMESPACES',
            'NULLS',
            'OUTPUTFORMAT',
            'OVERLAY',
            'OVERWRITE',
            'PARTITIONED',
            'PARTITIONS',
            'PERCENT',
            'PIVOT',
            'PLACING',
            'PRECEDING',
            'PRINCIPALS',
            'PROPERTIES',
            'PURGE',
            'QUERY',
            'RECORDREADER',
            'RECORDWRITER',
            'RECOVER',
            'REDUCE',
            'REFRESH',
            'RENAME',
            'REPLACE',
            'RESET',
            'RESTRICT',
            'REVOKE',
            'RLIKE',
            'ROLE',
            'ROLES',
            'ROLLBACK',
            'ROLLUP',
            'SEPARATED',
            'SERDE',
            'SERDEPROPERTIES',
            'SETS',
            'SHOW',
            'SORTED',
            'STATISTICS',
            'STORED',
            'STRATIFY',
            'STRUCT',
            'SUBSTR',
            'SUBSTRING',
            'TABLES',
            'TABLESAMPLE',
            'TBLPROPERTIES',
            'TEMPORARY',
            'TERMINATED',
            'TOUCH',
            'TRANSACTION',
            'TRANSACTIONS',
            'TRANSFORM',
            'TRIM',
            'UNARCHIVE',
            'UNCACHE',
            'UNLOCK',
            'UNSET',
            'VIEWS'
        ]

        TOP_LEVEL_KEYWORDS = [
            'ADD',
            'AFTER',
            'ALTER COLUMN',
            'ALTER TABLE',
            'CROSS JOIN',
            'DELETE FROM',
            'EXCEPT',
            'FETCH FIRST',
            'FROM',
            'GROUP BY',
            'GO',
            'HAVING',
            'INNER JOIN',
            'INSERT INTO',
            'INSERT',
            'JOIN',
            'LEFT JOIN',
            'LEFT OUTER JOIN',
            'LIMIT',
            'MODIFY',
            'ORDER BY',
            'OUTER JOIN',
            'RIGHT JOIN',
            'RIGHT OUTER JOIN',
            'SELECT',
            'SET CURRENT SCHEMA',
            'SET SCHEMA',
            'SET',
            'UPDATE',
            'VALUES',
            'WHERE'
        ]

        TOP_LEVEL_KEYWORDS_NO_INDENT = ['INTERSECT', 'INTERSECT ALL', 'MINUS', 'UNION', 'UNION ALL']

        NEWLINE_KEYWORDS = [
            'AND',
            # 'CROSS JOIN',
            'ELSE',
            # 'INNER JOIN',
            # 'JOIN',
            'LATERAL',
            # 'LEFT JOIN',
            # 'LEFT OUTER JOIN',
            'ON',
            'OR',
            # 'OUTER JOIN',
            # 'RIGHT JOIN',
            # 'RIGHT OUTER JOIN',
            'THEN',
            'WHEN',
            'XOR'
        ]

    class Function:
        # http://spark.apache.org/docs/latest/sql-ref-functions-builtin.html
        AGGREGATE_FUNCTIONS = [
            'any',
            'approx_count_distinct',
            'approx_percentile',
            'avg',
            'bit_or',
            'bit_xor',
            'bool_and',
            'bool_or',
            'collect_list',
            'collect_set',
            'corr',
            'count',
            'count_if',
            'count_min_sketch',
            'covar_pop',
            'covar_samp',
            'every',
            'first',
            'first_value',
            'kurtosis',
            'last',
            'last_value',
            'max',
            'mean',
            'min',
            'min_by',
            'percentile',
            'skewness',
            'some',
            'std',
            'stddev',
            'stddev_pop',
            'stddev_samp',
            'sum',
            'var_pop',
            'var_samp',
            'variance'
        ]
        WINDOW_FUNCTIONS = ['cume_dist', 'dense_rank', 'lag', 'lead', 'ntile', 'percent_rank', 'rank', 'row_number']
        ARRAY_FUNCTIONS = [
            'array_contains',
            'array_distinct',
            'array_except',
            'array_intersect',
            'array_join',
            'array_max',
            'array_min',
            'array_position',
            'array_remove',
            'array_repeat',
            'array_union',
            'arrays_overlap',
            'arrays_zip',
            'concat',
            'flatten',
            'reverse',
            'sequence',
            'shuffle',
            'slice',
            'sort_array'
        ]
        MAP_FUNCTIONS = ['map_concat', 'map_entries', 'map_from_entries', 'map_keys', 'map_values']
        DATE_TIME_FUNCTIONS = [
            'add_months',
            'current_date',
            'current_timestamp',
            'date_add',
            'date_format',
            'date_part',
            'date_sub',
            'date_trunc',
            'datediff',
            'dayofweek',
            'dayofyear',
            'from_unixtime',
            'from_utc_timestamp',
            'hour',
            'last_day',
            'make_date',
            'make_timestamp',
            'minute',
            'month',
            'months_between',
            'next_day',
            'now',
            'quarter',
            'second',
            'to_date',
            'to_timestamp',
            'to_unix_timestamp',
            'to_utc_timestamp',
            'trunc',
            'unix_timestamp',
            'weekday',
            'weekofyear',
            'year'
        ]
        JSON_FUNCTIONS = ['from_json', 'get_json_object', 'json_tuple', 'schema_of_json', 'to_json']


class HiveQL:
    # https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL
    class Keyword:
        RESERVED_KEYWORDS = [
            'ALL',
            'ALTER',
            'AND',
            'ARRAY',
            'AS',
            'AUTHORIZATION',
            'BETWEEN',
            'BIGINT',
            'BINARY',
            'BOOLEAN',
            'BOTH',
            'BY',
            'CACHE',
            'CASE',
            'CAST',
            'CHAR',
            'COLUMN',
            'COMMIT',
            'CONF',
            'CONSTRAINT',
            'CREATE',
            'CROSS',
            'CUBE',
            'CURRENT',
            'CURRENT_DATE',
            'CURRENT_TIMESTAMP',
            'CURSOR',
            'DATABASE',
            'DATE',
            'DAYOFWEEK',
            'DECIMAL',
            'DELETE',
            'DESCRIBE',
            'DISTINCT',
            'DOUBLE',
            'DROP',
            'ELSE',
            'END',
            'EXCHANGE',
            'EXISTS',
            'EXTENDED',
            'EXTERNAL',
            'EXTRACT',
            'FALSE',
            'FETCH',
            'FLOAT',
            'FLOOR',
            'FOLLOWING',
            'FOR',
            'FOREIGN',
            'FROM',
            'FULL',
            'FUNCTION',
            'GRANT',
            'GROUP',
            'GROUPING',
            'HAVING',
            'IF',
            'IMPORT',
            'IN',
            'INNER',
            'INSERT',
            'INT',
            'INTEGER',
            'INTERSECT',
            'INTERVAL',
            'INTO',
            'IS',
            'JOIN',
            'LATERAL',
            'LEFT',
            'LESS',
            'LIKE',
            'LOCAL',
            'MACRO',
            'MAP',
            'MORE',
            'NONE',
            'NOT',
            'NULL',
            'NUMERIC',
            'OF',
            'ON',
            'ONLY',
            'OR',
            'ORDER',
            'OUT',
            'OUTER',
            'OVER',
            'PARTIALSCAN',
            'PARTITION',
            'PERCENT',
            'PRECEDING',
            'PRECISION',
            'PRESERVE',
            'PRIMARY',
            'PROCEDURE',
            'RANGE',
            'READS',
            'REDUCE',
            'REFERENCES',
            # 'REGEXP',
            'REVOKE',
            'RIGHT',
            # 'RLIKE',
            'ROLLBACK',
            'ROLLUP',
            'ROW',
            'ROWS',
            'SELECT',
            'SET',
            'SMALLINT',
            'START',
            'SYNC',
            'TABLE',
            'TABLESAMPLE',
            'THEN',
            'TIME',
            'TIMESTAMP',
            'TO',
            'TRANSFORM',
            'TRIGGER',
            'TRUE',
            'TRUNCATE',
            'UNBOUNDED',
            'UNION',
            'UNIQUEJOIN',
            'UPDATE',
            'USER',
            'USING',
            'UTC_TMESTAMP',
            'VALUES',
            'VARCHAR',
            'VIEWS',
            'WHEN',
            'WHERE',
            'WINDOW',
            'WITH'
        ]

        NON_RESERVED_KEYWORDS = [
            'ADD',
            'ABORT',
            'ADMIN',
            'AFTER',
            'ANALYZE',
            'ARCHIVE',
            'ASC',
            'AUTOCOMMIT',
            'BEFORE',
            'BUCKET',
            'BUCKETS',
            'CASCADE',
            'CHANGE',
            'CLUSTER',
            'CLUSTERED',
            'CLUSTERSTATUS',
            'COLLECTION',
            'COLUMNS',
            'COMMENT',
            'COMPACT',
            'COMPACTIONS',
            'COMPUTE',
            'CONCATENATE',
            'CONTINUE',
            'DATA',
            'DATABASES',
            'DATETIME',
            'DAY',
            'DAYS',
            'DBPROPERTIES',
            'DEFERRED',
            'DEFINED',
            'DELIMITED',
            'DEPENDENCY',
            'DESC',
            'DETAIL',
            'DIRECTORIES',
            'DIRECTORY',
            'DISABLE',
            'DISTRIBUTE',
            'DOW',
            'ELEM_TYPE',
            'ENABLE',
            'ESCAPED',
            'EXCLUSIVE',
            'EXPLAIN',
            'EXPORT',
            'EXPRESSION',
            'FIELDS',
            'FILE',
            'FILEFORMAT',
            'FIRST',
            'FORMAT',
            'FORMATTED',
            'FUNCTIONS',
            'HOLD_DDLTIME',
            'HOUR',
            'HOURS',
            'IDXPROPERTIES',
            'IGNORE',
            'INDEX',
            'INDEXES',
            'INPATH',
            'INPUTDRIVER',
            'INPUTFORMAT',
            'ISOLATION',
            'ITEMS',
            'JAR',
            'KEY',
            'KEYS',
            'KEY_TYPE',
            'LAST',
            'LEVEL',
            'LIMIT',
            'LINES',
            'LOAD',
            'LOCATION',
            'LOCK',
            'LOCKS',
            'LOGICAL',
            'LONG',
            'MAPJOIN',
            'MATERIALIZED',
            'METADATA',
            'MINUS',
            'MINUTE',
            'MINUTES',
            'MONTH',
            'MONTHS',
            'MSCK',
            'NORELY',
            'NOSCAN',
            'NOVALIDATE',
            'NO_DROP',
            'NULLS',
            'OFFLINE',
            'OFFSET',
            'OPERATOR',
            'OPTION',
            'OUTPUTDRIVER',
            'OUTPUTFORMAT',
            'OVERWRITE',
            'OWNER',
            'PARTITIONED',
            'PARTITIONS',
            'PLUS',
            'PRETTY',
            'PRINCIPALS',
            'PROTECTION',
            'PURGE',
            'QUARTER',
            'READ',
            'READONLY',
            'REBUILD',
            'RECORDREADER',
            'RECORDWRITER',
            'REGEXP',
            'RELOAD',
            'RELY',
            'RENAME',
            'REPAIR',
            'REPLACE',
            'REPLICATION',
            'RESTRICT',
            'REWRITE',
            'RLIKE',
            'ROLE',
            'ROLES',
            'SCHEMA',
            'SCHEMAS',
            'SECOND',
            'SECONDS',
            'SEMI',
            'SERDE',
            'SERDEPROPERTIES',
            'SERVER',
            'SETS',
            'SHARED',
            'SHOW',
            'SHOW_DATABASE',
            'SKEWED',
            'SNAPSHOT',
            'SORT',
            'SORTED',
            'SSL',
            'STATISTICS',
            'STORED',
            'STREAMTABLE',
            'STRING',
            'STRUCT',
            'SUMMARY',
            'TABLES',
            'TBLPROPERTIES',
            'TEMPORARY',
            'TERMINATED',
            'TIMESTAMPTZ',
            'TINYINT',
            'TOUCH',
            'TRANSACTION',
            'TRANSACTIONS',
            'UNARCHIVE',
            'UNDO',
            'UNIONTYPE',
            'UNLOCK',
            'UNSET',
            'UNSIGNED',
            'URI',
            'USE',
            'UTC',
            'UTCTIMESTAMP',
            'VALIDATE',
            'VALUE_TYPE',
            'VECTORIZATION',
            'VIEW',
            'WEEK',
            'WEEKS',
            'WHILE',
            'WORK',
            'WRITE',
            'YEAR',
            'YEARS',
            'ZONE'
        ]

    # https://cwiki.apache.org/confluence/display/Hive/LanguageManual+UDF
    class Function:
        MATHEMATICAL_FUNCTIONS = [
            'round',
            'ceil',
            'ceiling',
            'rand',
            'exp',
            'ln',
            'log10',
            'log2',
            'log',
            'pow',
            'power',
            'sqrt',
            'bin',
            'hex',
            'unhdex',
            'conv',
            'abs',
            'pmod',
            'sin',
            'asin',
            'cos',
            'acos',
            'tan',
            'atan',
            'degrees',
            'radians',
            'positive',
            'negative',
            'sign',
            'e',
            'pi',
            'factorial',
            'cbrt',
            'shiftleft',
            'shiftright',
            'shiftrightunsigned',
            'greatest',
            'least',
            'width_bucket'
        ]

        COLLECTION_FUNCTIONS = ['size', 'map_keys', 'map_values', 'array_contains', 'sort_array']

        TYPE_CONVERSION_FUNCTIONS = ['binary', 'cast']

        DATE_TIME_FUNCTIONS = [
            'from_unixtime',
            'unix_timestamp',
            'to_date',
            'year',
            'quarter',
            'month',
            'day',
            'hour',
            'minute',
            'second',
            'weekofyear',
            'extract',
            'datediff',
            'date_add',
            'date_sub',
            'from_utc_timestamp',
            'to_utc_timestamp',
            'current_date',
            'current_timestamp',
            'add_months',
            'last_day',
            'next_day',
            'trunc',
            'months_between',
            'date_format'
        ]

        CONDITIONAL_FUNCTIONS = ['if', 'isnull', 'isnotnull', 'nvl', 'COALESCE', 'nullif', 'assert_true']

        STRING_FUNCTIONS = [
            'ascii',
            'base64',
            'character_length',
            'chr',
            'concat',
            'context_ngrams',
            'concat_ws',
            'decode',
            'elt',
            'encode',
            'field',
            'find_in_set',
            'format_number',
            'get_json_object',
            'in_file',
            'instr',
            'length',
            'locate',
            'lower',
            'lpad',
            'ltrim',
            'ngrams',
            'octet_length',
            'parse_url',
            'printf',
            'quote',
            'regexp_extract',
            'regexp_replace',
            'repeat',
            'replace',
            'reverse',
            'rpad',
            'rtrim',
            'sentences',
            'space',
            'split',
            'str_to_map',
            'substr',
            'substring_index',
            'translate',
            'trim',
            'unbase64',
            'upper',
            'initcap',
            'levenhtein',
            'soundex'
        ]

        DATA_MASKING_FUNCTIONS = [
            'mask',
            'mask_first_n',
            'mask_last_n',
            'mask_show_first_n',
            'mask_show_last_n',
            'mask_hash'
        ]

        MISC_FUNCTIONS = [
            'java_method',
            'reflect',
            'hash',
            'current_user',
            'logged_in_user',
            'current_database',
            'md5',
            'sha1',
            'sha',
            'crc32',
            'sha2',
            'aes_decrypt',
            'version',
            'surrogate_key'
        ]

        AGGREGATE_FUNCTIONS = [
            'count',
            'sum',
            'avg',
            'min',
            'max',
            'variance',
            'var_samp',
            'stddev_pop',
            'stddev_samp',
            'covar_pop',
            'covar_samp',
            'corr',
            'percentile',
            'percentile_approx',
            'regr_avgx',
            'regr_avgy',
            'regr_count',
            'regr_intercept',
            'regr_r2',
            'regr_slope',
            'regr_sxx',
            'regr_sxy',
            'regr_syy',
            'histogram_numeric',
            'collect_set',
            'collect_list',
            'ntile'
        ]

        TABLE_GENERATING_FUNCTIONS = ['explode', 'posexplode', 'inline', 'stack', 'json_tuple', 'parse_url_tuple']

        # https://cwiki.apache.org/confluence/display/Hive/LanguageManual+WindowingAndAnalytics#LanguageManualWindowingAndAnalytics-EnhancementstoHiveQL
        WINDOWING_FUNCTIONS = ['LEAD', 'LAG', 'FIRST_VALUE', 'LAST_VALUE']

        ANALYTICS_FUNCTIONS = ['RANK', 'ROW_NUMBER', 'DENSE_RANK', 'CUME_DIST', 'PERCENT_RANK', 'NTILE']


DEFAULT_CONFIG_SECTION = 'sparksqlformatter'  # default section heading for config files


class Keyword:
    RESERVED_KEYWORDS = list(set(SparkSQL.Keyword.RESERVED_KEYWORDS + HiveQL.Keyword.RESERVED_KEYWORDS))
    NON_RESERVED_KEYWORDS = [
        w for w in list(set(SparkSQL.Keyword.NON_RESERVED_KEYWORDS + HiveQL.Keyword.NON_RESERVED_KEYWORDS))
        if w not in RESERVED_KEYWORDS
    ]
    TOP_LEVEL_KEYWORDS = SparkSQL.Keyword.TOP_LEVEL_KEYWORDS
    TOP_LEVEL_KEYWORDS_NO_INDENT = SparkSQL.Keyword.TOP_LEVEL_KEYWORDS_NO_INDENT
    NEWLINE_KEYWORDS = SparkSQL.Keyword.NEWLINE_KEYWORDS


class Function:
    AGGREGATE_FUNCTIONS = list(set(SparkSQL.Function.AGGREGATE_FUNCTIONS + HiveQL.Function.AGGREGATE_FUNCTIONS))
    MATHEMATICAL_FUNCTIONS = HiveQL.Function.MATHEMATICAL_FUNCTIONS
    DATE_TIME_FUNCTIONS = list(set(SparkSQL.Function.DATE_TIME_FUNCTIONS + HiveQL.Function.DATE_TIME_FUNCTIONS))
    ARRAY_FUNCTIONS = list(
        set(SparkSQL.Function.ARRAY_FUNCTIONS + SparkSQL.Function.MAP_FUNCTIONS + HiveQL.Function.COLLECTION_FUNCTIONS))
    STRING_FUNCTIONS = list(set(SparkSQL.Function.JSON_FUNCTIONS + HiveQL.Function.STRING_FUNCTIONS))
    WINDOW_FUNCTIONS = list(
        set(SparkSQL.Function.WINDOW_FUNCTIONS + HiveQL.Function.WINDOWING_FUNCTIONS +
            HiveQL.Function.ANALYTICS_FUNCTIONS))
    CONDITIONAL_FUNCTIONS = HiveQL.Function.CONDITIONAL_FUNCTIONS
    TYPE_CONVERSION_FUNCTIONS = HiveQL.Function.TYPE_CONVERSION_FUNCTIONS
    DATA_MASKING_FUNCTIONS = HiveQL.Function.DATA_MASKING_FUNCTIONS
    MISC_FUNCTIONS = HiveQL.Function.MISC_FUNCTIONS
    TABLE_GENERATING_FUNCTIONS = HiveQL.Function.TABLE_GENERATING_FUNCTIONS