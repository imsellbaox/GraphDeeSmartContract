import argparse


def parameter_parser():
    """
    A method to parse up command line parameters. By default it learns on the Erdos-Renyi dataset.
    The default hyperparameters give good results without cross-validation.
    """

    # Experiment parameters
    parser = argparse.ArgumentParser(description='Graph Convolutional Networks')
    parser.add_argument('-D', '--dataset', type=str, default='GRAPH_BY_TOOL_420',
                        choices=['GRAPH_BY_TOOL_172', 'GRAPH_BY_TOOL_420', 'MULTIPLE_NODE_GRAPH', 'SINGLE_NODE_GRAPH', 'SMART_CONTRACT'])
    parser.add_argument('-M', '--model', type=str, default='gcn', choices=['gcn', 'unet', 'mgcn', 'gat', 'gcn_test'])
    parser.add_argument('--lr', type=float, default=0.001, help='learning rate')
    parser.add_argument('--lr_decay_steps', type=str, default='10,20', help='learning rate')
    parser.add_argument('--wd', type=float, default=1e-4, help='weight decay')
    parser.add_argument('-d', '--dropout', type=float, default=0.1, help='dropout rate')
    parser.add_argument('-f', '--filters', type=str, default='64,64,64', help='number of filters in each layer')
    parser.add_argument('--n_hidden', type=int, default=0,
                        help='number of hidden units in a fully connected layer after the last conv layer')
    parser.add_argument('--epochs', type=int, default=50, help='number of epochs')
    parser.add_argument('-b', '--batch_size', type=int, default=32, help='batch size')
    parser.add_argument('-t', '--threads', type=int, default=2, help='number of threads to load data')
    parser.add_argument('--log_interval', type=int, default=1,
                        help='interval (number of batches) of logging')  # interval表示每次batch的倍数
    parser.add_argument('--device', type=str, default='cpu', choices=['cuda', 'cpu'])
    parser.add_argument('--seed', type=int, default=80, help='random seed')  # random seed保证每次训练的结果是一致的
    parser.add_argument('--shuffle_nodes', action='store_true', default=False, help='shuffle nodes for debugging')
    parser.add_argument('-g', '--torch_geom', action='store_true', default=False, help='use PyTorch Geometric')
    parser.add_argument('-a', '--adj_sq', action='store_true', default=False,
                        help='use A^2 instead of A as an adjacency matrix')
    parser.add_argument('-s', '--scale_identity', action='store_true', default=False,
                        help='use 2I instead of I for self connections')
    parser.add_argument('-v', '--visualize', action='store_true', default=False,
                        help='only for unet: save some adjacency matrices and other data as images')
    parser.add_argument('-c', '--use_cont_node_attr', action='store_true', default=True,
                        help='use continuous node attributes in addition to discrete ones')
    parser.add_argument('--alpha', type=float, default=0.2, help='Alpha value for the leaky_relu')
    parser.add_argument('--multi_head', type=int, default=4, help='number of head attentions(Multi-Head)')

    return parser.parse_args()